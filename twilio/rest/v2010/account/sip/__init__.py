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
from twilio.rest.v2010.account.sip.domain import (
    Domain,
    Domains,
)
from twilio.rest.v2010.account.sip.ip_access_control_list import (
    IpAccessControlList,
    IpAccessControlLists,
)
from twilio.rest.v2010.account.sip.credential_list import (
    CredentialList,
    CredentialLists,
)


class Sip(object):
    """ Holds all specific Sip list resources """
    key = "sip"

    def __init__(self, client, base_uri, auth, timeout=UNSET_TIMEOUT):
        self.timeout = timeout
        self.client = client
        self.domains = Domains(client, base_uri, auth, timeout)
        self.ip_access_control_lists = IpAccessControlLists(client, base_uri, auth, timeout)
        self.credential_lists = CredentialLists(client, base_uri, auth, timeout)
