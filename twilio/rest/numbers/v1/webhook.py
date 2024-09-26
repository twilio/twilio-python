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

from datetime import datetime
from typing import Any, Dict, List, Optional
from twilio.base import deserialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class WebhookInstance(InstanceResource):
    """
    :ivar url: The URL of the webhook configuration request
    :ivar port_in_target_url: The complete webhook url that will be called when a notification event for port in request or port in phone number happens
    :ivar port_out_target_url: The complete webhook url that will be called when a notification event for a port out phone number happens.
    :ivar notifications_of: A list to filter what notification events to receive for this account and its sub accounts. If it is an empty list, then it means that there are no filters for the notifications events to send in each webhook and all events will get sent.
    :ivar port_in_target_date_created: Creation date for the port in webhook configuration
    :ivar port_out_target_date_created: Creation date for the port out webhook configuration
    """

    def __init__(self, version: Version, payload: Dict[str, Any]):
        super().__init__(version)

        self.url: Optional[str] = payload.get("url")
        self.port_in_target_url: Optional[str] = payload.get("port_in_target_url")
        self.port_out_target_url: Optional[str] = payload.get("port_out_target_url")
        self.notifications_of: Optional[List[str]] = payload.get("notifications_of")
        self.port_in_target_date_created: Optional[datetime] = (
            deserialize.iso8601_datetime(payload.get("port_in_target_date_created"))
        )
        self.port_out_target_date_created: Optional[datetime] = (
            deserialize.iso8601_datetime(payload.get("port_out_target_date_created"))
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.Numbers.V1.WebhookInstance>"


class WebhookList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the WebhookList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Porting/Configuration/Webhook"

    def fetch(self) -> WebhookInstance:
        """
        Asynchronously fetch the WebhookInstance


        :returns: The fetched WebhookInstance
        """
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = self._version.fetch(method="GET", uri=self._uri, headers=headers)

        return WebhookInstance(self._version, payload)

    async def fetch_async(self) -> WebhookInstance:
        """
        Asynchronously fetch the WebhookInstance


        :returns: The fetched WebhookInstance
        """
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = await self._version.fetch_async(
            method="GET", uri=self._uri, headers=headers
        )

        return WebhookInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Numbers.V1.WebhookList>"
