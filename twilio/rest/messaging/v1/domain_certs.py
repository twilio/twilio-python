r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Messaging
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Optional
from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class DomainCertsList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the DomainCertsList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.messaging.v1.domain_certs.DomainCertsList
        :rtype: twilio.rest.messaging.v1.domain_certs.DomainCertsList
        """
        super().__init__(version)

    def get(self, domain_sid):
        """
        Constructs a DomainCertsContext

        :param domain_sid: Unique string used to identify the domain that this certificate should be associated with.

        :returns: twilio.rest.messaging.v1.domain_certs.DomainCertsContext
        :rtype: twilio.rest.messaging.v1.domain_certs.DomainCertsContext
        """
        return DomainCertsContext(self._version, domain_sid=domain_sid)

    def __call__(self, domain_sid):
        """
        Constructs a DomainCertsContext

        :param domain_sid: Unique string used to identify the domain that this certificate should be associated with.

        :returns: twilio.rest.messaging.v1.domain_certs.DomainCertsContext
        :rtype: twilio.rest.messaging.v1.domain_certs.DomainCertsContext
        """
        return DomainCertsContext(self._version, domain_sid=domain_sid)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Messaging.V1.DomainCertsList>"


class DomainCertsInstance(InstanceResource):
    def __init__(self, version, payload, domain_sid: Optional[str] = None):
        """
        Initialize the DomainCertsInstance

        :returns: twilio.rest.messaging.v1.domain_certs.DomainCertsInstance
        :rtype: twilio.rest.messaging.v1.domain_certs.DomainCertsInstance
        """
        super().__init__(version)

        self._properties = {
            "domain_sid": payload.get("domain_sid"),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "date_expires": deserialize.iso8601_datetime(payload.get("date_expires")),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "domain_name": payload.get("domain_name"),
            "certificate_sid": payload.get("certificate_sid"),
            "url": payload.get("url"),
            "validated": payload.get("validated"),
        }

        self._solution = {
            "domain_sid": domain_sid or self._properties["domain_sid"],
        }
        self._context: Optional[DomainCertsContext] = None

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: DomainCertsContext for this DomainCertsInstance
        :rtype: twilio.rest.messaging.v1.domain_certs.DomainCertsContext
        """
        if self._context is None:
            self._context = DomainCertsContext(
                self._version,
                domain_sid=self._solution["domain_sid"],
            )
        return self._context

    @property
    def domain_sid(self):
        """
        :returns: The unique string that we created to identify the Domain resource.
        :rtype: str
        """
        return self._properties["domain_sid"]

    @property
    def date_updated(self):
        """
        :returns: Date that this Domain was last updated.
        :rtype: datetime
        """
        return self._properties["date_updated"]

    @property
    def date_expires(self):
        """
        :returns: Date that the private certificate associated with this domain expires. You will need to update the certificate before that date to ensure your shortened links will continue to work.
        :rtype: datetime
        """
        return self._properties["date_expires"]

    @property
    def date_created(self):
        """
        :returns: Date that this Domain was registered to the Twilio platform to create a new Domain object.
        :rtype: datetime
        """
        return self._properties["date_created"]

    @property
    def domain_name(self):
        """
        :returns: Full url path for this domain.
        :rtype: str
        """
        return self._properties["domain_name"]

    @property
    def certificate_sid(self):
        """
        :returns: The unique string that we created to identify this Certificate resource.
        :rtype: str
        """
        return self._properties["certificate_sid"]

    @property
    def url(self):
        """
        :returns:
        :rtype: str
        """
        return self._properties["url"]

    @property
    def validated(self):
        """
        :returns: Boolean value indicating whether certificate has been validated
        :rtype: bool
        """
        return self._properties["validated"]

    def delete(self):
        """
        Deletes the DomainCertsInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the DomainCertsInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._proxy.delete_async()

    def fetch(self):
        """
        Fetch the DomainCertsInstance


        :returns: The fetched DomainCertsInstance
        :rtype: twilio.rest.messaging.v1.domain_certs.DomainCertsInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the DomainCertsInstance


        :returns: The fetched DomainCertsInstance
        :rtype: twilio.rest.messaging.v1.domain_certs.DomainCertsInstance
        """
        return await self._proxy.fetch_async()

    def update(self, tls_cert):
        """
        Update the DomainCertsInstance

        :param str tls_cert: Contains the full TLS certificate and private for this domain in PEM format: https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail. Twilio uses this information to process HTTPS traffic sent to your domain.

        :returns: The updated DomainCertsInstance
        :rtype: twilio.rest.messaging.v1.domain_certs.DomainCertsInstance
        """
        return self._proxy.update(
            tls_cert=tls_cert,
        )

    async def update_async(self, tls_cert):
        """
        Asynchronous coroutine to update the DomainCertsInstance

        :param str tls_cert: Contains the full TLS certificate and private for this domain in PEM format: https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail. Twilio uses this information to process HTTPS traffic sent to your domain.

        :returns: The updated DomainCertsInstance
        :rtype: twilio.rest.messaging.v1.domain_certs.DomainCertsInstance
        """
        return await self._proxy.update_async(
            tls_cert=tls_cert,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Messaging.V1.DomainCertsInstance {}>".format(context)


class DomainCertsContext(InstanceContext):
    def __init__(self, version: Version, domain_sid: str):
        """
        Initialize the DomainCertsContext

        :param Version version: Version that contains the resource
        :param domain_sid: Unique string used to identify the domain that this certificate should be associated with.

        :returns: twilio.rest.messaging.v1.domain_certs.DomainCertsContext
        :rtype: twilio.rest.messaging.v1.domain_certs.DomainCertsContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "domain_sid": domain_sid,
        }
        self._uri = "/LinkShortening/Domains/{domain_sid}/Certificate".format(
            **self._solution
        )

    def delete(self):
        """
        Deletes the DomainCertsInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the DomainCertsInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self):
        """
        Fetch the DomainCertsInstance


        :returns: The fetched DomainCertsInstance
        :rtype: twilio.rest.messaging.v1.domain_certs.DomainCertsInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return DomainCertsInstance(
            self._version,
            payload,
            domain_sid=self._solution["domain_sid"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the DomainCertsInstance


        :returns: The fetched DomainCertsInstance
        :rtype: twilio.rest.messaging.v1.domain_certs.DomainCertsInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return DomainCertsInstance(
            self._version,
            payload,
            domain_sid=self._solution["domain_sid"],
        )

    def update(self, tls_cert):
        """
        Update the DomainCertsInstance

        :param str tls_cert: Contains the full TLS certificate and private for this domain in PEM format: https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail. Twilio uses this information to process HTTPS traffic sent to your domain.

        :returns: The updated DomainCertsInstance
        :rtype: twilio.rest.messaging.v1.domain_certs.DomainCertsInstance
        """
        data = values.of(
            {
                "TlsCert": tls_cert,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return DomainCertsInstance(
            self._version, payload, domain_sid=self._solution["domain_sid"]
        )

    async def update_async(self, tls_cert):
        """
        Asynchronous coroutine to update the DomainCertsInstance

        :param str tls_cert: Contains the full TLS certificate and private for this domain in PEM format: https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail. Twilio uses this information to process HTTPS traffic sent to your domain.

        :returns: The updated DomainCertsInstance
        :rtype: twilio.rest.messaging.v1.domain_certs.DomainCertsInstance
        """
        data = values.of(
            {
                "TlsCert": tls_cert,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return DomainCertsInstance(
            self._version, payload, domain_sid=self._solution["domain_sid"]
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Messaging.V1.DomainCertsContext {}>".format(context)
