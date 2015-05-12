from twilio.rest.base import TwilioClient
from twilio.rest.resources import UNSET_TIMEOUT
from twilio.rest.resources.conversations.conversations import ConversationsRoot


class TwilioConversationsClient(TwilioClient):
    """
    A client for accessing the Twilio Conversations API.

    XXX more verbiage here

    :param str account: Your Account Sid from `your dashboard
        <https://www.twilio.com/user/account>`_
    :param str token: Your Auth Token from `your dashboard
        <https://www.twilio.com/user/account>`_
    :param float timeout: The socket and read timeout for requests to Twilio
    """

    def __init__(self, account=None, token=None,
                 base="https://conversations.twilio.com", version="v1",
                 timeout=UNSET_TIMEOUT):

        super(TwilioConversationsClient, self).__init__(account, token, base,
                                                        version, timeout)

        self.version_uri = "%s/%s" % (base, version)
        self.conversations = ConversationsRoot(self.version_uri, self.auth,
                                               timeout)
