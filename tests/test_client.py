from twilio.rest import TwilioRestClient

def test_client_init():
    twilio = TwilioRestClient("AC123", "SECRET")
