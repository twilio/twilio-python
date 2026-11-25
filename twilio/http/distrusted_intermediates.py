"""
Refuse TLS connections whose certificate chain contains one of eight intermediate certificates
that are no longer trustworthy.

The private keys of these intermediates are weak, so anyone can use them to issue a certificate that a
default trust store accepts. This is the same list Go distrusts as of Go 1.27.3 and 1.26.10
(CVE-2026-111943, golang/go#82345). Each certificate is identified by the SHA-256 hash of its DER-encoded
SubjectPublicKeyInfo.

The SDK's default clients, ``TwilioHttpClient`` and ``ValidationClient``, apply this check. A client that
brings its own ``requests`` session can opt in with ``mount_distrusted_intermediates_check(session)``.

Python 3.10 and later can read the chain from the standard library's TLS connection. Older versions can't, so
there the SDK's connections use pyOpenSSL (a dependency installed only on those versions), which can.

The two read different chains. Python 3.10 and later check the verified chain, the path OpenSSL built to a trust
anchor. Python 3.7 to 3.9 check the chain the server sent, which usually has no root, as in the Java SDK. Both
check every certificate they get.
"""

import hashlib
import logging
import os
import ssl
import sys
from typing import FrozenSet, Iterable, List, Optional

from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.connection import HTTPSConnection
from urllib3.connectionpool import HTTPSConnectionPool

_logger = logging.getLogger("twilio.http_client")

# Copied from Go commit 7f86f957633ee31a1c17a1eb8452ca7a3d9bc141 (src/crypto/x509/verify.go).
DISTRUSTED_SPKI_SHA256: FrozenSet[str] = frozenset(
    {
        "ebed6475c2c2d80fcb199f3fe8dd6e6b3ce60b77eb15d4e42c3dec0c6f5b5105",
        "49dd353dc2b919a3770645117d0e60c16115e7d1bc259eefe734b00ea434fe5f",
        "e0254c7fcdc265e2f0f8a428dabb75ab4ae039b4872d62f5ee57f0877d5a8a41",
        "5c0660a2b164910d8ff589c18e14552e9e0ec237dcefe2cb736d41a4811f81a0",
        "43bffa19d6ef651451f6841e019931e96f6f2eaeff28ab4b6f1ce4576de2717b",
        "63ecefee431d49523bc1136c4e72d0206a477086caf606cd5cf025686c109cf8",
        "ec4ffa1ad0ac88081314b7aaffef6a91f97cd57291bb5ba686c5415f5eb4f6b6",
        "92c063d67e8f14db71d288e11266ffdaf69cbf115f7bab14f3bc2f68d25e0e30",
    }
)

_warned_unsupported = False


class DistrustedIntermediateError(ssl.SSLError):
    """The server's certificate chain contains a distrusted intermediate certificate."""


# TBSCertificate ::= SEQUENCE { version [0] EXPLICIT OPTIONAL, serialNumber, signature, issuer, validity,
#                               subject, subjectPublicKeyInfo, ... }
def _read_header(der: bytes, offset: int, expected_tag: int = -1):
    """Return (content_offset, content_length) for the DER element at offset."""
    if offset + 2 > len(der):
        raise ValueError("Truncated DER element")
    tag = der[offset]
    if (tag & 0x1F) == 0x1F or (expected_tag != -1 and tag != expected_tag):
        raise ValueError("Unexpected DER tag %d" % tag)
    length = der[offset + 1]
    content_offset = offset + 2
    if length >= 0x80:
        length_bytes = length & 0x7F
        if (
            length_bytes == 0
            or length_bytes > 3
            or content_offset + length_bytes > len(der)
        ):
            raise ValueError("Unsupported DER length")
        length = int.from_bytes(
            der[content_offset : content_offset + length_bytes], "big"
        )
        content_offset += length_bytes
    if content_offset + length > len(der):
        raise ValueError("Truncated DER element")
    return content_offset, length


def _skip(der: bytes, offset: int) -> int:
    content_offset, length = _read_header(der, offset)
    return content_offset + length


def subject_public_key_info(certificate_der: bytes) -> bytes:
    """
    The SubjectPublicKeyInfo bytes exactly as they appear in the certificate, which is what Go hashes.
    """
    offset, _ = _read_header(certificate_der, 0, 0x30)  # Certificate
    offset, _ = _read_header(certificate_der, offset, 0x30)  # tbsCertificate
    if offset < len(certificate_der) and certificate_der[offset] == 0xA0:  # version
        offset = _skip(certificate_der, offset)
    for _ in range(5):  # serialNumber, signature, issuer, validity, subject
        offset = _skip(certificate_der, offset)
    content_offset, length = _read_header(certificate_der, offset, 0x30)
    return certificate_der[offset : content_offset + length]


def spki_sha256_hex(certificate_der: bytes) -> str:
    return hashlib.sha256(subject_public_key_info(certificate_der)).hexdigest()


def contains_distrusted(
    chain: Iterable[bytes], distrusted: FrozenSet[str] = DISTRUSTED_SPKI_SHA256
) -> bool:
    return any(spki_sha256_hex(certificate) in distrusted for certificate in chain)


def _to_der_list(certificates) -> List[bytes]:
    # 3.13+ returns DER bytes; 3.10 to 3.12 return _ssl.Certificate objects.
    encoding_der = getattr(ssl._ssl, "ENCODING_DER", None)
    return [
        c if isinstance(c, bytes) else c.public_bytes(encoding_der)
        for c in certificates
    ]


# Python 3.10 added the ability to read the peer's chain; before that it needs pyOpenSSL.
_NEEDS_PYOPENSSL = sys.version_info < (3, 10)


def _pyopenssl_chain(tls_object) -> Optional[List[bytes]]:
    """The chain of a urllib3 pyOpenSSL-backed socket, as DER bytes."""
    connection = getattr(tls_object, "connection", None)
    get_chain = getattr(connection, "get_peer_cert_chain", None)
    if get_chain is None:
        return None
    chain = get_chain()
    if not chain:
        return None
    from OpenSSL import crypto

    return [crypto.dump_certificate(crypto.FILETYPE_ASN1, c) for c in chain]


def _pyopenssl_context(verify=True):
    """
    A urllib3 pyOpenSSL context, or None if pyOpenSSL isn't installed. It verifies against the same CA bundle
    requests would use.
    """
    try:
        from urllib3.contrib.pyopenssl import PyOpenSSLContext
    except ImportError:
        return None
    context = PyOpenSSLContext(ssl.PROTOCOL_TLS_CLIENT)
    if verify is True:
        import requests.certs

        context.load_verify_locations(cafile=requests.certs.where())
    elif isinstance(verify, str):
        if os.path.isdir(verify):
            context.load_verify_locations(capath=verify)
        else:
            context.load_verify_locations(cafile=verify)
    return context


def peer_chain(tls_object) -> Optional[List[bytes]]:
    """
    The certificate chain of a TLS connection as DER bytes, or None if this Python can't provide it.
    Prefers the chain the TLS library verified, and falls back to the chain the server sent.
    """
    candidates = (tls_object, getattr(tls_object, "_sslobj", None))
    for getter in ("get_verified_chain", "get_unverified_chain"):
        for candidate in candidates:
            method = getattr(candidate, getter, None)
            if method is None:
                continue
            chain = method()
            if chain:
                return _to_der_list(chain)
    return _pyopenssl_chain(tls_object)


def check_connection(
    tls_object, distrusted: FrozenSet[str] = DISTRUSTED_SPKI_SHA256
) -> None:
    """Raise DistrustedIntermediateError if the connection's chain contains a distrusted intermediate."""
    global _warned_unsupported
    chain = peer_chain(tls_object)
    if chain is None:
        if not _warned_unsupported:
            _warned_unsupported = True
            _logger.warning(
                "Cannot read the TLS certificate chain on this connection, so the "
                "distrusted-intermediate check is skipped. Use Python 3.10 or later, or install pyOpenSSL."
            )
        return
    if contains_distrusted(chain, distrusted):
        raise DistrustedIntermediateError(
            "Certificate chain contains a distrusted intermediate certificate"
        )


def _checked_connection_class(distrusted: FrozenSet[str]):
    class CheckedHTTPSConnection(HTTPSConnection):
        def connect(self):
            super().connect()
            try:
                check_connection(self.sock, distrusted)
            except DistrustedIntermediateError:
                self.close()
                raise

    return CheckedHTTPSConnection


def _checked_pool_class(distrusted: FrozenSet[str]):
    class CheckedHTTPSConnectionPool(HTTPSConnectionPool):
        ConnectionCls = _checked_connection_class(distrusted)

    return CheckedHTTPSConnectionPool


class DistrustedIntermediatesAdapter(HTTPAdapter):
    """An HTTPAdapter whose HTTPS connections refuse chains that contain a distrusted intermediate."""

    def __init__(
        self, *args, distrusted: FrozenSet[str] = DISTRUSTED_SPKI_SHA256, **kwargs
    ):
        self._distrusted = distrusted
        super().__init__(*args, **kwargs)

    def init_poolmanager(self, *args, **kwargs):
        if _NEEDS_PYOPENSSL and "ssl_context" not in kwargs:
            context = _pyopenssl_context()
            if context is not None:
                kwargs["ssl_context"] = context
        super().init_poolmanager(*args, **kwargs)
        self._install(self.poolmanager)

    def build_connection_pool_key_attributes(self, request, verify, cert=None):
        # requests 2.32+ passes its own ssl_context per request; swap in the pyOpenSSL one on old Pythons.
        host_params, pool_kwargs = super().build_connection_pool_key_attributes(
            request, verify, cert
        )
        if _NEEDS_PYOPENSSL and verify:
            context = _pyopenssl_context(verify)
            if context is not None:
                pool_kwargs["ssl_context"] = context
        return host_params, pool_kwargs

    def proxy_manager_for(self, *args, **kwargs):
        manager = super().proxy_manager_for(*args, **kwargs)
        self._install(manager)
        return manager

    def _install(self, manager) -> None:
        manager.pool_classes_by_scheme = dict(manager.pool_classes_by_scheme)
        manager.pool_classes_by_scheme["https"] = _checked_pool_class(self._distrusted)


def mount_distrusted_intermediates_check(
    session: Session, adapter: Optional[HTTPAdapter] = None, **adapter_kwargs
) -> Session:
    """
    Make a requests session refuse HTTPS connections whose certificate chain contains a distrusted
    intermediate. Pass adapter_kwargs (for example max_retries) to configure the HTTPAdapter.
    """
    session.mount(
        "https://", adapter or DistrustedIntermediatesAdapter(**adapter_kwargs)
    )
    return session
