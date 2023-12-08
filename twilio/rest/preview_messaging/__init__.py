from twilio.rest.preview_messaging.PreviewMessagingBase import PreviewMessagingBase
from twilio.rest.preview_messaging.v1.broadcast import BroadcastList
from twilio.rest.preview_messaging.v1.message import MessageList


class PreviewMessaging(PreviewMessagingBase):
    @property
    def broadcast(self) -> BroadcastList:
        return self.v1.broadcasts

    @property
    def messages(self) -> MessageList:
        return self.v1.messages
