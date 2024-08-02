r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Verify
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Any, Dict, Optional
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class SafelistInstance(InstanceResource):
    """
    :ivar sid: The unique string that we created to identify the SafeList resource.
    :ivar phone_number: The phone number in SafeList.
    :ivar url: The absolute URL of the SafeList resource.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        phone_number: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.phone_number: Optional[str] = payload.get("phone_number")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "phone_number": phone_number or self.phone_number,
        }
        self._context: Optional[SafelistContext] = None

    @property
    def _proxy(self) -> "SafelistContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SafelistContext for this SafelistInstance
        """
        if self._context is None:
            self._context = SafelistContext(
                self._version,
                phone_number=self._solution["phone_number"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the SafelistInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the SafelistInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "SafelistInstance":
        """
        Fetch the SafelistInstance


        :returns: The fetched SafelistInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "SafelistInstance":
        """
        Asynchronous coroutine to fetch the SafelistInstance


        :returns: The fetched SafelistInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Verify.V2.SafelistInstance {}>".format(context)


class SafelistContext(InstanceContext):

    def __init__(self, version: Version, phone_number: str):
        """
        Initialize the SafelistContext

        :param version: Version that contains the resource
        :param phone_number: The phone number to be fetched from SafeList. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "phone_number": phone_number,
        }
        self._uri = "/SafeList/Numbers/{phone_number}".format(**self._solution)

    def delete(self) -> bool:
        """
        Deletes the SafelistInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the SafelistInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> SafelistInstance:
        """
        Fetch the SafelistInstance


        :returns: The fetched SafelistInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return SafelistInstance(
            self._version,
            payload,
            phone_number=self._solution["phone_number"],
        )

    async def fetch_async(self) -> SafelistInstance:
        """
        Asynchronous coroutine to fetch the SafelistInstance


        :returns: The fetched SafelistInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return SafelistInstance(
            self._version,
            payload,
            phone_number=self._solution["phone_number"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Verify.V2.SafelistContext {}>".format(context)


class SafelistList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the SafelistList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/SafeList/Numbers"

    def create(self, phone_number: str) -> SafelistInstance:
        """
        Create the SafelistInstance

        :param phone_number: The phone number to be added in SafeList. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).

        :returns: The created SafelistInstance
        """

        data = values.of(
            {
                "PhoneNumber": phone_number,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return SafelistInstance(self._version, payload)

    async def create_async(self, phone_number: str) -> SafelistInstance:
        """
        Asynchronously create the SafelistInstance

        :param phone_number: The phone number to be added in SafeList. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).

        :returns: The created SafelistInstance
        """

        data = values.of(
            {
                "PhoneNumber": phone_number,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return SafelistInstance(self._version, payload)

    def get(self, phone_number: str) -> SafelistContext:
        """
        Constructs a SafelistContext

        :param phone_number: The phone number to be fetched from SafeList. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
        """
        return SafelistContext(self._version, phone_number=phone_number)

    def __call__(self, phone_number: str) -> SafelistContext:
        """
        Constructs a SafelistContext

        :param phone_number: The phone number to be fetched from SafeList. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
        """
        return SafelistContext(self._version, phone_number=phone_number)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Verify.V2.SafelistList>"
