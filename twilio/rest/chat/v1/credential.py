r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Chat
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Any, Dict, List, Optional
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class CredentialInstance(InstanceResource):
    class PushService(object):
        GCM = "gcm"
        APN = "apn"
        FCM = "fcm"

    """
    :ivar sid: The unique string that we created to identify the Credential resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/api/rest/account) that created the Credential resource.
    :ivar friendly_name: The string that you assigned to describe the resource.
    :ivar type: 
    :ivar sandbox: [APN only] Whether to send the credential to sandbox APNs. Can be `true` to send to sandbox APNs or `false` to send to production.
    :ivar date_created: The date and time in GMT when the resource was created specified in [RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar url: The absolute URL of the Credential resource.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.type: Optional["CredentialInstance.PushService"] = payload.get("type")
        self.sandbox: Optional[str] = payload.get("sandbox")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[CredentialContext] = None

    @property
    def _proxy(self) -> "CredentialContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: CredentialContext for this CredentialInstance
        """
        if self._context is None:
            self._context = CredentialContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the CredentialInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the CredentialInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "CredentialInstance":
        """
        Fetch the CredentialInstance


        :returns: The fetched CredentialInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "CredentialInstance":
        """
        Asynchronous coroutine to fetch the CredentialInstance


        :returns: The fetched CredentialInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        friendly_name=values.unset,
        certificate=values.unset,
        private_key=values.unset,
        sandbox=values.unset,
        api_key=values.unset,
        secret=values.unset,
    ) -> "CredentialInstance":
        """
        Update the CredentialInstance

        :param str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param str certificate: [APN only] The URL encoded representation of the certificate. For example,  `-----BEGIN CERTIFICATE----- MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEFBQAwgZYxCzAJBgNV.....A== -----END CERTIFICATE-----`
        :param str private_key: [APN only] The URL encoded representation of the private key. For example, `-----BEGIN RSA PRIVATE KEY----- MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fGgvCI1l9s+cmBY3WIz+cUDqmxiieR. -----END RSA PRIVATE KEY-----`
        :param bool sandbox: [APN only] Whether to send the credential to sandbox APNs. Can be `true` to send to sandbox APNs or `false` to send to production.
        :param str api_key: [GCM only] The API key for the project that was obtained from the Google Developer console for your GCM Service application credential.
        :param str secret: [FCM only] The **Server key** of your project from the Firebase console, found under Settings / Cloud messaging.

        :returns: The updated CredentialInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            certificate=certificate,
            private_key=private_key,
            sandbox=sandbox,
            api_key=api_key,
            secret=secret,
        )

    async def update_async(
        self,
        friendly_name=values.unset,
        certificate=values.unset,
        private_key=values.unset,
        sandbox=values.unset,
        api_key=values.unset,
        secret=values.unset,
    ) -> "CredentialInstance":
        """
        Asynchronous coroutine to update the CredentialInstance

        :param str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param str certificate: [APN only] The URL encoded representation of the certificate. For example,  `-----BEGIN CERTIFICATE----- MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEFBQAwgZYxCzAJBgNV.....A== -----END CERTIFICATE-----`
        :param str private_key: [APN only] The URL encoded representation of the private key. For example, `-----BEGIN RSA PRIVATE KEY----- MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fGgvCI1l9s+cmBY3WIz+cUDqmxiieR. -----END RSA PRIVATE KEY-----`
        :param bool sandbox: [APN only] Whether to send the credential to sandbox APNs. Can be `true` to send to sandbox APNs or `false` to send to production.
        :param str api_key: [GCM only] The API key for the project that was obtained from the Google Developer console for your GCM Service application credential.
        :param str secret: [FCM only] The **Server key** of your project from the Firebase console, found under Settings / Cloud messaging.

        :returns: The updated CredentialInstance
        """
        return await self._proxy.update_async(
            friendly_name=friendly_name,
            certificate=certificate,
            private_key=private_key,
            sandbox=sandbox,
            api_key=api_key,
            secret=secret,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Chat.V1.CredentialInstance {}>".format(context)


class CredentialContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the CredentialContext

        :param version: Version that contains the resource
        :param sid: The Twilio-provided string that uniquely identifies the Credential resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Credentials/{sid}".format(**self._solution)

    def delete(self) -> bool:
        """
        Deletes the CredentialInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the CredentialInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> CredentialInstance:
        """
        Fetch the CredentialInstance


        :returns: The fetched CredentialInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return CredentialInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> CredentialInstance:
        """
        Asynchronous coroutine to fetch the CredentialInstance


        :returns: The fetched CredentialInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return CredentialInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(
        self,
        friendly_name=values.unset,
        certificate=values.unset,
        private_key=values.unset,
        sandbox=values.unset,
        api_key=values.unset,
        secret=values.unset,
    ) -> CredentialInstance:
        """
        Update the CredentialInstance

        :param str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param str certificate: [APN only] The URL encoded representation of the certificate. For example,  `-----BEGIN CERTIFICATE----- MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEFBQAwgZYxCzAJBgNV.....A== -----END CERTIFICATE-----`
        :param str private_key: [APN only] The URL encoded representation of the private key. For example, `-----BEGIN RSA PRIVATE KEY----- MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fGgvCI1l9s+cmBY3WIz+cUDqmxiieR. -----END RSA PRIVATE KEY-----`
        :param bool sandbox: [APN only] Whether to send the credential to sandbox APNs. Can be `true` to send to sandbox APNs or `false` to send to production.
        :param str api_key: [GCM only] The API key for the project that was obtained from the Google Developer console for your GCM Service application credential.
        :param str secret: [FCM only] The **Server key** of your project from the Firebase console, found under Settings / Cloud messaging.

        :returns: The updated CredentialInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "Certificate": certificate,
                "PrivateKey": private_key,
                "Sandbox": sandbox,
                "ApiKey": api_key,
                "Secret": secret,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return CredentialInstance(self._version, payload, sid=self._solution["sid"])

    async def update_async(
        self,
        friendly_name=values.unset,
        certificate=values.unset,
        private_key=values.unset,
        sandbox=values.unset,
        api_key=values.unset,
        secret=values.unset,
    ) -> CredentialInstance:
        """
        Asynchronous coroutine to update the CredentialInstance

        :param str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param str certificate: [APN only] The URL encoded representation of the certificate. For example,  `-----BEGIN CERTIFICATE----- MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEFBQAwgZYxCzAJBgNV.....A== -----END CERTIFICATE-----`
        :param str private_key: [APN only] The URL encoded representation of the private key. For example, `-----BEGIN RSA PRIVATE KEY----- MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fGgvCI1l9s+cmBY3WIz+cUDqmxiieR. -----END RSA PRIVATE KEY-----`
        :param bool sandbox: [APN only] Whether to send the credential to sandbox APNs. Can be `true` to send to sandbox APNs or `false` to send to production.
        :param str api_key: [GCM only] The API key for the project that was obtained from the Google Developer console for your GCM Service application credential.
        :param str secret: [FCM only] The **Server key** of your project from the Firebase console, found under Settings / Cloud messaging.

        :returns: The updated CredentialInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "Certificate": certificate,
                "PrivateKey": private_key,
                "Sandbox": sandbox,
                "ApiKey": api_key,
                "Secret": secret,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return CredentialInstance(self._version, payload, sid=self._solution["sid"])

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Chat.V1.CredentialContext {}>".format(context)


class CredentialPage(Page):
    def get_instance(self, payload) -> CredentialInstance:
        """
        Build an instance of CredentialInstance

        :param dict payload: Payload response from the API
        """
        return CredentialInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Chat.V1.CredentialPage>"


class CredentialList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the CredentialList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Credentials"

    def create(
        self,
        type,
        friendly_name=values.unset,
        certificate=values.unset,
        private_key=values.unset,
        sandbox=values.unset,
        api_key=values.unset,
        secret=values.unset,
    ) -> CredentialInstance:
        """
        Create the CredentialInstance

        :param &quot;CredentialInstance.PushService&quot; type:
        :param str friendly_name: A descriptive string that you create to describe the new resource. It can be up to 64 characters long.
        :param str certificate: [APN only] The URL encoded representation of the certificate. For example,  `-----BEGIN CERTIFICATE----- MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEFBQAwgZYxCzAJBgNV.....A== -----END CERTIFICATE-----`
        :param str private_key: [APN only] The URL encoded representation of the private key. For example, `-----BEGIN RSA PRIVATE KEY----- MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fGgvCI1l9s+cmBY3WIz+cUDqmxiieR. -----END RSA PRIVATE KEY-----`
        :param bool sandbox: [APN only] Whether to send the credential to sandbox APNs. Can be `true` to send to sandbox APNs or `false` to send to production.
        :param str api_key: [GCM only] The API key for the project that was obtained from the Google Developer console for your GCM Service application credential.
        :param str secret: [FCM only] The **Server key** of your project from the Firebase console, found under Settings / Cloud messaging.

        :returns: The created CredentialInstance
        """
        data = values.of(
            {
                "Type": type,
                "FriendlyName": friendly_name,
                "Certificate": certificate,
                "PrivateKey": private_key,
                "Sandbox": sandbox,
                "ApiKey": api_key,
                "Secret": secret,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return CredentialInstance(self._version, payload)

    async def create_async(
        self,
        type,
        friendly_name=values.unset,
        certificate=values.unset,
        private_key=values.unset,
        sandbox=values.unset,
        api_key=values.unset,
        secret=values.unset,
    ) -> CredentialInstance:
        """
        Asynchronously create the CredentialInstance

        :param &quot;CredentialInstance.PushService&quot; type:
        :param str friendly_name: A descriptive string that you create to describe the new resource. It can be up to 64 characters long.
        :param str certificate: [APN only] The URL encoded representation of the certificate. For example,  `-----BEGIN CERTIFICATE----- MIIFnTCCBIWgAwIBAgIIAjy9H849+E8wDQYJKoZIhvcNAQEFBQAwgZYxCzAJBgNV.....A== -----END CERTIFICATE-----`
        :param str private_key: [APN only] The URL encoded representation of the private key. For example, `-----BEGIN RSA PRIVATE KEY----- MIIEpQIBAAKCAQEAuyf/lNrH9ck8DmNyo3fGgvCI1l9s+cmBY3WIz+cUDqmxiieR. -----END RSA PRIVATE KEY-----`
        :param bool sandbox: [APN only] Whether to send the credential to sandbox APNs. Can be `true` to send to sandbox APNs or `false` to send to production.
        :param str api_key: [GCM only] The API key for the project that was obtained from the Google Developer console for your GCM Service application credential.
        :param str secret: [FCM only] The **Server key** of your project from the Firebase console, found under Settings / Cloud messaging.

        :returns: The created CredentialInstance
        """
        data = values.of(
            {
                "Type": type,
                "FriendlyName": friendly_name,
                "Certificate": certificate,
                "PrivateKey": private_key,
                "Sandbox": sandbox,
                "ApiKey": api_key,
                "Secret": secret,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return CredentialInstance(self._version, payload)

    def stream(self, limit=None, page_size=None) -> List[CredentialInstance]:
        """
        Streams CredentialInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self, limit=None, page_size=None
    ) -> List[CredentialInstance]:
        """
        Asynchronously streams CredentialInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(self, limit=None, page_size=None) -> List[CredentialInstance]:
        """
        Lists CredentialInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(self, limit=None, page_size=None) -> List[CredentialInstance]:
        """
        Asynchronously lists CredentialInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        return list(
            await self.stream_async(
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ) -> CredentialPage:
        """
        Retrieve a single page of CredentialInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CredentialInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return CredentialPage(self._version, response)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ) -> CredentialPage:
        """
        Asynchronously retrieve a single page of CredentialInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CredentialInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return CredentialPage(self._version, response)

    def get_page(self, target_url) -> CredentialPage:
        """
        Retrieve a specific page of CredentialInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CredentialInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return CredentialPage(self._version, response)

    async def get_page_async(self, target_url) -> CredentialPage:
        """
        Asynchronously retrieve a specific page of CredentialInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CredentialInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return CredentialPage(self._version, response)

    def get(self, sid) -> CredentialContext:
        """
        Constructs a CredentialContext

        :param sid: The Twilio-provided string that uniquely identifies the Credential resource to update.
        """
        return CredentialContext(self._version, sid=sid)

    def __call__(self, sid) -> CredentialContext:
        """
        Constructs a CredentialContext

        :param sid: The Twilio-provided string that uniquely identifies the Credential resource to update.
        """
        return CredentialContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Chat.V1.CredentialList>"
