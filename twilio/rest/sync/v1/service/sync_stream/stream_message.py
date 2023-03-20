r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Sync
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import serialize
from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class StreamMessageList(ListResource):
    def __init__(self, version: Version, service_sid: str, stream_sid: str):
        """
        Initialize the StreamMessageList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) to create the new Stream Message in.
        :param stream_sid: The SID of the Sync Stream to create the new Stream Message resource for.

        :returns: twilio.rest.sync.v1.service.sync_stream.stream_message.StreamMessageList
        :rtype: twilio.rest.sync.v1.service.sync_stream.stream_message.StreamMessageList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "stream_sid": stream_sid,
        }
        self._uri = "/Services/{service_sid}/Streams/{stream_sid}/Messages".format(
            **self._solution
        )

    def create(self, data):
        """
        Create the StreamMessageInstance

        :param object data: A JSON string that represents an arbitrary, schema-less object that makes up the Stream Message body. Can be up to 4 KiB in length.

        :returns: The created StreamMessageInstance
        :rtype: twilio.rest.sync.v1.service.sync_stream.stream_message.StreamMessageInstance
        """
        data = values.of(
            {
                "Data": serialize.object(data),
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return StreamMessageInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            stream_sid=self._solution["stream_sid"],
        )

    async def create_async(self, data):
        """
        Asynchronously create the StreamMessageInstance

        :param object data: A JSON string that represents an arbitrary, schema-less object that makes up the Stream Message body. Can be up to 4 KiB in length.

        :returns: The created StreamMessageInstance
        :rtype: twilio.rest.sync.v1.service.sync_stream.stream_message.StreamMessageInstance
        """
        data = values.of(
            {
                "Data": serialize.object(data),
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return StreamMessageInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            stream_sid=self._solution["stream_sid"],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Sync.V1.StreamMessageList>"


class StreamMessageInstance(InstanceResource):
    def __init__(self, version, payload, service_sid: str, stream_sid: str):
        """
        Initialize the StreamMessageInstance

        :returns: twilio.rest.sync.v1.service.sync_stream.stream_message.StreamMessageInstance
        :rtype: twilio.rest.sync.v1.service.sync_stream.stream_message.StreamMessageInstance
        """
        super().__init__(version)

        self._properties = {
            "sid": payload.get("sid"),
            "data": payload.get("data"),
        }

        self._solution = {
            "service_sid": service_sid,
            "stream_sid": stream_sid,
        }

    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Stream Message resource.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def data(self):
        """
        :returns: An arbitrary, schema-less object that contains the Stream Message body. Can be up to 4 KiB in length.
        :rtype: dict
        """
        return self._properties["data"]

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Sync.V1.StreamMessageInstance {}>".format(context)
