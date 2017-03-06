# -*- coding: utf-8 -*-
from nose.tools import assert_equal
from six import u
from tests.unit.twiml import TwilioTest
from twilio.twiml.voice_response import VoiceResponse, Dial, Gather


class TestResponse(TwilioTest):

    def test_empty_response(self):
        r = VoiceResponse()
        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response />'
        )

    def test_response(self):
        r = VoiceResponse()
        r.hangup()
        r.leave()
        r.sms(
            'twilio sms',
            to='+11234567890',
            from_='+10987654321'
        )

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Hangup /><Leave /><Sms from="+10987654321" to="+11234567890">twilio sms</Sms></Response>'
        )

    def test_response_chain(self):
        r = VoiceResponse().hangup().leave().sms(
            'twilio sms',
            to='+11234567890',
            from_='+10987654321'
        )

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Hangup /><Leave /><Sms from="+10987654321" to="+11234567890">twilio sms</Sms></Response>'
        )


class TestSay(TwilioTest):

    def test_empty_say(self):
        """ should be a say with no text """
        r = VoiceResponse()
        r.say('')

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Say /></Response>'
        )

    def test_say_hello_world(self):
        """ should say hello world """
        r = VoiceResponse()
        r.say('Hello World')

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Say>Hello World</Say></Response>'
        )

    def test_say_french(self):
        """ should say hello monkey """
        r = VoiceResponse()
        r.say(u('n\xe9cessaire et d\'autres'))

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Say>n&#233;cessaire et d\'autres</Say></Response>'
        )

    def test_say_loop(self):
        """ should say hello monkey and loop 3 times """
        r = VoiceResponse()
        r.say('Hello Monkey', loop=3)

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Say loop="3">Hello Monkey</Say></Response>'
        )

    def test_say_loop_gb(self):
        """ should say have a woman say hello monkey and loop 3 times """
        r = VoiceResponse()
        r.say('Hello Monkey', language='en-gb')

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Say language="en-gb">Hello Monkey</Say></Response>'
        )

    def test_say_loop_woman(self):
        """ should say have a woman say hello monkey and loop 3 times """
        r = VoiceResponse()
        r.say('Hello Monkey', loop=3, voice='woman')

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Say loop="3" voice="woman">Hello Monkey</Say></Response>'
        )

    def test_say_all(self):
        """ convenience method: should say have a woman say hello monkey and loop 3 times and be in french """
        r = VoiceResponse()
        r.say('Hello Monkey', loop=3, voice='man', language='fr')

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Say language="fr" loop="3" voice="man">Hello Monkey</Say></Response>'
        )


class TestPlay(TwilioTest):

    def test_empty_play(self):
        """ should play hello monkey """
        r = VoiceResponse()
        r.play('')

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Play /></Response>'
        )

    def test_play_hello(self):
        """ should play hello monkey """
        r = VoiceResponse()
        r.play('http://hellomonkey.mp3')

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Play>http://hellomonkey.mp3</Play></Response>'
        )

    def test_play_hello_loop(self):
        """ should play hello monkey loop """
        r = VoiceResponse()
        r.play('http://hellomonkey.mp3', loop=3)

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Play loop="3">http://hellomonkey.mp3</Play></Response>'
        )

    def test_play_digits(self):
        """ should play digits """
        r = VoiceResponse()
        r.play('', digits='w123')

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Play digits="w123" /></Response>'
        )


class TestRecord(TwilioTest):

    def test_record_empty(self):
        """ should record """
        r = VoiceResponse()
        r.record()

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Record /></Response>'
        )

    def test_record_action_method(self):
        """ should record with an action and a get method """
        r = VoiceResponse()
        r.record(action='example.com', method='GET')

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Record action="example.com" method="GET" /></Response>'
        )

    def test_record_max_length_finish_timeout(self):
        """ should record with an maxLength, finishOnKey, and timeout """
        r = VoiceResponse()
        r.record(timeout=4, finish_on_key='#', max_length=30)

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Record finishOnKey="#" maxLength="30" timeout="4" /></Response>'
        )

    def test_record_transcribe(self):
        """ should record with a transcribe and transcribeCallback """
        r = VoiceResponse()
        r.record(transcribe_callback='example.com')

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Record transcribeCallback="example.com" /></Response>'
        )


class TestRedirect(TwilioTest):

    def test_redirect_empty(self):
        r = VoiceResponse()
        r.redirect('')

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Redirect /></Response>'
        )

    def test_redirect_method(self):
        r = VoiceResponse()
        r.redirect('example.com', method='POST')

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Redirect method="POST">example.com</Redirect></Response>'
        )

    def test_redirect_method_params(self):
        r = VoiceResponse()
        r.redirect('example.com?id=34&action=hey', method='POST')

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Redirect method="POST">example.com?id=34&amp;action=hey</Redirect></Response>'
        )


class TestHangup(TwilioTest):

    def test_hangup(self):
        """ convenience: should Hangup to a url via POST """
        r = VoiceResponse()
        r.hangup()

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Hangup /></Response>'
        )


class TestLeave(TwilioTest):

    def test_leave(self):
        """ convenience: should Hangup to a url via POST """
        r = VoiceResponse()
        r.leave()

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Leave /></Response>'
        )


class TestReject(TwilioTest):

    def test_reject(self):
        """ should be a Reject with default reason """
        r = VoiceResponse()
        r.reject()

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Reject /></Response>'
        )


class TestSms(TwilioTest):

    def test_empty(self):
        """ Test empty sms verb """
        r = VoiceResponse()
        r.sms('')

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Sms /></Response>'
        )

    def test_body(self):
        """ Test hello world """
        r = VoiceResponse()
        r.sms('Hello, World')

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Sms>Hello, World</Sms></Response>'
        )

    def test_to_from_action(self):
        """ Test the to, from, and status callback """
        r = VoiceResponse()
        r.sms('Hello, World', to=1231231234, from_=3453453456, status_callback='example.com?id=34&action=hey')

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Sms from="3453453456" statusCallback="example.com?id=34&amp;action=hey" to="1231231234">Hello, World</Sms></Response>'
        )

    def test_action_method(self):
        """ Test the action and method parameters on Sms """
        r = VoiceResponse()
        r.sms('Hello', method='POST', action='example.com?id=34&action=hey')

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Sms action="example.com?id=34&amp;action=hey" method="POST">Hello</Sms></Response>'
        )


class TestConference(TwilioTest):

    def test_conference(self):
        d = Dial()
        d.conference(
            'TestConferenceAttributes',
            beep=False,
            wait_url='',
            start_conference_on_enter=True,
            end_conference_on_exit=True
        )

        r = VoiceResponse()
        r.append(d)

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Dial><Conference beep="false" endConferenceOnExit="true" startConferenceOnEnter="true" waitUrl="">TestConferenceAttributes</Conference></Dial></Response>'
        )


class TestQueue(TwilioTest):

    def test_queue(self):
        d = Dial()
        d.queue('TestQueueAttribute', url='', method='GET')

        r = VoiceResponse()
        r.append(d)

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Dial><Queue method="GET" url="">TestQueueAttribute</Queue></Dial></Response>'
        )


class TestEnqueue(TwilioTest):

    def test_enqueue(self):
        r = VoiceResponse()
        r.enqueue(
            'TestEnqueueAttribute',
            action='act',
            method='GET',
            wait_url='wait',
            wait_url_method='POST'
        )

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Enqueue action="act" method="GET" waitUrl="wait" waitUrlMethod="POST">TestEnqueueAttribute</Enqueue></Response>'
        )


class TestDial(TwilioTest):

    def test_dial(self):
        """ should redirect the call """
        r = VoiceResponse()
        r.dial("1231231234")

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Dial>1231231234</Dial></Response>'
        )

    def test_sip(self):
        """ should redirect the call """
        d = Dial()
        d.sip('foo@example.com')

        r = VoiceResponse()
        r.append(d)

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Dial><Sip>foo@example.com</Sip></Dial></Response>'
        )

    def test_sip_username_password(self):
        """ should redirect the call """
        d = Dial()
        d.sip('foo@example.com', username='foo', password='bar')

        r = VoiceResponse()
        r.append(d)

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Dial><Sip password="bar" username="foo">foo@example.com</Sip></Dial></Response>'
        )

    def test_add_number(self):
        """ add a number to a dial """
        d = Dial()
        d.number('1231231234')

        r = VoiceResponse()
        r.append(d)

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Dial><Number>1231231234</Number></Dial></Response>'
        )

    def test_add_number_status_callback_event(self):
        """ add a number to a dial with status callback events"""
        d = Dial()
        d.number('1231231234', status_callback='http://example.com', status_callback_event='initiated completed')

        r = VoiceResponse()
        r.append(d)

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Dial><Number statusCallback="http://example.com" statusCallbackEvent="initiated completed">1231231234</Number></Dial></Response>'
        )

    def test_add_conference(self):
        """ add a conference to a dial """
        d = Dial()
        d.conference('My Room')

        r = VoiceResponse()
        r.append(d)

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Dial><Conference>My Room</Conference></Dial></Response>'
        )

    def test_add_queue(self):
        """ add a queue to a dial """
        d = Dial()
        d.queue('The Cute Queue')

        r = VoiceResponse()
        r.append(d)

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Dial><Queue>The Cute Queue</Queue></Dial></Response>'
        )

    def test_add_empty_client(self):
        """ add an empty client to a dial """
        d = Dial()
        d.client('')

        r = VoiceResponse()
        r.append(d)

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Dial><Client /></Dial></Response>'
        )

    def test_add_client(self):
        """ add a client to a dial """
        d = Dial()
        d.client('alice')

        r = VoiceResponse()
        r.append(d)

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Dial><Client>alice</Client></Dial></Response>'
        )


class TestGather(TwilioTest):

    def test_empty(self):
        """ a gather with nothing inside """
        r = VoiceResponse()
        r.gather()

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Gather /></Response>'
        )

    def test_gather_say(self):
        g = Gather()
        g.say('Hello')

        r = VoiceResponse()
        r.append(g)

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Gather><Say>Hello</Say></Gather></Response>'
        )

    def test_nested_say_play_pause(self):
        """ a gather with a say, play, and pause """
        g = Gather()
        g.say('Hey')
        g.play('hey.mp3')
        g.pause()

        r = VoiceResponse()
        r.append(g)

        assert_equal(
            self.strip(r),
            '<?xml version="1.0" encoding="UTF-8"?><Response><Gather><Say>Hey</Say><Play>hey.mp3</Play><Pause /></Gather></Response>'
        )
