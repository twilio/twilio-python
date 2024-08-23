r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Frontline
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Any, Dict, Optional, Union
from twilio.base import serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class UserInstance(InstanceResource):

    class StateType:
        ACTIVE = "active"
        DEACTIVATED = "deactivated"

    """
    :ivar sid: The unique string that we created to identify the User resource.
    :ivar identity: The application-defined string that uniquely identifies the resource's User. This value is often a username or an email address, and is case-sensitive.
    :ivar friendly_name: The string that you assigned to describe the User.
    :ivar avatar: The avatar URL which will be shown in Frontline application.
    :ivar state: 
    :ivar is_available: Whether the User is available for new conversations. Defaults to `false` for new users.
    :ivar url: An absolute API resource URL for this user.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.identity: Optional[str] = payload.get("identity")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.avatar: Optional[str] = payload.get("avatar")
        self.state: Optional["UserInstance.StateType"] = payload.get("state")
        self.is_available: Optional[bool] = payload.get("is_available")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[UserContext] = None

    @property
    def _proxy(self) -> "UserContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: UserContext for this UserInstance
        """
        if self._context is None:
            self._context = UserContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def fetch(self) -> "UserInstance":
        """
        Fetch the UserInstance


        :returns: The fetched UserInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "UserInstance":
        """
        Asynchronous coroutine to fetch the UserInstance


        :returns: The fetched UserInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        friendly_name: Union[str, object] = values.unset,
        avatar: Union[str, object] = values.unset,
        state: Union["UserInstance.StateType", object] = values.unset,
        is_available: Union[bool, object] = values.unset,
    ) -> "UserInstance":
        """
        Update the UserInstance

        :param friendly_name: The string that you assigned to describe the User.
        :param avatar: The avatar URL which will be shown in Frontline application.
        :param state:
        :param is_available: Whether the User is available for new conversations. Set to `false` to prevent User from receiving new inbound conversations if you are using [Pool Routing](https://www.twilio.com/docs/frontline/handle-incoming-conversations#3-pool-routing).

        :returns: The updated UserInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            avatar=avatar,
            state=state,
            is_available=is_available,
        )

    async def update_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        avatar: Union[str, object] = values.unset,
        state: Union["UserInstance.StateType", object] = values.unset,
        is_available: Union[bool, object] = values.unset,
    ) -> "UserInstance":
        """
        Asynchronous coroutine to update the UserInstance

        :param friendly_name: The string that you assigned to describe the User.
        :param avatar: The avatar URL which will be shown in Frontline application.
        :param state:
        :param is_available: Whether the User is available for new conversations. Set to `false` to prevent User from receiving new inbound conversations if you are using [Pool Routing](https://www.twilio.com/docs/frontline/handle-incoming-conversations#3-pool-routing).

        :returns: The updated UserInstance
        """
        return await self._proxy.update_async(
            friendly_name=friendly_name,
            avatar=avatar,
            state=state,
            is_available=is_available,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return f"<Twilio.FrontlineApi.V1.UserInstance {context}>"


class UserContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the UserContext

        :param version: Version that contains the resource
        :param sid: The SID of the User resource to update. This value can be either the `sid` or the `identity` of the User resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Users/{sid}".format(**self._solution)

    def fetch(self) -> UserInstance:
        """
        Fetch the UserInstance


        :returns: The fetched UserInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return UserInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> UserInstance:
        """
        Asynchronous coroutine to fetch the UserInstance


        :returns: The fetched UserInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return UserInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(
        self,
        friendly_name: Union[str, object] = values.unset,
        avatar: Union[str, object] = values.unset,
        state: Union["UserInstance.StateType", object] = values.unset,
        is_available: Union[bool, object] = values.unset,
    ) -> UserInstance:
        """
        Update the UserInstance

        :param friendly_name: The string that you assigned to describe the User.
        :param avatar: The avatar URL which will be shown in Frontline application.
        :param state:
        :param is_available: Whether the User is available for new conversations. Set to `false` to prevent User from receiving new inbound conversations if you are using [Pool Routing](https://www.twilio.com/docs/frontline/handle-incoming-conversations#3-pool-routing).

        :returns: The updated UserInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "Avatar": avatar,
                "State": state,
                "IsAvailable": serialize.boolean_to_string(is_available),
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return UserInstance(self._version, payload, sid=self._solution["sid"])

    async def update_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        avatar: Union[str, object] = values.unset,
        state: Union["UserInstance.StateType", object] = values.unset,
        is_available: Union[bool, object] = values.unset,
    ) -> UserInstance:
        """
        Asynchronous coroutine to update the UserInstance

        :param friendly_name: The string that you assigned to describe the User.
        :param avatar: The avatar URL which will be shown in Frontline application.
        :param state:
        :param is_available: Whether the User is available for new conversations. Set to `false` to prevent User from receiving new inbound conversations if you are using [Pool Routing](https://www.twilio.com/docs/frontline/handle-incoming-conversations#3-pool-routing).

        :returns: The updated UserInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "Avatar": avatar,
                "State": state,
                "IsAvailable": serialize.boolean_to_string(is_available),
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return UserInstance(self._version, payload, sid=self._solution["sid"])

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return f"<Twilio.FrontlineApi.V1.UserContext {context}>"


class UserList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the UserList

        :param version: Version that contains the resource

        """
        super().__init__(version)

    def get(self, sid: str) -> UserContext:
        """
        Constructs a UserContext

        :param sid: The SID of the User resource to update. This value can be either the `sid` or the `identity` of the User resource to update.
        """
        return UserContext(self._version, sid=sid)

    def __call__(self, sid: str) -> UserContext:
        """
        Constructs a UserContext

        :param sid: The SID of the User resource to update. This value can be either the `sid` or the `identity` of the User resource to update.
        """
        return UserContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.FrontlineApi.V1.UserList>"
