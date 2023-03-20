r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Serverless
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Optional
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class FunctionVersionContentList(ListResource):
    def __init__(self, version: Version, service_sid: str, function_sid: str, sid: str):
        """
        Initialize the FunctionVersionContentList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service to fetch the Function Version content from.
        :param function_sid: The SID of the Function that is the parent of the Function Version content to fetch.
        :param sid: The SID of the Function Version content to fetch.

        :returns: twilio.rest.serverless.v1.service.function.function_version.function_version_content.FunctionVersionContentList
        :rtype: twilio.rest.serverless.v1.service.function.function_version.function_version_content.FunctionVersionContentList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "function_sid": function_sid,
            "sid": sid,
        }

    def get(self):
        """
        Constructs a FunctionVersionContentContext


        :returns: twilio.rest.serverless.v1.service.function.function_version.function_version_content.FunctionVersionContentContext
        :rtype: twilio.rest.serverless.v1.service.function.function_version.function_version_content.FunctionVersionContentContext
        """
        return FunctionVersionContentContext(
            self._version,
            service_sid=self._solution["service_sid"],
            function_sid=self._solution["function_sid"],
            sid=self._solution["sid"],
        )

    def __call__(self):
        """
        Constructs a FunctionVersionContentContext


        :returns: twilio.rest.serverless.v1.service.function.function_version.function_version_content.FunctionVersionContentContext
        :rtype: twilio.rest.serverless.v1.service.function.function_version.function_version_content.FunctionVersionContentContext
        """
        return FunctionVersionContentContext(
            self._version,
            service_sid=self._solution["service_sid"],
            function_sid=self._solution["function_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Serverless.V1.FunctionVersionContentList>"


class FunctionVersionContentInstance(InstanceResource):
    def __init__(self, version, payload, service_sid: str, function_sid: str, sid: str):
        """
        Initialize the FunctionVersionContentInstance

        :returns: twilio.rest.serverless.v1.service.function.function_version.function_version_content.FunctionVersionContentInstance
        :rtype: twilio.rest.serverless.v1.service.function.function_version.function_version_content.FunctionVersionContentInstance
        """
        super().__init__(version)

        self._properties = {
            "sid": payload.get("sid"),
            "account_sid": payload.get("account_sid"),
            "service_sid": payload.get("service_sid"),
            "function_sid": payload.get("function_sid"),
            "content": payload.get("content"),
            "url": payload.get("url"),
        }

        self._solution = {
            "service_sid": service_sid,
            "function_sid": function_sid,
            "sid": sid,
        }
        self._context: Optional[FunctionVersionContentContext] = None

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: FunctionVersionContentContext for this FunctionVersionContentInstance
        :rtype: twilio.rest.serverless.v1.service.function.function_version.function_version_content.FunctionVersionContentContext
        """
        if self._context is None:
            self._context = FunctionVersionContentContext(
                self._version,
                service_sid=self._solution["service_sid"],
                function_sid=self._solution["function_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Function Version resource.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Function Version resource.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def service_sid(self):
        """
        :returns: The SID of the Service that the Function Version resource is associated with.
        :rtype: str
        """
        return self._properties["service_sid"]

    @property
    def function_sid(self):
        """
        :returns: The SID of the Function that is the parent of the Function Version.
        :rtype: str
        """
        return self._properties["function_sid"]

    @property
    def content(self):
        """
        :returns: The content of the Function Version resource.
        :rtype: str
        """
        return self._properties["content"]

    @property
    def url(self):
        """
        :returns:
        :rtype: str
        """
        return self._properties["url"]

    def fetch(self):
        """
        Fetch the FunctionVersionContentInstance


        :returns: The fetched FunctionVersionContentInstance
        :rtype: twilio.rest.serverless.v1.service.function.function_version.function_version_content.FunctionVersionContentInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the FunctionVersionContentInstance


        :returns: The fetched FunctionVersionContentInstance
        :rtype: twilio.rest.serverless.v1.service.function.function_version.function_version_content.FunctionVersionContentInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Serverless.V1.FunctionVersionContentInstance {}>".format(
            context
        )


class FunctionVersionContentContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, function_sid: str, sid: str):
        """
        Initialize the FunctionVersionContentContext

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service to fetch the Function Version content from.
        :param function_sid: The SID of the Function that is the parent of the Function Version content to fetch.
        :param sid: The SID of the Function Version content to fetch.

        :returns: twilio.rest.serverless.v1.service.function.function_version.function_version_content.FunctionVersionContentContext
        :rtype: twilio.rest.serverless.v1.service.function.function_version.function_version_content.FunctionVersionContentContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "function_sid": function_sid,
            "sid": sid,
        }
        self._uri = "/Services/{service_sid}/Functions/{function_sid}/Versions/{sid}/Content".format(
            **self._solution
        )

    def fetch(self):
        """
        Fetch the FunctionVersionContentInstance


        :returns: The fetched FunctionVersionContentInstance
        :rtype: twilio.rest.serverless.v1.service.function.function_version.function_version_content.FunctionVersionContentInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return FunctionVersionContentInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            function_sid=self._solution["function_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the FunctionVersionContentInstance


        :returns: The fetched FunctionVersionContentInstance
        :rtype: twilio.rest.serverless.v1.service.function.function_version.function_version_content.FunctionVersionContentInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return FunctionVersionContentInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            function_sid=self._solution["function_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Serverless.V1.FunctionVersionContentContext {}>".format(context)
