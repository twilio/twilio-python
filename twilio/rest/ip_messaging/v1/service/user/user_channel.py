r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Ip_messaging
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Any, Dict, List, Optional
from twilio.base import deserialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class UserChannelInstance(InstanceResource):
    class ChannelStatus(object):
        JOINED = "joined"
        INVITED = "invited"
        NOT_PARTICIPATING = "not_participating"

    """
    :ivar account_sid: 
    :ivar service_sid: 
    :ivar channel_sid: 
    :ivar member_sid: 
    :ivar status: 
    :ivar last_consumed_message_index: 
    :ivar unread_messages_count: 
    :ivar links: 
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], service_sid: str, user_sid: str
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.channel_sid: Optional[str] = payload.get("channel_sid")
        self.member_sid: Optional[str] = payload.get("member_sid")
        self.status: Optional["UserChannelInstance.ChannelStatus"] = payload.get(
            "status"
        )
        self.last_consumed_message_index: Optional[int] = deserialize.integer(
            payload.get("last_consumed_message_index")
        )
        self.unread_messages_count: Optional[int] = deserialize.integer(
            payload.get("unread_messages_count")
        )
        self.links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "service_sid": service_sid,
            "user_sid": user_sid,
        }

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.IpMessaging.V1.UserChannelInstance {}>".format(context)


class UserChannelPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> UserChannelInstance:
        """
        Build an instance of UserChannelInstance

        :param payload: Payload response from the API
        """
        return UserChannelInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            user_sid=self._solution["user_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.IpMessaging.V1.UserChannelPage>"


class UserChannelList(ListResource):
    def __init__(self, version: Version, service_sid: str, user_sid: str):
        """
        Initialize the UserChannelList

        :param version: Version that contains the resource
        :param service_sid:
        :param user_sid:

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "user_sid": user_sid,
        }
        self._uri = "/Services/{service_sid}/Users/{user_sid}/Channels".format(
            **self._solution
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[UserChannelInstance]:
        """
        Streams UserChannelInstance records from the API as a generator stream.
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
    ) -> List[UserChannelInstance]:
        """
        Asynchronously streams UserChannelInstance records from the API as a generator stream.
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
    ) -> List[UserChannelInstance]:
        """
        Lists UserChannelInstance records from the API as a list.
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
    ) -> List[UserChannelInstance]:
        """
        Asynchronously lists UserChannelInstance records from the API as a list.
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
        page_token: Optional[str] = None,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> UserChannelPage:
        """
        Retrieve a single page of UserChannelInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of UserChannelInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return UserChannelPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Optional[str] = None,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> UserChannelPage:
        """
        Asynchronously retrieve a single page of UserChannelInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of UserChannelInstance
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
        return UserChannelPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> UserChannelPage:
        """
        Retrieve a specific page of UserChannelInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of UserChannelInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return UserChannelPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> UserChannelPage:
        """
        Asynchronously retrieve a specific page of UserChannelInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of UserChannelInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return UserChannelPage(self._version, response, self._solution)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.IpMessaging.V1.UserChannelList>"
