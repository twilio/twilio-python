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
from typing import Any, Dict, List, Optional, Union
from twilio.base import deserialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class BundleCopyInstance(InstanceResource):
    class Status(object):
        DRAFT = "draft"
        PENDING_REVIEW = "pending-review"
        IN_REVIEW = "in-review"
        TWILIO_REJECTED = "twilio-rejected"
        TWILIO_APPROVED = "twilio-approved"
        PROVISIONALLY_APPROVED = "provisionally-approved"

    """
    :ivar sid: The unique string that we created to identify the Bundle resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Bundle resource.
    :ivar regulation_sid: The unique string of a regulation that is associated to the Bundle resource.
    :ivar friendly_name: The string that you assigned to describe the resource.
    :ivar status: 
    :ivar valid_until: The date and time in GMT in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format when the resource will be valid until.
    :ivar email: The email address that will receive updates when the Bundle resource changes status.
    :ivar status_callback: The URL we call to inform your application of status changes.
    :ivar date_created: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    """

    def __init__(self, version: Version, payload: Dict[str, Any], bundle_sid: str):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.regulation_sid: Optional[str] = payload.get("regulation_sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.status: Optional["BundleCopyInstance.Status"] = payload.get("status")
        self.valid_until: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("valid_until")
        )
        self.email: Optional[str] = payload.get("email")
        self.status_callback: Optional[str] = payload.get("status_callback")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )

        self._solution = {
            "bundle_sid": bundle_sid,
        }

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Numbers.V2.BundleCopyInstance {}>".format(context)


class BundleCopyPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> BundleCopyInstance:
        """
        Build an instance of BundleCopyInstance

        :param payload: Payload response from the API
        """
        return BundleCopyInstance(
            self._version, payload, bundle_sid=self._solution["bundle_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Numbers.V2.BundleCopyPage>"


class BundleCopyList(ListResource):
    def __init__(self, version: Version, bundle_sid: str):
        """
        Initialize the BundleCopyList

        :param version: Version that contains the resource
        :param bundle_sid: The unique string that we created to identify the Bundle resource.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "bundle_sid": bundle_sid,
        }
        self._uri = "/RegulatoryCompliance/Bundles/{bundle_sid}/Copies".format(
            **self._solution
        )

    def create(
        self, friendly_name: Union[str, object] = values.unset
    ) -> BundleCopyInstance:
        """
        Create the BundleCopyInstance

        :param friendly_name: The string that you assigned to describe the copied bundle.

        :returns: The created BundleCopyInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return BundleCopyInstance(
            self._version, payload, bundle_sid=self._solution["bundle_sid"]
        )

    async def create_async(
        self, friendly_name: Union[str, object] = values.unset
    ) -> BundleCopyInstance:
        """
        Asynchronously create the BundleCopyInstance

        :param friendly_name: The string that you assigned to describe the copied bundle.

        :returns: The created BundleCopyInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return BundleCopyInstance(
            self._version, payload, bundle_sid=self._solution["bundle_sid"]
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[BundleCopyInstance]:
        """
        Streams BundleCopyInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[BundleCopyInstance]:
        """
        Asynchronously streams BundleCopyInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[BundleCopyInstance]:
        """
        Lists BundleCopyInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
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

    async def list_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[BundleCopyInstance]:
        """
        Asynchronously lists BundleCopyInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
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
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> BundleCopyPage:
        """
        Retrieve a single page of BundleCopyInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of BundleCopyInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return BundleCopyPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> BundleCopyPage:
        """
        Asynchronously retrieve a single page of BundleCopyInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of BundleCopyInstance
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
        return BundleCopyPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> BundleCopyPage:
        """
        Retrieve a specific page of BundleCopyInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of BundleCopyInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return BundleCopyPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> BundleCopyPage:
        """
        Asynchronously retrieve a specific page of BundleCopyInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of BundleCopyInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return BundleCopyPage(self._version, response, self._solution)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Numbers.V2.BundleCopyList>"
