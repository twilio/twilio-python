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
from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class VariableList(ListResource):
    def __init__(self, version: Version, service_sid: str, environment_sid: str):
        """
        Initialize the VariableList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service to read the Variable resources from.
        :param environment_sid: The SID of the Environment with the Variable resources to read.

        :returns: twilio.rest.serverless.v1.service.environment.variable.VariableList
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariableList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "environment_sid": environment_sid,
        }
        self._uri = (
            "/Services/{service_sid}/Environments/{environment_sid}/Variables".format(
                **self._solution
            )
        )

    def create(self, key, value):
        """
        Create the VariableInstance

        :param str key: A string by which the Variable resource can be referenced. It can be a maximum of 128 characters.
        :param str value: A string that contains the actual value of the Variable. It can be a maximum of 450 bytes in size.

        :returns: The created VariableInstance
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariableInstance
        """
        data = values.of(
            {
                "Key": key,
                "Value": value,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return VariableInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            environment_sid=self._solution["environment_sid"],
        )

    async def create_async(self, key, value):
        """
        Asynchronously create the VariableInstance

        :param str key: A string by which the Variable resource can be referenced. It can be a maximum of 128 characters.
        :param str value: A string that contains the actual value of the Variable. It can be a maximum of 450 bytes in size.

        :returns: The created VariableInstance
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariableInstance
        """
        data = values.of(
            {
                "Key": key,
                "Value": value,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return VariableInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            environment_sid=self._solution["environment_sid"],
        )

    def stream(self, limit=None, page_size=None):
        """
        Streams VariableInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.serverless.v1.service.environment.variable.VariableInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronously streams VariableInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.serverless.v1.service.environment.variable.VariableInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(self, limit=None, page_size=None):
        """
        Lists VariableInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.serverless.v1.service.environment.variable.VariableInstance]
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronously lists VariableInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.serverless.v1.service.environment.variable.VariableInstance]
        """
        return list(
            await self.stream_async(
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Retrieve a single page of VariableInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of VariableInstance
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariablePage
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return VariablePage(self._version, response, self._solution)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Asynchronously retrieve a single page of VariableInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of VariableInstance
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariablePage
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
        return VariablePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of VariableInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of VariableInstance
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariablePage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return VariablePage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of VariableInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of VariableInstance
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariablePage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return VariablePage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a VariableContext

        :param sid: The SID of the Variable resource to update.

        :returns: twilio.rest.serverless.v1.service.environment.variable.VariableContext
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariableContext
        """
        return VariableContext(
            self._version,
            service_sid=self._solution["service_sid"],
            environment_sid=self._solution["environment_sid"],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a VariableContext

        :param sid: The SID of the Variable resource to update.

        :returns: twilio.rest.serverless.v1.service.environment.variable.VariableContext
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariableContext
        """
        return VariableContext(
            self._version,
            service_sid=self._solution["service_sid"],
            environment_sid=self._solution["environment_sid"],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Serverless.V1.VariableList>"


class VariablePage(Page):
    def get_instance(self, payload):
        """
        Build an instance of VariableInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.serverless.v1.service.environment.variable.VariableInstance
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariableInstance
        """
        return VariableInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            environment_sid=self._solution["environment_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Serverless.V1.VariablePage>"


class VariableInstance(InstanceResource):
    def __init__(
        self,
        version,
        payload,
        service_sid: str,
        environment_sid: str,
        sid: Optional[str] = None,
    ):
        """
        Initialize the VariableInstance

        :returns: twilio.rest.serverless.v1.service.environment.variable.VariableInstance
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariableInstance
        """
        super().__init__(version)

        self._properties = {
            "sid": payload.get("sid"),
            "account_sid": payload.get("account_sid"),
            "service_sid": payload.get("service_sid"),
            "environment_sid": payload.get("environment_sid"),
            "key": payload.get("key"),
            "value": payload.get("value"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "url": payload.get("url"),
        }

        self._solution = {
            "service_sid": service_sid,
            "environment_sid": environment_sid,
            "sid": sid or self._properties["sid"],
        }
        self._context: Optional[VariableContext] = None

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: VariableContext for this VariableInstance
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariableContext
        """
        if self._context is None:
            self._context = VariableContext(
                self._version,
                service_sid=self._solution["service_sid"],
                environment_sid=self._solution["environment_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Variable resource.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Variable resource.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def service_sid(self):
        """
        :returns: The SID of the Service that the Variable resource is associated with.
        :rtype: str
        """
        return self._properties["service_sid"]

    @property
    def environment_sid(self):
        """
        :returns: The SID of the Environment in which the Variable exists.
        :rtype: str
        """
        return self._properties["environment_sid"]

    @property
    def key(self):
        """
        :returns: A string by which the Variable resource can be referenced.
        :rtype: str
        """
        return self._properties["key"]

    @property
    def value(self):
        """
        :returns: A string that contains the actual value of the Variable.
        :rtype: str
        """
        return self._properties["value"]

    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the Variable resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties["date_created"]

    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the Variable resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties["date_updated"]

    @property
    def url(self):
        """
        :returns: The absolute URL of the Variable resource.
        :rtype: str
        """
        return self._properties["url"]

    def delete(self):
        """
        Deletes the VariableInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the VariableInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._proxy.delete_async()

    def fetch(self):
        """
        Fetch the VariableInstance


        :returns: The fetched VariableInstance
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariableInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the VariableInstance


        :returns: The fetched VariableInstance
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariableInstance
        """
        return await self._proxy.fetch_async()

    def update(self, key=values.unset, value=values.unset):
        """
        Update the VariableInstance

        :param str key: A string by which the Variable resource can be referenced. It can be a maximum of 128 characters.
        :param str value: A string that contains the actual value of the Variable. It can be a maximum of 450 bytes in size.

        :returns: The updated VariableInstance
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariableInstance
        """
        return self._proxy.update(
            key=key,
            value=value,
        )

    async def update_async(self, key=values.unset, value=values.unset):
        """
        Asynchronous coroutine to update the VariableInstance

        :param str key: A string by which the Variable resource can be referenced. It can be a maximum of 128 characters.
        :param str value: A string that contains the actual value of the Variable. It can be a maximum of 450 bytes in size.

        :returns: The updated VariableInstance
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariableInstance
        """
        return await self._proxy.update_async(
            key=key,
            value=value,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Serverless.V1.VariableInstance {}>".format(context)


class VariableContext(InstanceContext):
    def __init__(
        self, version: Version, service_sid: str, environment_sid: str, sid: str
    ):
        """
        Initialize the VariableContext

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service to update the Variable resource under.
        :param environment_sid: The SID of the Environment with the Variable resource to update.
        :param sid: The SID of the Variable resource to update.

        :returns: twilio.rest.serverless.v1.service.environment.variable.VariableContext
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariableContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "environment_sid": environment_sid,
            "sid": sid,
        }
        self._uri = "/Services/{service_sid}/Environments/{environment_sid}/Variables/{sid}".format(
            **self._solution
        )

    def delete(self):
        """
        Deletes the VariableInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the VariableInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self):
        """
        Fetch the VariableInstance


        :returns: The fetched VariableInstance
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariableInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return VariableInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            environment_sid=self._solution["environment_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the VariableInstance


        :returns: The fetched VariableInstance
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariableInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return VariableInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            environment_sid=self._solution["environment_sid"],
            sid=self._solution["sid"],
        )

    def update(self, key=values.unset, value=values.unset):
        """
        Update the VariableInstance

        :param str key: A string by which the Variable resource can be referenced. It can be a maximum of 128 characters.
        :param str value: A string that contains the actual value of the Variable. It can be a maximum of 450 bytes in size.

        :returns: The updated VariableInstance
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariableInstance
        """
        data = values.of(
            {
                "Key": key,
                "Value": value,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return VariableInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            environment_sid=self._solution["environment_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(self, key=values.unset, value=values.unset):
        """
        Asynchronous coroutine to update the VariableInstance

        :param str key: A string by which the Variable resource can be referenced. It can be a maximum of 128 characters.
        :param str value: A string that contains the actual value of the Variable. It can be a maximum of 450 bytes in size.

        :returns: The updated VariableInstance
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariableInstance
        """
        data = values.of(
            {
                "Key": key,
                "Value": value,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return VariableInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            environment_sid=self._solution["environment_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Serverless.V1.VariableContext {}>".format(context)
