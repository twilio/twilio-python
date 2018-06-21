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
        with MessagingResponse() as r:
            r.message('Hello')
            r.redirect(url='example.com')

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Message>Hello</Message><Redirect>example.com</Redirect></Response>'
        )

    def test_nested_verbs(self):
        with MessagingResponse() as r:
            with r.message('Hello') as m:
                m.media('example.com')

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Message>Hello<Media>example.com</Media></Message></Response>'
        )

    def test_child_node(self):
        with MessagingResponse() as r:
            with r.add_child('message', tag='global') as mod:
                mod.add_child('bold', 'Hello')

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><message tag="global"><bold>Hello</bold></message></Response>')

    def test_mixed(self):
        r = MessagingResponse()

        r.append('before')
        r.add_child('Child').append('content')
        r.append('after')

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response>before<Child>content</Child>after</Response>'
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


class TestText(TwilioTest):
    def test_text(self):
        r = MessagingResponse()
        r.append('No tags!')

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response>No tags!</Response>'
        )

    def text_mixed(self):
        r = MessagingResponse()
        r.append('before')
        r.append(Body('Content'))
        r.append('after')

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response>before<Body>Content</Body>after</Response>'
        )
