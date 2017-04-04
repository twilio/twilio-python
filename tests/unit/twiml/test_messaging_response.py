from nose.tools import assert_equal
from tests.unit.twiml import TwilioTest
from twilio.twiml.messaging_response import MessagingResponse, Body, Media


class TestResponse(TwilioTest):

    def test_empty_response(self):
        r = MessagingResponse()
        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response />'
        )

    def test_response(self):
        r = MessagingResponse()
        r.message('Hello')
        r.redirect(url='example.com')

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Message>Hello</Message><Redirect>example.com</Redirect></Response>'
        )

    def test_response_chain(self):
        r = MessagingResponse().message('Hello').redirect(url='example.com')

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Message>Hello</Message><Redirect>example.com</Redirect></Response>'
        )


class TestMessage(TwilioTest):

    def test_body(self):
        r = MessagingResponse()
        r.message('Hello')

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Message>Hello</Message></Response>'
        )

    def test_nested_body(self):
        b = Body('Hello World')

        r = MessagingResponse()
        r.append(b)

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Body>Hello World</Body></Response>'
        )

    def test_nested_body_media(self):
        b = Body('Hello World')
        m = Media('hey.jpg')

        r = MessagingResponse()
        r.append(b)
        r.append(m)

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Body>Hello World</Body><Media>hey.jpg</Media></Response>'
        )


class TestRedirect(TwilioTest):
    def test_redirect(self):
        r = MessagingResponse()
        r.redirect(url='example.com')

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Redirect>example.com</Redirect></Response>'
        )
