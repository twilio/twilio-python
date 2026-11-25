import datetime
import http.server
import logging
import os
import ssl
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch

import requests
from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.x509.oid import NameOID

from twilio.http import distrusted_intermediates as di
from twilio.http.http_client import TwilioHttpClient
from twilio.http.validation_client import ValidationClient


def _name(common_name):
    return x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, common_name)])


def _issue(subject, subject_key, issuer, issuer_key, ca, san=None):
    now = datetime.datetime.now(datetime.timezone.utc)
    builder = (
        x509.CertificateBuilder()
        .subject_name(_name(subject))
        .issuer_name(_name(issuer))
        .public_key(subject_key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(now - datetime.timedelta(minutes=5))
        .not_valid_after(now + datetime.timedelta(days=1))
        .add_extension(x509.BasicConstraints(ca=ca, path_length=None), critical=True)
        .add_extension(
            x509.KeyUsage(
                digital_signature=not ca,
                content_commitment=False,
                key_encipherment=False,
                data_encipherment=False,
                key_agreement=False,
                key_cert_sign=ca,
                crl_sign=ca,
                encipher_only=False,
                decipher_only=False,
            ),
            critical=True,
        )
        .add_extension(
            x509.SubjectKeyIdentifier.from_public_key(subject_key.public_key()),
            critical=False,
        )
        .add_extension(
            x509.AuthorityKeyIdentifier.from_issuer_public_key(issuer_key.public_key()),
            critical=False,
        )
    )
    if san:
        builder = builder.add_extension(
            x509.SubjectAlternativeName([x509.DNSName(san)]), critical=False
        )
    return builder.sign(issuer_key, hashes.SHA256())


def _pem(cert):
    return cert.public_bytes(serialization.Encoding.PEM)


def _spki_sha256(cert):
    spki = cert.public_key().public_bytes(
        serialization.Encoding.DER, serialization.PublicFormat.SubjectPublicKeyInfo
    )
    digest = hashes.Hash(hashes.SHA256())
    digest.update(spki)
    return digest.finalize().hex()


class _Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Length", "2")
        self.end_headers()
        self.wfile.write(b"ok")

    def log_message(self, *args):
        pass


class _Pki:
    """A root, an intermediate and a localhost leaf, served over TLS on a local port."""

    def __init__(self):
        root_key, inter_key, leaf_key = (
            ec.generate_private_key(ec.SECP256R1()) for _ in range(3)
        )
        self.root = _issue("Test Root", root_key, "Test Root", root_key, ca=True)
        self.intermediate = _issue(
            "Test Intermediate", inter_key, "Test Root", root_key, ca=True
        )
        self.leaf = _issue(
            "localhost",
            leaf_key,
            "Test Intermediate",
            inter_key,
            ca=False,
            san="localhost",
        )
        self.directory = tempfile.TemporaryDirectory()
        self.ca_path = os.path.join(self.directory.name, "root.pem")
        chain_path = os.path.join(self.directory.name, "chain.pem")
        key_path = os.path.join(self.directory.name, "leaf.key")
        with open(self.ca_path, "wb") as f:
            f.write(_pem(self.root))
        with open(chain_path, "wb") as f:
            f.write(_pem(self.leaf) + _pem(self.intermediate))
        with open(key_path, "wb") as f:
            f.write(
                leaf_key.private_bytes(
                    serialization.Encoding.PEM,
                    serialization.PrivateFormat.PKCS8,
                    serialization.NoEncryption(),
                )
            )
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(chain_path, key_path)
        self.server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), _Handler)
        self.server.daemon_threads = True
        self.server.socket = context.wrap_socket(self.server.socket, server_side=True)
        self.url = "https://localhost:%d/" % self.server.server_address[1]
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()

    def close(self):
        self.server.shutdown()
        self.server.server_close()
        self.directory.cleanup()


def _can_read_chain():
    if sys.version_info >= (3, 10):
        return True
    try:
        import OpenSSL  # noqa: F401
    except ImportError:
        return False
    return True


@unittest.skipUnless(
    _can_read_chain(), "needs Python 3.10+ or pyOpenSSL to read the TLS chain"
)
class TestDistrustedIntermediatesConnection(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pki = _Pki()

    @classmethod
    def tearDownClass(cls):
        cls.pki.close()

    def _session(self, distrusted):
        session = requests.Session()
        session.verify = self.pki.ca_path
        di.mount_distrusted_intermediates_check(session, distrusted=distrusted)
        return session

    def test_allows_a_chain_without_a_distrusted_intermediate(self):
        response = self._session(di.DISTRUSTED_SPKI_SHA256).get(self.pki.url)
        self.assertEqual(response.status_code, 200)

    def test_refuses_a_chain_with_a_distrusted_intermediate(self):
        distrusted = frozenset({_spki_sha256(self.pki.intermediate)})
        with self.assertRaises(requests.exceptions.SSLError) as context:
            self._session(distrusted).get(self.pki.url)
        self.assertIn("distrusted intermediate", str(context.exception))

    def test_refuses_a_distrusted_certificate_anywhere_in_the_chain(self):
        distrusted = frozenset({_spki_sha256(self.pki.root)})
        if sys.version_info < (3, 10):
            # pyOpenSSL only exposes the chain the server sent, and servers don't send the root.
            response = self._session(distrusted).get(self.pki.url)
            self.assertEqual(response.status_code, 200)
            return
        with self.assertRaises(requests.exceptions.SSLError):
            self._session(distrusted).get(self.pki.url)

    def test_still_refuses_a_trusted_chain_issued_for_another_host(self):
        session = self._session(di.DISTRUSTED_SPKI_SHA256)
        with self.assertRaises(requests.exceptions.SSLError):
            session.get(self.pki.url.replace("localhost", "127.0.0.1"))

    def test_refuses_on_every_request_not_just_the_first(self):
        distrusted = frozenset({_spki_sha256(self.pki.intermediate)})
        session = self._session(distrusted)
        for _ in range(2):
            with self.assertRaises(requests.exceptions.SSLError):
                session.get(self.pki.url)


class TestSpkiHash(unittest.TestCase):
    def test_matches_the_hash_cryptography_computes(self):
        pki = _Pki()
        try:
            for cert in (pki.root, pki.intermediate, pki.leaf):
                der = cert.public_bytes(serialization.Encoding.DER)
                self.assertEqual(di.spki_sha256_hex(der), _spki_sha256(cert))
        finally:
            pki.close()

    def test_contains_distrusted(self):
        pki = _Pki()
        try:
            chain = [
                c.public_bytes(serialization.Encoding.DER)
                for c in (pki.leaf, pki.intermediate)
            ]
            self.assertFalse(di.contains_distrusted(chain))
            self.assertTrue(
                di.contains_distrusted(
                    chain, frozenset({_spki_sha256(pki.intermediate)})
                )
            )
        finally:
            pki.close()

    def test_list_has_the_eight_go_hashes(self):
        self.assertEqual(len(di.DISTRUSTED_SPKI_SHA256), 8)
        for value in di.DISTRUSTED_SPKI_SHA256:
            self.assertEqual(len(value), 64)

    def test_rejects_truncated_der(self):
        with self.assertRaises(ValueError):
            di.subject_public_key_info(b"\x30\x82\x01")


class TestUnsupportedPython(unittest.TestCase):
    def test_warns_once_and_allows_when_chain_is_unreadable(self):
        di._warned_unsupported = False
        with patch.object(di, "peer_chain", return_value=None):
            with self.assertLogs("twilio.http_client", level=logging.WARNING) as logs:
                di.check_connection(object())
                di.check_connection(object())
        self.assertEqual(len(logs.records), 1)
        self.assertIn("distrusted-intermediate check is skipped", logs.output[0])


class TestDefaultClientsApplyTheCheck(unittest.TestCase):
    def test_twilio_http_client_uses_the_checking_adapter(self):
        client = TwilioHttpClient()
        self.assertIsInstance(
            client.session.get_adapter("https://api.twilio.com"),
            di.DistrustedIntermediatesAdapter,
        )

    def test_twilio_http_client_with_retries_uses_the_checking_adapter(self):
        client = TwilioHttpClient(max_retries=2)
        self.assertIsInstance(
            client.session.get_adapter("https://api.twilio.com"),
            di.DistrustedIntermediatesAdapter,
        )

    def test_validation_client_uses_the_checking_adapter(self):
        client = ValidationClient("AC123", "SK123", "CR123", "private-key")
        self.assertIsInstance(
            client.session.get_adapter("https://api.twilio.com"),
            di.DistrustedIntermediatesAdapter,
        )
