import unittest
from mock import Mock, DEFAULT, patch
from tests.tools import create_mock_json
from twilio.rest.v2010.account.conference import Participants, Participant


class ParticipantsTest(unittest.TestCase):

    def setUp(self):
        self.base_uri = "https://api.twilio.com/2010-04-01/Accounts/" \
                        "AC4bf2dafbed59a5733d2c1c1c69a83a28/Conferences" \
                        "/CFf2fe8498ed59a5733d2c1c1c69a83a28"

        self.call_sid = 'CAd31637cced59a5733d2c1c1c69a83a28'

        self.resource = Participants(self.base_uri, ("sid", "token"))

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_list(self, mock):
        resp = create_mock_json("tests/resources/participants_list.json")
        resp.status_code = 201
        mock.return_value = resp

        uri = "%s/Participants" % (self.base_uri)
        self.resource.list()
        mock.assert_called_with("GET", uri, params={}, auth=('sid', 'token'),
                                use_json_extension=True)

    @patch("twilio.rest.resources.base.Resource.request")
    def test_delete(self, mock):
        resp = Mock()
        resp.content = ""
        resp.status_code = 204
        mock.return_value = resp, {}

        r = Participant(self.resource, self.call_sid)
        r.delete()
        uri = '{}/Participants/{}'.format(self.base_uri, self.call_sid)
        mock.assert_called_with("DELETE", uri)

    @patch("twilio.rest.resources.base.Resource.request")
    def test_kick_alias(self, mock):
        resp = Mock()
        resp.content = ""
        resp.status_code = 204
        mock.return_value = resp, {}

        r = Participant(self.resource, self.call_sid)
        r.kick()
        uri = '{}/Participants/{}'.format(self.base_uri, self.call_sid)
        mock.assert_called_with("DELETE", uri)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_mute_alias(self, mock):
        resp = create_mock_json("tests/resources/participants_instance.json")
        resp.status_code = 201
        mock.return_value = resp

        uri = "{}/Participants/{}".format(self.base_uri, self.call_sid)
        p = Participant(self.resource, self.call_sid)
        p.mute()
        mock.assert_called_with("POST", uri, data={'Muted': 'true'}, auth=('sid', 'token'),
                                use_json_extension=True)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_unmute_alias(self, mock):
        resp = create_mock_json("tests/resources/participants_instance.json")
        resp.status_code = 201
        mock.return_value = resp

        uri = "{}/Participants/{}".format(self.base_uri, self.call_sid)
        p = Participant(self.resource, self.call_sid)
        p.unmute()
        mock.assert_called_with("POST", uri, data={'Muted': 'false'}, auth=('sid', 'token'),
                                use_json_extension=True)
