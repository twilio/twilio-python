r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Supersim
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class EsimProfileInstance(InstanceResource):
    class Status(object):
        NEW = "new"
        RESERVING = "reserving"
        AVAILABLE = "available"
        DOWNLOADED = "downloaded"
        INSTALLED = "installed"
        FAILED = "failed"

    """
    :ivar sid: The unique string that we created to identify the eSIM Profile resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) to which the eSIM Profile resource belongs.
    :ivar iccid: The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module#ICCID) associated with the Sim resource.
    :ivar sim_sid: The SID of the [Sim](https://www.twilio.com/docs/wireless/api/sim-resource) resource that this eSIM Profile controls.
    :ivar status: 
    :ivar eid: Identifier of the eUICC that can claim the eSIM Profile.
    :ivar smdp_plus_address: Address of the SM-DP+ server from which the Profile will be downloaded. The URL will appear once the eSIM Profile reaches the status `available`.
    :ivar matching_id: Unique identifier of the eSIM profile that can be used to identify and download the eSIM profile from the SM-DP+ server. Populated if `generate_matching_id` is set to `true` when creating the eSIM profile reservation.
    :ivar activation_code: Combined machine-readable activation code for acquiring an eSIM Profile with the Activation Code download method. Can be used in a QR code to download an eSIM profile.
    :ivar error_code: Code indicating the failure if the download of the SIM Profile failed and the eSIM Profile is in `failed` state.
    :ivar error_message: Error message describing the failure if the download of the SIM Profile failed and the eSIM Profile is in `failed` state.
    :ivar date_created: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar url: The absolute URL of the eSIM Profile resource.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.iccid: Optional[str] = payload.get("iccid")
        self.sim_sid: Optional[str] = payload.get("sim_sid")
        self.status: Optional["EsimProfileInstance.Status"] = payload.get("status")
        self.eid: Optional[str] = payload.get("eid")
        self.smdp_plus_address: Optional[str] = payload.get("smdp_plus_address")
        self.matching_id: Optional[str] = payload.get("matching_id")
        self.activation_code: Optional[str] = payload.get("activation_code")
        self.error_code: Optional[str] = payload.get("error_code")
        self.error_message: Optional[str] = payload.get("error_message")
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
        self._context: Optional[EsimProfileContext] = None

    @property
    def _proxy(self) -> "EsimProfileContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: EsimProfileContext for this EsimProfileInstance
        """
        if self._context is None:
            self._context = EsimProfileContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def fetch(self) -> "EsimProfileInstance":
        """
        Fetch the EsimProfileInstance


        :returns: The fetched EsimProfileInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "EsimProfileInstance":
        """
        Asynchronous coroutine to fetch the EsimProfileInstance


        :returns: The fetched EsimProfileInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Supersim.V1.EsimProfileInstance {}>".format(context)


class EsimProfileContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the EsimProfileContext

        :param version: Version that contains the resource
        :param sid: The SID of the eSIM Profile resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/ESimProfiles/{sid}".format(**self._solution)

    def fetch(self) -> EsimProfileInstance:
        """
        Fetch the EsimProfileInstance


        :returns: The fetched EsimProfileInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return EsimProfileInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> EsimProfileInstance:
        """
        Asynchronous coroutine to fetch the EsimProfileInstance


        :returns: The fetched EsimProfileInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return EsimProfileInstance(
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
        return "<Twilio.Supersim.V1.EsimProfileContext {}>".format(context)


class EsimProfilePage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> EsimProfileInstance:
        """
        Build an instance of EsimProfileInstance

        :param payload: Payload response from the API
        """
        return EsimProfileInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Supersim.V1.EsimProfilePage>"


class EsimProfileList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the EsimProfileList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/ESimProfiles"

    def create(
        self,
        callback_url: Union[str, object] = values.unset,
        callback_method: Union[str, object] = values.unset,
        generate_matching_id: Union[bool, object] = values.unset,
        eid: Union[str, object] = values.unset,
    ) -> EsimProfileInstance:
        """
        Create the EsimProfileInstance

        :param callback_url: The URL we should call using the `callback_method` when the status of the eSIM Profile changes. At this stage of the eSIM Profile pilot, the a request to the URL will only be called when the ESimProfile resource changes from `reserving` to `available`.
        :param callback_method: The HTTP method we should use to call `callback_url`. Can be: `GET` or `POST` and the default is POST.
        :param generate_matching_id: When set to `true`, a value for `Eid` does not need to be provided. Instead, when the eSIM profile is reserved, a matching ID will be generated and returned via the `matching_id` property. This identifies the specific eSIM profile that can be used by any capable device to claim and download the profile.
        :param eid: Identifier of the eUICC that will claim the eSIM Profile.

        :returns: The created EsimProfileInstance
        """
        data = values.of(
            {
                "CallbackUrl": callback_url,
                "CallbackMethod": callback_method,
                "GenerateMatchingId": generate_matching_id,
                "Eid": eid,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return EsimProfileInstance(self._version, payload)

    async def create_async(
        self,
        callback_url: Union[str, object] = values.unset,
        callback_method: Union[str, object] = values.unset,
        generate_matching_id: Union[bool, object] = values.unset,
        eid: Union[str, object] = values.unset,
    ) -> EsimProfileInstance:
        """
        Asynchronously create the EsimProfileInstance

        :param callback_url: The URL we should call using the `callback_method` when the status of the eSIM Profile changes. At this stage of the eSIM Profile pilot, the a request to the URL will only be called when the ESimProfile resource changes from `reserving` to `available`.
        :param callback_method: The HTTP method we should use to call `callback_url`. Can be: `GET` or `POST` and the default is POST.
        :param generate_matching_id: When set to `true`, a value for `Eid` does not need to be provided. Instead, when the eSIM profile is reserved, a matching ID will be generated and returned via the `matching_id` property. This identifies the specific eSIM profile that can be used by any capable device to claim and download the profile.
        :param eid: Identifier of the eUICC that will claim the eSIM Profile.

        :returns: The created EsimProfileInstance
        """
        data = values.of(
            {
                "CallbackUrl": callback_url,
                "CallbackMethod": callback_method,
                "GenerateMatchingId": generate_matching_id,
                "Eid": eid,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return EsimProfileInstance(self._version, payload)

    def stream(
        self,
        eid: Union[str, object] = values.unset,
        sim_sid: Union[str, object] = values.unset,
        status: Union["EsimProfileInstance.Status", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[EsimProfileInstance]:
        """
        Streams EsimProfileInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str eid: List the eSIM Profiles that have been associated with an EId.
        :param str sim_sid: Find the eSIM Profile resource related to a [Sim](https://www.twilio.com/docs/wireless/api/sim-resource) resource by providing the SIM SID. Will always return an array with either 1 or 0 records.
        :param &quot;EsimProfileInstance.Status&quot; status: List the eSIM Profiles that are in a given status.
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
            eid=eid, sim_sid=sim_sid, status=status, page_size=limits["page_size"]
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        eid: Union[str, object] = values.unset,
        sim_sid: Union[str, object] = values.unset,
        status: Union["EsimProfileInstance.Status", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[EsimProfileInstance]:
        """
        Asynchronously streams EsimProfileInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str eid: List the eSIM Profiles that have been associated with an EId.
        :param str sim_sid: Find the eSIM Profile resource related to a [Sim](https://www.twilio.com/docs/wireless/api/sim-resource) resource by providing the SIM SID. Will always return an array with either 1 or 0 records.
        :param &quot;EsimProfileInstance.Status&quot; status: List the eSIM Profiles that are in a given status.
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
            eid=eid, sim_sid=sim_sid, status=status, page_size=limits["page_size"]
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        eid: Union[str, object] = values.unset,
        sim_sid: Union[str, object] = values.unset,
        status: Union["EsimProfileInstance.Status", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[EsimProfileInstance]:
        """
        Lists EsimProfileInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str eid: List the eSIM Profiles that have been associated with an EId.
        :param str sim_sid: Find the eSIM Profile resource related to a [Sim](https://www.twilio.com/docs/wireless/api/sim-resource) resource by providing the SIM SID. Will always return an array with either 1 or 0 records.
        :param &quot;EsimProfileInstance.Status&quot; status: List the eSIM Profiles that are in a given status.
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
                eid=eid,
                sim_sid=sim_sid,
                status=status,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        eid: Union[str, object] = values.unset,
        sim_sid: Union[str, object] = values.unset,
        status: Union["EsimProfileInstance.Status", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[EsimProfileInstance]:
        """
        Asynchronously lists EsimProfileInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str eid: List the eSIM Profiles that have been associated with an EId.
        :param str sim_sid: Find the eSIM Profile resource related to a [Sim](https://www.twilio.com/docs/wireless/api/sim-resource) resource by providing the SIM SID. Will always return an array with either 1 or 0 records.
        :param &quot;EsimProfileInstance.Status&quot; status: List the eSIM Profiles that are in a given status.
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
                eid=eid,
                sim_sid=sim_sid,
                status=status,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        eid: Union[str, object] = values.unset,
        sim_sid: Union[str, object] = values.unset,
        status: Union["EsimProfileInstance.Status", object] = values.unset,
        page_token: Optional[str] = None,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> EsimProfilePage:
        """
        Retrieve a single page of EsimProfileInstance records from the API.
        Request is executed immediately

        :param eid: List the eSIM Profiles that have been associated with an EId.
        :param sim_sid: Find the eSIM Profile resource related to a [Sim](https://www.twilio.com/docs/wireless/api/sim-resource) resource by providing the SIM SID. Will always return an array with either 1 or 0 records.
        :param status: List the eSIM Profiles that are in a given status.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of EsimProfileInstance
        """
        data = values.of(
            {
                "Eid": eid,
                "SimSid": sim_sid,
                "Status": status,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return EsimProfilePage(self._version, response)

    async def page_async(
        self,
        eid: Union[str, object] = values.unset,
        sim_sid: Union[str, object] = values.unset,
        status: Union["EsimProfileInstance.Status", object] = values.unset,
        page_token: Optional[str] = None,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> EsimProfilePage:
        """
        Asynchronously retrieve a single page of EsimProfileInstance records from the API.
        Request is executed immediately

        :param eid: List the eSIM Profiles that have been associated with an EId.
        :param sim_sid: Find the eSIM Profile resource related to a [Sim](https://www.twilio.com/docs/wireless/api/sim-resource) resource by providing the SIM SID. Will always return an array with either 1 or 0 records.
        :param status: List the eSIM Profiles that are in a given status.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of EsimProfileInstance
        """
        data = values.of(
            {
                "Eid": eid,
                "SimSid": sim_sid,
                "Status": status,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return EsimProfilePage(self._version, response)

    def get_page(self, target_url: str) -> EsimProfilePage:
        """
        Retrieve a specific page of EsimProfileInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of EsimProfileInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return EsimProfilePage(self._version, response)

    async def get_page_async(self, target_url: str) -> EsimProfilePage:
        """
        Asynchronously retrieve a specific page of EsimProfileInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of EsimProfileInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return EsimProfilePage(self._version, response)

    def get(self, sid: str) -> EsimProfileContext:
        """
        Constructs a EsimProfileContext

        :param sid: The SID of the eSIM Profile resource to fetch.
        """
        return EsimProfileContext(self._version, sid=sid)

    def __call__(self, sid: str) -> EsimProfileContext:
        """
        Constructs a EsimProfileContext

        :param sid: The SID of the eSIM Profile resource to fetch.
        """
        return EsimProfileContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Supersim.V1.EsimProfileList>"
