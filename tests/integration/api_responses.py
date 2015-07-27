import os
from . import config
from mock import Mock
from twilio.rest.resources.base import Response


class RequestHandler(object):
    def __init__(self, method, uri,
                 auth=(config.account_sid, config.auth_token),
                 status=200,
                 response_data=None,
                 data=None,
                 params=None,
                 use_json_extension=True):
        self.method = method
        self.uri = uri
        self.url = '%s/%s%s.json' % (config.base_uri, config.version, uri)
        self.auth = auth
        self.data = data
        self.params = params
        self.response = Response(Mock(status=status), response_data, self.url)

    def can_respond_to(self, request):
        return self.method == request.method \
               and self.url == request.url \
               and self.auth == request.auth \
               and self.data == request.data \
               and self.params == request.params

    def load_file(self, filename):
        with open(os.path.join('tests', 'resources', filename)) as f:
            return f.read()


class GETRequestHandler(RequestHandler):
    def __init__(self, uri,
                 response_file,
                 params={},
                 auth=(config.account_sid, config.auth_token)):
        super(GETRequestHandler, self).__init__('GET', uri, params=params, auth=auth,
                                                response_data=self.load_file(response_file))


class POSTRequestHandler(RequestHandler):
    def __init__(self, uri, response_file,
                 data={}, auth=(config.account_sid, config.auth_token)):
        super(POSTRequestHandler, self).__init__('POST', uri, data=data, auth=auth,
                                                 response_data=self.load_file(response_file))


class TwilioRequest(object):
    def __init__(self, method, url, auth=(None, None),
                 headers=None, data=None, params=None, use_json_extension=None):
        self.method = method
        self.url = url
        self.auth = auth
        self.data = data
        self.params = params
        self.use_json_extension = use_json_extension

GRH = GETRequestHandler
PRH = POSTRequestHandler

RESPONSE_HANDLERS = [
    GRH('/Accounts', 'accounts_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28', 'accounts_instance.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Calls', 'calls_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Calls'
        '/CA24388be8ed59a5733d2c1c1c69a83a28/Notifications',
        'notifications_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Calls'
        '/CA24388be8ed59a5733d2c1c1c69a83a28/Recordings',
        'recordings_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Conferences',
        'conferences_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/IncomingPhoneNumbers',
        'incoming_phone_numbers_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Messages',
        'messages_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Notifications',
        'notifications_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/OutgoingCallerIds',
        'outgoing_caller_ids_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Queues',
        'queues_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Queues/QU1b9faddec3d54ec18488f86c83019bf0/Members',
        'members_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Recordings',
        'recordings_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/SIP/Domains',
        os.path.join('sip', 'sip_domain_list.json')),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/SIP/CredentialLists',
        os.path.join('sip', 'sip_credential_list_list.json')),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/'
        'SIP/CredentialLists/CL1e9949149f055138a8c215fb7ccd5b64/Credentials',
        os.path.join('sip', 'sip_credential_list.json')),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/SIP/IpAccessControlLists',
        os.path.join('sip', 'sip_ip_access_control_list_list.json')),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/SMS/Messages',
        'sms_messages_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/SMS/ShortCodes',
        'sms_short_codes_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Transcriptions',
        'transcriptions_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Usage/Records',
        'usage_records_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Usage/Records/Daily',
        'usage_records_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Usage/Records/LastMonth',
        'usage_records_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Usage/Records/Monthly',
        'usage_records_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Usage/Records/ThisMonth',
        'usage_records_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Usage/Records/Today',
        'usage_records_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Usage/Triggers',
        'usage_triggers_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/AuthorizedConnectApps',
        'authorized_connect_apps.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Applications',
        'applications_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Conferences'
        '/CFf2fe8498ed59a5733d2c1c1c69a83a28/Participants',
        'participants_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/ConnectApps',
        'connect_apps_list.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/AvailablePhoneNumbers/US/Local',
        'available_phone_numbers_us_local.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/AvailablePhoneNumbers/US/Mobile',
        'available_phone_numbers_us_local.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/AvailablePhoneNumbers/US/TollFree',
        'available_phone_numbers_us_tollfree.json'),
    GRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/AvailablePhoneNumbers/CA/Local',
        'available_phone_numbers_ca_local.json'),
    PRH('/Accounts/AC4bf2dafbed59a5733d2c1c1c69a83a28/Tokens',
        'tokens.json', {'Ttl': 30})
]
