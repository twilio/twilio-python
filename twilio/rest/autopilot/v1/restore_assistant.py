r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Autopilot
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Any, Dict, Optional
from twilio.base import deserialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class RestoreAssistantInstance(InstanceResource):

    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Assistant resource.
    :ivar sid: The unique string that we created to identify the Assistant resource.
    :ivar date_created: The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
    :ivar friendly_name: The string that you assigned to describe the resource. It is not unique and can be up to 255 characters long.
    :ivar needs_model_build: Whether model needs to be rebuilt.
    :ivar latest_model_build_sid: Reserved.
    :ivar log_queries: Whether queries should be logged and kept after training. Can be: `true` or `false` and defaults to `true`. If `true`, queries are stored for 30 days, and then deleted. If `false`, no queries are stored.
    :ivar development_stage: A string describing the state of the assistant.
    :ivar callback_url: Reserved.
    :ivar callback_events: Reserved.
    """

    def __init__(self, version: Version, payload: Dict[str, Any]):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.sid: Optional[str] = payload.get("sid")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.unique_name: Optional[str] = payload.get("unique_name")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.needs_model_build: Optional[bool] = payload.get("needs_model_build")
        self.latest_model_build_sid: Optional[str] = payload.get(
            "latest_model_build_sid"
        )
        self.log_queries: Optional[bool] = payload.get("log_queries")
        self.development_stage: Optional[str] = payload.get("development_stage")
        self.callback_url: Optional[str] = payload.get("callback_url")
        self.callback_events: Optional[str] = payload.get("callback_events")

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.Autopilot.V1.RestoreAssistantInstance>"


class RestoreAssistantList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the RestoreAssistantList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Assistants/Restore"

    def update(self, assistant) -> RestoreAssistantInstance:
        """
        Update the RestoreAssistantInstance

        :param str assistant: The Twilio-provided string that uniquely identifies the Assistant resource to restore.

        :returns: The created RestoreAssistantInstance
        """
        data = values.of(
            {
                "Assistant": assistant,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return RestoreAssistantInstance(self._version, payload)

    async def update_async(self, assistant) -> RestoreAssistantInstance:
        """
        Asynchronously update the RestoreAssistantInstance

        :param str assistant: The Twilio-provided string that uniquely identifies the Assistant resource to restore.

        :returns: The created RestoreAssistantInstance
        """
        data = values.of(
            {
                "Assistant": assistant,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return RestoreAssistantInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Autopilot.V1.RestoreAssistantList>"
