import unittest
from mock import Mock, patch
from tests.tools import create_mock_json
from twilio.rest.http import HttpClient
from twilio.rest.v2010.account.conference import Participants, Participant


class ParticipantsTest(unittest.TestCase):

    def setUp(self):
        self.client = HttpClient()
        self.base_uri = "https://api.twilio.com/2010-04-01/Accounts/" \
                        "AC4bf2dafbed59a5733d2c1c1c69a83a28/Conferences" \
                        "/CFf2fe8498ed59a5733d2c1c1c69a83a28"

        self.call_sid = 'CAd31637cced59a5733d2c1c1c69a83a28'

        self.auth = ("sid", "token")
        self.resource = Participants(self.client, self.base_uri, self.auth)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_list(self, mock):
        resp = create_mock_json("tests/resources/participants_list.json")
        resp.status_code = 201
        mock.return_value = resp

        uri = "%s/Participants" % (self.base_uri)
        self.resource.list().execute()
        mock.assert_called_with("GET", uri, auth=self.auth,
                                use_json_extension=True,
                                client=self.client)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_delete(self, mock):
        resp = Mock()
        resp.content = ""
        resp.status_code = 204
        mock.return_value = resp

        r = Participant(self.resource, self.call_sid)
        r.delete().execute()
        uri = '{}/Participants/{}'.format(self.base_uri, self.call_sid)
        mock.assert_called_with("DELETE", uri, auth=self.auth,
                                use_json_extension=True,
                                client=self.client)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_kick_alias(self, mock):
        resp = Mock()
        resp.content = ""
        resp.status_code = 204
        mock.return_value = resp

        r = Participant(self.resource, self.call_sid)
        r.kick().execute()
        uri = '{}/Participants/{}'.format(self.base_uri, self.call_sid)

        mock.assert_called_with("DELETE", uri, auth=self.auth,
                                use_json_extension=True,
                                client=self.client)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_mute_alias(self, mock):
        resp = create_mock_json("tests/resources/participants_instance.json")
        resp.status_code = 201
        mock.return_value = resp

        uri = "{}/Participants/{}".format(self.base_uri, self.call_sid)
        p = Participant(self.resource, self.call_sid)
        p.mute().execute()
        mock.assert_called_with("POST", uri, data={'Muted': 'true'}, auth=('sid', 'token'),
                                use_json_extension=True,
                                client=self.client)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_unmute_alias(self, mock):
        resp = create_mock_json("tests/resources/participants_instance.json")
        resp.status_code = 201
        mock.return_value = resp

        uri = "{}/Participants/{}".format(self.base_uri, self.call_sid)
        p = Participant(self.resource, self.call_sid)
        p.unmute().execute()
        mock.assert_called_with("POST", uri, data={'Muted': 'false'}, auth=('sid', 'token'),
                                use_json_extension=True,
                                client=self.client)
