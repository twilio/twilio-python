# -*- coding: utf-8 -*-
import re
import twilio
import unittest
from twilio import twiml
from twilio.twiml import TwimlException
from twilio.twiml import Response
import xml.etree.ElementTree as ET

class TwilioTest(unittest.TestCase):
    def strip(self, xml):
        return str(xml)

    def improperAppend(self, verb):
        self.assertRaises(TwimlException, verb.append, twiml.Say(""))
        self.assertRaises(TwimlException, verb.append, twiml.Gather())
        self.assertRaises(TwimlException, verb.append, twiml.Play(""))
        self.assertRaises(TwimlException, verb.append, twiml.Record())
        self.assertRaises(TwimlException, verb.append, twiml.Hangup())
        self.assertRaises(TwimlException, verb.append, twiml.Reject())
        self.assertRaises(TwimlException, verb.append, twiml.Redirect())
        self.assertRaises(TwimlException, verb.append, twiml.Dial())
        self.assertRaises(TwimlException, verb.append, twiml.Conference(""))
        self.assertRaises(TwimlException, verb.append, twiml.Sms(""))
        self.assertRaises(TwimlException, verb.append, twiml.Pause())

class TestResponse(TwilioTest):

    def testEmptyResponse(self):
        r = Response()
        self.assertEquals(self.strip(r), '<?xml version="1.0" encoding="UTF-8"?><Response />')

    def testResponseAddAttribute(self):
        r = Response(foo="bar")
        self.assertEquals(self.strip(r), '<?xml version="1.0" encoding="UTF-8"?><Response foo="bar" />')

class TestSay(TwilioTest):

    def testEmptySay(self):
        """should be a say with no text"""
        r = Response()
        r.append(twiml.Say(""))
        self.assertEquals(self.strip(r), '<?xml version="1.0" encoding="UTF-8"?><Response><Say /></Response>')

    def testSayHelloWorld(self):
        """should say hello monkey"""
        r = Response()
        r.append(twiml.Say("Hello World"))
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Response><Say>Hello World</Say></Response>')

    def testSayFrench(self):
        """should say hello monkey"""
        r = Response()
        r.append(twiml.Say(u"nécessaire et d'autres"))
        self.assertEquals(unicode(r),
                          '<?xml version="1.0" encoding="UTF-8"?><Response><Say>n&#233;cessaire et d\'autres</Say></Response>')

    def testSayLoop(self):
        """should say hello monkey and loop 3 times"""
        r = Response()
        r.append(twiml.Say("Hello Monkey", loop=3))
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Response><Say loop="3">Hello Monkey</Say></Response>')

    def testSayLoopGreatBritian(self):
        """should say have a woman say hello monkey and loop 3 times"""
        r = Response()
        r.append(twiml.Say("Hello Monkey", language="en-gb"))
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Response><Say language="en-gb">Hello Monkey</Say></Response>')

    def testSayLoopWoman(self):
        """should say have a woman say hello monkey and loop 3 times"""
        r = Response()
        r.append(twiml.Say("Hello Monkey", loop=3, voice=twiml.Say.WOMAN))
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Response><Say loop="3" voice="woman">Hello Monkey</Say></Response>')

    def testSayConvienceMethod(self):
        """convenience method: should say have a woman say hello monkey and loop 3 times and be in french"""
        r = Response()
        r.addSay("Hello Monkey", loop=3, voice=twiml.Say.MAN, language=twiml.Say.FRENCH)
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Response><Say language="fr" loop="3" voice="man">Hello Monkey</Say></Response>')

    def testSayAddAttribute(self):
        """add attribute"""
        r = twiml.Say("",foo="bar")
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Say foo="bar" />')

    def testSayBadAppend(self):
        """ should raise exceptions for wrong appending"""
        self.improperAppend(twiml.Say(""))

class TestPlay(TwilioTest):

    def testEmptyPlay(self):
        """should play hello monkey"""
        r = Response()
        r.append(twiml.Play(""))
        r = self.strip(r)
        self.assertEqual(r,'<?xml version="1.0" encoding="UTF-8"?><Response><Play /></Response>')

    def testPlayHello(self):
        """should play hello monkey"""
        r = Response()
        r.append(twiml.Play("http://hellomonkey.mp3"))
        r = self.strip(r)
        self.assertEqual(r, '<?xml version="1.0" encoding="UTF-8"?><Response><Play>http://hellomonkey.mp3</Play></Response>')

    def testPlayHelloLoop(self):
        """should play hello monkey loop"""
        r = Response()
        r.append(twiml.Play("http://hellomonkey.mp3", loop=3))
        r = self.strip(r)
        self.assertEqual(r, '<?xml version="1.0" encoding="UTF-8"?><Response><Play loop="3">http://hellomonkey.mp3</Play></Response>')

    def testPlayConvienceMethod(self):
        """convenience method: should play hello monkey"""
        r = Response()
        r.addPlay("http://hellomonkey.mp3", loop=3)
        r = self.strip(r)
        self.assertEqual(r, '<?xml version="1.0" encoding="UTF-8"?><Response><Play loop="3">http://hellomonkey.mp3</Play></Response>')

    def testPlayAddAttribute(self):
        """add attribute"""
        r = twiml.Play("",foo="bar")
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Play foo="bar" />')

    def testPlayBadAppend(self):
        """ should raise exceptions for wrong appending"""
        self.improperAppend(twiml.Play(""))

class TestRecord(TwilioTest):

    def testRecordEmpty(self):
        """should record"""
        r = Response()
        r.append(twiml.Record())
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Response><Record /></Response>')

    def testRecordActionMethod(self):
        """should record with an action and a get method"""
        r = Response()
        r.append(twiml.Record(action="example.com", method="GET"))
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Response><Record action="example.com" method="GET" /></Response>')

    def testRecordMaxlengthFinishTimeout(self):
        """should record with an maxlength, finishonkey, and timeout"""
        r = Response()
        r.append(twiml.Record(timeout=4,finishOnKey="#", maxLength=30))
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Response><Record finishOnKey="#" maxLength="30" timeout="4" /></Response>')

    def testRecordTranscribeCallback(self):
        """should record with a transcribe and transcribeCallback"""
        r = Response()
        r.append(twiml.Record(transcribeCallback="example.com"))
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Response><Record transcribeCallback="example.com" /></Response>')

    def testRecordMaxlengthFinishTimeout(self):
        """should record with an maxlength, finishonkey, and timeout"""
        r = Response()
        r.addRecord(timeout=4,finishOnKey="#", maxLength=30)
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Response><Record finishOnKey="#" maxLength="30" timeout="4" /></Response>')

    def testRecordAddAttribute(self):
        """add attribute"""
        r = twiml.Record(foo="bar")
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Record foo="bar" />')

    def testRecordBadAppend(self):
        """ should raise exceptions for wrong appending"""
        self.improperAppend(twiml.Record())

class TestRedirect(TwilioTest):

    def testRedirectEmpty(self):
        r = Response()
        r.append(twiml.Redirect())
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Response><Redirect /></Response>')

    def testRedirectMethod(self):
        r = Response()
        r.append(twiml.Redirect(url="example.com", method="POST"))
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Response><Redirect method="POST">example.com</Redirect></Response>')

    def testRedirectMethodGetParams(self):
        r = Response()
        r.append(twiml.Redirect(url="example.com?id=34&action=hey", method="POST"))
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Response><Redirect method="POST">example.com?id=34&amp;action=hey</Redirect></Response>')

    def testAddAttribute(self):
        """add attribute"""
        r = twiml.Redirect("",foo="bar")
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Redirect foo="bar" />')

    def testBadAppend(self):
        """ should raise exceptions for wrong appending"""
        self.improperAppend(twiml.Redirect())


class TestHangup(TwilioTest):

    def testHangup(self):
        """convenience: should Hangup to a url via POST"""
        r = Response()
        r.append(twiml.Hangup())
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Response><Hangup /></Response>')


    def testHangupConvience(self):
        """should raises exceptions for wrong appending"""
        r = Response()
        r.addHangup()
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Response><Hangup /></Response>')

    def testBadAppend(self):
        """ should raise exceptions for wrong appending"""
        self.improperAppend(twiml.Hangup())


class TestReject(TwilioTest):

    def testReject(self):
        """should be a Reject with default reason"""
        r = Response()
        r.append(twiml.Reject())
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Response><Reject /></Response>')

    def testRejectConvenience(self):
        """should be a Reject with reason Busy"""
        r = Response()
        r.addReject(reason='busy')
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Response><Reject reason="busy" /></Response>')

    def testBadAppend(self):
        """ should raise exceptions for wrong appending"""
        self.improperAppend(twiml.Reject())

class TestSms(TwilioTest):

    def testEmpty(self):
        """Test empty sms verb"""
        r = Response()
        r.append(twiml.Sms(""))
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Response><Sms /></Response>')

    def testBody(self):
        """Test hello world"""
        r = Response()
        r.append(twiml.Sms("Hello, World"))
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Response><Sms>Hello, World</Sms></Response>')

    def testToFromAction(self):
        """ Test the to, from, and status callback"""
        r = Response()
        r.append(twiml.Sms("Hello, World", to=1231231234, sender=3453453456,
            statusCallback="example.com?id=34&action=hey"))
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Response><Sms from="3453453456" statusCallback="example.com?id=34&amp;action=hey" to="1231231234">Hello, World</Sms></Response>')

    def testActionMethod(self):
        """ Test the action and method parameters on Sms"""
        r = Response()
        r.append(twiml.Sms("Hello", method="POST", action="example.com?id=34&action=hey"))
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Response><Sms action="example.com?id=34&amp;action=hey" method="POST">Hello</Sms></Response>')

    def testConvience(self):
        """should raises exceptions for wrong appending"""
        r = Response()
        r.addSms("Hello")
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Response><Sms>Hello</Sms></Response>')

    def testBadAppend(self):
        """ should raise exceptions for wrong appending"""
        self.improperAppend(twiml.Sms("Hello"))


class TestConference(TwilioTest):

    def setUp(self):
        r = Response()
        with r.dial() as dial:
            dial.conference("TestConferenceAttributes", beep=False, waitUrl="",
                startConferenceOnEnter=True, endConferenceOnExit=True)
        xml = r.toxml()

        #parse twiml XML string with Element Tree and inspect structure
        tree = ET.fromstring(xml)
        self.conf = tree.find(".//Dial/Conference")

    def test_conf_text(self):
        self.assertEqual(self.conf.text.strip(), "TestConferenceAttributes")

    def test_conf_beep(self):
        self.assertEqual(self.conf.get('beep'), "false")

    def test_conf_waiturl(self):
        self.assertEqual(self.conf.get('waitUrl'), "")

    def test_conf_start_conference(self):
        self.assertEqual(self.conf.get('startConferenceOnEnter'), "true")

    def test_conf_end_conference(self):
        self.assertEqual(self.conf.get('endConferenceOnExit'), "true")


class TestDial(TwilioTest):

    def testDial(self):
        """ should redirect the call"""
        r = Response()
        r.append(twiml.Dial("1231231234"))
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Response><Dial>1231231234</Dial></Response>')

    def testConvienceMethod(self):
        """ should dial to a url via post"""
        r = Response()
        r.addDial()
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Response><Dial /></Response>')

    def testAddNumber(self):
        """add a number to a dial"""
        r = Response()
        d = twiml.Dial()
        d.append(twiml.Number("1231231234"))
        r.append(d)
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Response><Dial><Number>1231231234</Number></Dial></Response>')

    def testAddNumberConvience(self):
        """add a number to a dial, convience method"""
        r = Response()
        d = r.addDial()
        d.addNumber("1231231234")
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Response><Dial><Number>1231231234</Number></Dial></Response>')

    def testAddConference(self):
        """ add a conference to a dial"""
        r = Response()
        d = twiml.Dial()
        d.append(twiml.Conference("My Room"))
        r.append(d)
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Response><Dial><Conference>My Room</Conference></Dial></Response>')

    def test_add_empty_client(self):
        """ add an empty client to a dial"""
        r = Response()
        d = r.dial()
        d.client("")
        self.assertEquals(str(r), '<?xml version="1.0" encoding="UTF-8"?><Response><Dial><Client /></Dial></Response>')

    def test_add_client(self):
        """ add a client to a dial"""
        r = Response()
        d = r.dial()
        d.client("alice")
        self.assertEquals(str(r), '<?xml version="1.0" encoding="UTF-8"?><Response><Dial><Client>alice</Client></Dial></Response>')

    def testAddConferenceConvenceMethod(self):
        """ add a conference to a dial, conviently"""
        r = Response()
        d = r.addDial()
        d.addConference("My Room")
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Response><Dial><Conference>My Room</Conference></Dial></Response>')

    def testAddAttribute(self):
        """add attribute"""
        r = twiml.Conference("MyRoom",foo="bar")
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Conference foo="bar">MyRoom</Conference>')


    def testBadAppend(self):
        """ should raise exceptions for wrong appending"""
        self.improperAppend(twiml.Conference("Hello"))


class TestGather(TwilioTest):

    def testEmpty(self):
        """ a gather with nothing inside"""
        r = Response()
        r.append(twiml.Gather())
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Response><Gather /></Response>')

    def test_context_manager(self):
        with Response() as r:
            with r.gather() as g:
                g.say("Hello")

            self.assertEquals(str(r), '<?xml version="1.0" encoding="UTF-8"?><Response><Gather><Say>Hello</Say></Gather></Response>')

    def testNestedSayPlayPause(self):
        """ a gather with a say, play, and pause"""
        r = Response()
        g = twiml.Gather()
        g.append(twiml.Say("Hey"))
        g.append(twiml.Play("hey.mp3"))
        g.append(twiml.Pause())
        r.append(g)
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Response><Gather><Say>Hey</Say><Play>hey.mp3</Play><Pause /></Gather></Response>')


    def testNestedSayPlayPauseConvience(self):
        """ a gather with a say, play, and pause"""
        r = Response()
        g = r.addGather()
        g.addSay("Hey")
        g.addPlay("hey.mp3")
        g.addPause()
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Response><Gather><Say>Hey</Say><Play>hey.mp3</Play><Pause /></Gather></Response>')

    def testAddAttribute(self):
        """add attribute"""
        r = twiml.Gather(foo="bar")
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="UTF-8"?><Gather foo="bar" />')

    def testNoDeclaration(self):
        """add attribute"""
        r = twiml.Gather(foo="bar")
        self.assertEquals(r.toxml(xml_declaration=False), '<Gather foo="bar" />')

    def testImproperNesting(self):
        """ bad nesting"""
        verb = twiml.Gather()
        self.assertRaises(TwimlException, verb.append, twiml.Gather())
        self.assertRaises(TwimlException, verb.append, twiml.Record())
        self.assertRaises(TwimlException, verb.append, twiml.Hangup())
        self.assertRaises(TwimlException, verb.append, twiml.Redirect())
        self.assertRaises(TwimlException, verb.append, twiml.Dial())
        self.assertRaises(TwimlException, verb.append, twiml.Conference(""))
        self.assertRaises(TwimlException, verb.append, twiml.Sms(""))

if __name__ == '__main__':
    unittest.main()
