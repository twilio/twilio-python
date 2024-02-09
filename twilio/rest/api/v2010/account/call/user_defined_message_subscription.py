r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, Optional, Union
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class UserDefinedMessageSubscriptionInstance(InstanceResource):
    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that subscribed to the User Defined Messages.
    :ivar call_sid: The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the User Defined Message Subscription is associated with. This refers to the Call SID that is producing the User Defined Messages.
    :ivar sid: The SID that uniquely identifies this User Defined Message Subscription.
    :ivar date_created: The date that this User Defined Message Subscription was created, given in RFC 2822 format.
    :ivar uri: The URI of the User Defined Message Subscription Resource, relative to `https://api.twilio.com`.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        account_sid: str,
        call_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.call_sid: Optional[str] = payload.get("call_sid")
        self.sid: Optional[str] = payload.get("sid")
        self.date_created: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_created")
        )
        self.uri: Optional[str] = payload.get("uri")

        self._solution = {
            "account_sid": account_sid,
            "call_sid": call_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[UserDefinedMessageSubscriptionContext] = None

    @property
    def _proxy(self) -> "UserDefinedMessageSubscriptionContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: UserDefinedMessageSubscriptionContext for this UserDefinedMessageSubscriptionInstance
        """
        if self._context is None:
            self._context = UserDefinedMessageSubscriptionContext(
                self._version,
                account_sid=self._solution["account_sid"],
                call_sid=self._solution["call_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the UserDefinedMessageSubscriptionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the UserDefinedMessageSubscriptionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.UserDefinedMessageSubscriptionInstance {}>".format(
            context
        )


class UserDefinedMessageSubscriptionContext(InstanceContext):
    def __init__(self, version: Version, account_sid: str, call_sid: str, sid: str):
        """
        Initialize the UserDefinedMessageSubscriptionContext

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that subscribed to the User Defined Messages.
        :param call_sid: The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the User Defined Message Subscription is associated with. This refers to the Call SID that is producing the User Defined Messages.
        :param sid: The SID that uniquely identifies this User Defined Message Subscription.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "call_sid": call_sid,
            "sid": sid,
        }
        self._uri = "/Accounts/{account_sid}/Calls/{call_sid}/UserDefinedMessageSubscriptions/{sid}.json".format(
            **self._solution
        )

    def delete(self) -> bool:
        """
        Deletes the UserDefinedMessageSubscriptionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the UserDefinedMessageSubscriptionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.UserDefinedMessageSubscriptionContext {}>".format(
            context
        )


class UserDefinedMessageSubscriptionList(ListResource):
    def __init__(self, version: Version, account_sid: str, call_sid: str):
        """
        Initialize the UserDefinedMessageSubscriptionList

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that subscribed to the User Defined Messages.
        :param call_sid: The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the User Defined Messages subscription is associated with. This refers to the Call SID that is producing the user defined messages.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "call_sid": call_sid,
        }
        self._uri = "/Accounts/{account_sid}/Calls/{call_sid}/UserDefinedMessageSubscriptions.json".format(
            **self._solution
        )

    def create(
        self,
        callback: str,
        idempotency_key: Union[str, object] = values.unset,
        method: Union[str, object] = values.unset,
    ) -> UserDefinedMessageSubscriptionInstance:
        """
        Create the UserDefinedMessageSubscriptionInstance

        :param callback: The URL we should call using the `method` to send user defined events to your application. URLs must contain a valid hostname (underscores are not permitted).
        :param idempotency_key: A unique string value to identify API call. This should be a unique string value per API call and can be a randomly generated.
        :param method: The HTTP method Twilio will use when requesting the above `Url`. Either `GET` or `POST`. Default is `POST`.

        :returns: The created UserDefinedMessageSubscriptionInstance
        """
        data = values.of(
            {
                "Callback": callback,
                "IdempotencyKey": idempotency_key,
                "Method": method,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return UserDefinedMessageSubscriptionInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            call_sid=self._solution["call_sid"],
        )

    async def create_async(
        self,
        callback: str,
        idempotency_key: Union[str, object] = values.unset,
        method: Union[str, object] = values.unset,
    ) -> UserDefinedMessageSubscriptionInstance:
        """
        Asynchronously create the UserDefinedMessageSubscriptionInstance

        :param callback: The URL we should call using the `method` to send user defined events to your application. URLs must contain a valid hostname (underscores are not permitted).
        :param idempotency_key: A unique string value to identify API call. This should be a unique string value per API call and can be a randomly generated.
        :param method: The HTTP method Twilio will use when requesting the above `Url`. Either `GET` or `POST`. Default is `POST`.

        :returns: The created UserDefinedMessageSubscriptionInstance
        """
        data = values.of(
            {
                "Callback": callback,
                "IdempotencyKey": idempotency_key,
                "Method": method,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return UserDefinedMessageSubscriptionInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            call_sid=self._solution["call_sid"],
        )

    def get(self, sid: str) -> UserDefinedMessageSubscriptionContext:
        """
        Constructs a UserDefinedMessageSubscriptionContext

        :param sid: The SID that uniquely identifies this User Defined Message Subscription.
        """
        return UserDefinedMessageSubscriptionContext(
            self._version,
            account_sid=self._solution["account_sid"],
            call_sid=self._solution["call_sid"],
            sid=sid,
        )

    def __call__(self, sid: str) -> UserDefinedMessageSubscriptionContext:
        """
        Constructs a UserDefinedMessageSubscriptionContext

        :param sid: The SID that uniquely identifies this User Defined Message Subscription.
        """
        return UserDefinedMessageSubscriptionContext(
            self._version,
            account_sid=self._solution["account_sid"],
            call_sid=self._solution["call_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.UserDefinedMessageSubscriptionList>"
