"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Events
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from twilio.base.version import Version
from twilio.base.domain import Domain
from twilio.rest.events.v1.event_type import EventTypeList
from twilio.rest.events.v1.schema import SchemaList
from twilio.rest.events.v1.sink import SinkList
from twilio.rest.events.v1.subscription import SubscriptionList


class V1(Version):

    def __init__(self, domain: Domain):
        """
        Initialize the V1 version of Events

        :param domain: The Twilio.events domain
        """
        super().__init__(domain)
        self.version = 'v1'
        self._event_types = None
        self._schemas = None
        self._sinks = None
        self._subscriptions = None
        
    @property
    def event_types(self) -> EventTypeList:
        """
        :rtype: twilio.rest.events.v1.event_type.EventTypeList
        """
        if self._event_types is None:
            self._event_types = EventTypeList(self)
        return self._event_types

    @property
    def schemas(self) -> SchemaList:
        """
        :rtype: twilio.rest.events.v1.schema.SchemaList
        """
        if self._schemas is None:
            self._schemas = SchemaList(self)
        return self._schemas

    @property
    def sinks(self) -> SinkList:
        """
        :rtype: twilio.rest.events.v1.sink.SinkList
        """
        if self._sinks is None:
            self._sinks = SinkList(self)
        return self._sinks

    @property
    def subscriptions(self) -> SubscriptionList:
        """
        :rtype: twilio.rest.events.v1.subscription.SubscriptionList
        """
        if self._subscriptions is None:
            self._subscriptions = SubscriptionList(self)
        return self._subscriptions

    def __repr__(self) -> str:
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Events.V1>'
