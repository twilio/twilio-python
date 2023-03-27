r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Numbers
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Any, Dict, List, Optional
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class EndUserInstance(InstanceResource):
    class Type(object):
        INDIVIDUAL = "individual"
        BUSINESS = "business"

    """
    :ivar sid: The unique string created by Twilio to identify the End User resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the End User resource.
    :ivar friendly_name: The string that you assigned to describe the resource.
    :ivar type: 
    :ivar attributes: The set of parameters that are the attributes of the End Users resource which are listed in the End User Types.
    :ivar date_created: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar url: The absolute URL of the End User resource.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.type: Optional["EndUserInstance.Type"] = payload.get("type")
        self.attributes: Optional[Dict[str, object]] = payload.get("attributes")
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
        self._context: Optional[EndUserContext] = None

    @property
    def _proxy(self) -> "EndUserContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: EndUserContext for this EndUserInstance
        """
        if self._context is None:
            self._context = EndUserContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the EndUserInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the EndUserInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "EndUserInstance":
        """
        Fetch the EndUserInstance


        :returns: The fetched EndUserInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "EndUserInstance":
        """
        Asynchronous coroutine to fetch the EndUserInstance


        :returns: The fetched EndUserInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self, friendly_name=values.unset, attributes=values.unset
    ) -> "EndUserInstance":
        """
        Update the EndUserInstance

        :param str friendly_name: The string that you assigned to describe the resource.
        :param object attributes: The set of parameters that are the attributes of the End User resource which are derived End User Types.

        :returns: The updated EndUserInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            attributes=attributes,
        )

    async def update_async(
        self, friendly_name=values.unset, attributes=values.unset
    ) -> "EndUserInstance":
        """
        Asynchronous coroutine to update the EndUserInstance

        :param str friendly_name: The string that you assigned to describe the resource.
        :param object attributes: The set of parameters that are the attributes of the End User resource which are derived End User Types.

        :returns: The updated EndUserInstance
        """
        return await self._proxy.update_async(
            friendly_name=friendly_name,
            attributes=attributes,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Numbers.V2.EndUserInstance {}>".format(context)


class EndUserContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the EndUserContext

        :param version: Version that contains the resource
        :param sid: The unique string created by Twilio to identify the End User resource.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/RegulatoryCompliance/EndUsers/{sid}".format(**self._solution)

    def delete(self) -> bool:
        """
        Deletes the EndUserInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the EndUserInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> EndUserInstance:
        """
        Fetch the EndUserInstance


        :returns: The fetched EndUserInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return EndUserInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> EndUserInstance:
        """
        Asynchronous coroutine to fetch the EndUserInstance


        :returns: The fetched EndUserInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return EndUserInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(
        self, friendly_name=values.unset, attributes=values.unset
    ) -> EndUserInstance:
        """
        Update the EndUserInstance

        :param str friendly_name: The string that you assigned to describe the resource.
        :param object attributes: The set of parameters that are the attributes of the End User resource which are derived End User Types.

        :returns: The updated EndUserInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "Attributes": serialize.object(attributes),
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return EndUserInstance(self._version, payload, sid=self._solution["sid"])

    async def update_async(
        self, friendly_name=values.unset, attributes=values.unset
    ) -> EndUserInstance:
        """
        Asynchronous coroutine to update the EndUserInstance

        :param str friendly_name: The string that you assigned to describe the resource.
        :param object attributes: The set of parameters that are the attributes of the End User resource which are derived End User Types.

        :returns: The updated EndUserInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "Attributes": serialize.object(attributes),
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return EndUserInstance(self._version, payload, sid=self._solution["sid"])

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Numbers.V2.EndUserContext {}>".format(context)


class EndUserPage(Page):
    def get_instance(self, payload) -> EndUserInstance:
        """
        Build an instance of EndUserInstance

        :param dict payload: Payload response from the API
        """
        return EndUserInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Numbers.V2.EndUserPage>"


class EndUserList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the EndUserList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/RegulatoryCompliance/EndUsers"

    def create(self, friendly_name, type, attributes=values.unset) -> EndUserInstance:
        """
        Create the EndUserInstance

        :param str friendly_name: The string that you assigned to describe the resource.
        :param &quot;EndUserInstance.Type&quot; type:
        :param object attributes: The set of parameters that are the attributes of the End User resource which are derived End User Types.

        :returns: The created EndUserInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "Type": type,
                "Attributes": serialize.object(attributes),
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return EndUserInstance(self._version, payload)

    async def create_async(
        self, friendly_name, type, attributes=values.unset
    ) -> EndUserInstance:
        """
        Asynchronously create the EndUserInstance

        :param str friendly_name: The string that you assigned to describe the resource.
        :param &quot;EndUserInstance.Type&quot; type:
        :param object attributes: The set of parameters that are the attributes of the End User resource which are derived End User Types.

        :returns: The created EndUserInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "Type": type,
                "Attributes": serialize.object(attributes),
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return EndUserInstance(self._version, payload)

    def stream(self, limit=None, page_size=None) -> List[EndUserInstance]:
        """
        Streams EndUserInstance records from the API as a generator stream.
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

    async def stream_async(self, limit=None, page_size=None) -> List[EndUserInstance]:
        """
        Asynchronously streams EndUserInstance records from the API as a generator stream.
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

    def list(self, limit=None, page_size=None) -> List[EndUserInstance]:
        """
        Lists EndUserInstance records from the API as a list.
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

    async def list_async(self, limit=None, page_size=None) -> List[EndUserInstance]:
        """
        Asynchronously lists EndUserInstance records from the API as a list.
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
    ) -> EndUserPage:
        """
        Retrieve a single page of EndUserInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of EndUserInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return EndUserPage(self._version, response)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ) -> EndUserPage:
        """
        Asynchronously retrieve a single page of EndUserInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of EndUserInstance
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
        return EndUserPage(self._version, response)

    def get_page(self, target_url) -> EndUserPage:
        """
        Retrieve a specific page of EndUserInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of EndUserInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return EndUserPage(self._version, response)

    async def get_page_async(self, target_url) -> EndUserPage:
        """
        Asynchronously retrieve a specific page of EndUserInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of EndUserInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return EndUserPage(self._version, response)

    def get(self, sid) -> EndUserContext:
        """
        Constructs a EndUserContext

        :param sid: The unique string created by Twilio to identify the End User resource.
        """
        return EndUserContext(self._version, sid=sid)

    def __call__(self, sid) -> EndUserContext:
        """
        Constructs a EndUserContext

        :param sid: The unique string created by Twilio to identify the End User resource.
        """
        return EndUserContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Numbers.V2.EndUserList>"
