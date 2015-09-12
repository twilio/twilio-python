# coding=utf-8
"""
__  __                      __
\ \/ /___  __  ______  ____/ /_  ______  ___
 \  / __ \/ / / / __ \/ __  / / / / __ \/ _ \
 / / /_/ / /_/ / /_/ / /_/ / /_/ / / / /  __/
/_/\____/\__. /\____/\__._/\__. /_/ /_/\___/      version 0.0.1
        /____/            /____/
"""

from twilio.rest.resources.util import UNSET_TIMEOUT
from twilio.rest.v2010.account.sms.sms_message import (
    SmsMessage,
    SmsMessages,
)
from twilio.rest.v2010.account.sms.short_code import (
    ShortCode,
    ShortCodes,
)


class Sms(object):
    """ Holds all specific Sms list resources """
    key = "sms"

    def __init__(self, client, base_uri, auth, timeout=UNSET_TIMEOUT):
        self.timeout = timeout
        self.client = client
        self.messages = SmsMessages(client, base_uri, auth, timeout)
        self.short_codes = ShortCodes(client, base_uri, auth, timeout)
