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


from typing import Any, Dict, List, Optional, Union
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class RegulationInstance(InstanceResource):
    class EndUserType(object):
        INDIVIDUAL = "individual"
        BUSINESS = "business"

    """
    :ivar sid: The unique string that identifies the Regulation resource.
    :ivar friendly_name: A human-readable description that is assigned to describe the Regulation resource. Examples can include Germany: Mobile - Business.
    :ivar iso_country: The ISO country code of the phone number's country.
    :ivar number_type: The type of phone number restricted by the regulatory requirement. For example, Germany mobile phone numbers provisioned by businesses require a business name with commercial register proof from the Handelsregisterauszug and a proof of address from Handelsregisterauszug or a trade license by Gewerbeanmeldung.
    :ivar end_user_type: 
    :ivar requirements: The SID of an object that holds the regulatory information of the phone number country, phone number type, and end user type.
    :ivar url: The absolute URL of the Regulation resource.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.iso_country: Optional[str] = payload.get("iso_country")
        self.number_type: Optional[str] = payload.get("number_type")
        self.end_user_type: Optional["RegulationInstance.EndUserType"] = payload.get(
            "end_user_type"
        )
        self.requirements: Optional[Dict[str, object]] = payload.get("requirements")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[RegulationContext] = None

    @property
    def _proxy(self) -> "RegulationContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: RegulationContext for this RegulationInstance
        """
        if self._context is None:
            self._context = RegulationContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def fetch(self) -> "RegulationInstance":
        """
        Fetch the RegulationInstance


        :returns: The fetched RegulationInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "RegulationInstance":
        """
        Asynchronous coroutine to fetch the RegulationInstance


        :returns: The fetched RegulationInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Numbers.V2.RegulationInstance {}>".format(context)


class RegulationContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the RegulationContext

        :param version: Version that contains the resource
        :param sid: The unique string that identifies the Regulation resource.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/RegulatoryCompliance/Regulations/{sid}".format(**self._solution)

    def fetch(self) -> RegulationInstance:
        """
        Fetch the RegulationInstance


        :returns: The fetched RegulationInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return RegulationInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> RegulationInstance:
        """
        Asynchronous coroutine to fetch the RegulationInstance


        :returns: The fetched RegulationInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return RegulationInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Numbers.V2.RegulationContext {}>".format(context)


class RegulationPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> RegulationInstance:
        """
        Build an instance of RegulationInstance

        :param payload: Payload response from the API
        """
        return RegulationInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Numbers.V2.RegulationPage>"


class RegulationList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the RegulationList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/RegulatoryCompliance/Regulations"

    def stream(
        self,
        end_user_type: Union["RegulationInstance.EndUserType", object] = values.unset,
        iso_country: Union[str, object] = values.unset,
        number_type: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[RegulationInstance]:
        """
        Streams RegulationInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;RegulationInstance.EndUserType&quot; end_user_type: The type of End User the regulation requires - can be `individual` or `business`.
        :param str iso_country: The ISO country code of the phone number's country.
        :param str number_type: The type of phone number that the regulatory requiremnt is restricting.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            end_user_type=end_user_type,
            iso_country=iso_country,
            number_type=number_type,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        end_user_type: Union["RegulationInstance.EndUserType", object] = values.unset,
        iso_country: Union[str, object] = values.unset,
        number_type: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[RegulationInstance]:
        """
        Asynchronously streams RegulationInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;RegulationInstance.EndUserType&quot; end_user_type: The type of End User the regulation requires - can be `individual` or `business`.
        :param str iso_country: The ISO country code of the phone number's country.
        :param str number_type: The type of phone number that the regulatory requiremnt is restricting.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            end_user_type=end_user_type,
            iso_country=iso_country,
            number_type=number_type,
            page_size=limits["page_size"],
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        end_user_type: Union["RegulationInstance.EndUserType", object] = values.unset,
        iso_country: Union[str, object] = values.unset,
        number_type: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[RegulationInstance]:
        """
        Lists RegulationInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;RegulationInstance.EndUserType&quot; end_user_type: The type of End User the regulation requires - can be `individual` or `business`.
        :param str iso_country: The ISO country code of the phone number's country.
        :param str number_type: The type of phone number that the regulatory requiremnt is restricting.
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
                end_user_type=end_user_type,
                iso_country=iso_country,
                number_type=number_type,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        end_user_type: Union["RegulationInstance.EndUserType", object] = values.unset,
        iso_country: Union[str, object] = values.unset,
        number_type: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[RegulationInstance]:
        """
        Asynchronously lists RegulationInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;RegulationInstance.EndUserType&quot; end_user_type: The type of End User the regulation requires - can be `individual` or `business`.
        :param str iso_country: The ISO country code of the phone number's country.
        :param str number_type: The type of phone number that the regulatory requiremnt is restricting.
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
                end_user_type=end_user_type,
                iso_country=iso_country,
                number_type=number_type,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        end_user_type: Union["RegulationInstance.EndUserType", object] = values.unset,
        iso_country: Union[str, object] = values.unset,
        number_type: Union[str, object] = values.unset,
        page_token: Union[str, object] = None,
        page_number: Union[int, object] = None,
        page_size: Union[int, object] = None,
    ) -> RegulationPage:
        """
        Retrieve a single page of RegulationInstance records from the API.
        Request is executed immediately

        :param end_user_type: The type of End User the regulation requires - can be `individual` or `business`.
        :param iso_country: The ISO country code of the phone number's country.
        :param number_type: The type of phone number that the regulatory requiremnt is restricting.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of RegulationInstance
        """
        data = values.of(
            {
                "EndUserType": end_user_type,
                "IsoCountry": iso_country,
                "NumberType": number_type,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return RegulationPage(self._version, response)

    async def page_async(
        self,
        end_user_type: Union["RegulationInstance.EndUserType", object] = values.unset,
        iso_country: Union[str, object] = values.unset,
        number_type: Union[str, object] = values.unset,
        page_token: Union[str, object] = None,
        page_number: Union[int, object] = None,
        page_size: Union[int, object] = None,
    ) -> RegulationPage:
        """
        Asynchronously retrieve a single page of RegulationInstance records from the API.
        Request is executed immediately

        :param end_user_type: The type of End User the regulation requires - can be `individual` or `business`.
        :param iso_country: The ISO country code of the phone number's country.
        :param number_type: The type of phone number that the regulatory requiremnt is restricting.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of RegulationInstance
        """
        data = values.of(
            {
                "EndUserType": end_user_type,
                "IsoCountry": iso_country,
                "NumberType": number_type,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return RegulationPage(self._version, response)

    def get_page(self, target_url: str) -> RegulationPage:
        """
        Retrieve a specific page of RegulationInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of RegulationInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return RegulationPage(self._version, response)

    async def get_page_async(self, target_url: str) -> RegulationPage:
        """
        Asynchronously retrieve a specific page of RegulationInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of RegulationInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return RegulationPage(self._version, response)

    def get(self, sid: str) -> RegulationContext:
        """
        Constructs a RegulationContext

        :param sid: The unique string that identifies the Regulation resource.
        """
        return RegulationContext(self._version, sid=sid)

    def __call__(self, sid: str) -> RegulationContext:
        """
        Constructs a RegulationContext

        :param sid: The unique string that identifies the Regulation resource.
        """
        return RegulationContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Numbers.V2.RegulationList>"
