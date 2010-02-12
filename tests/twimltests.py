import unittest
import twilio
import re

class TwilioTest(unittest.TestCase):
    def strip(self, xml):
        return re.sub(r'\n|\t', '', str(xml).strip())
        
    def improperAppend(self, verb):
        self.assertRaises(twilio.TwilioException, verb.append, twilio.Say(""))
        self.assertRaises(twilio.TwilioException, verb.append, twilio.Gather())
        self.assertRaises(twilio.TwilioException, verb.append, twilio.Play(""))
        self.assertRaises(twilio.TwilioException, verb.append, twilio.Record())
        self.assertRaises(twilio.TwilioException, verb.append, twilio.Hangup())
        self.assertRaises(twilio.TwilioException, verb.append, twilio.Redirect())
        self.assertRaises(twilio.TwilioException, verb.append, twilio.Dial())
        self.assertRaises(twilio.TwilioException, verb.append, twilio.Conference(""))
        self.assertRaises(twilio.TwilioException, verb.append, twilio.Sms(""))
        self.assertRaises(twilio.TwilioException, verb.append, twilio.Pause())

class TestResponse(TwilioTest):
    
    def testEmptyResponse(self):
        r = twilio.Response()
        self.assertEquals(self.strip(r), "<Response/>")
    
    def testResponseAddAttribute(self):
        r = twilio.Response(foo="bar")
        self.assertEquals(self.strip(r), '<Response foo="bar"/>')
        
class TestSay(TwilioTest):

    def testEmptySay(self):
        """should be a say with no text"""
        r = twilio.Response()
        r.append(twilio.Say(""))
        self.assertEquals(self.strip(r), "<Response><Say/></Response>")

    def testSayHelloWorld(self):
        """should say hello monkey"""
        r = twilio.Response()
        r.append(twilio.Say("Hello World"))
        r = self.strip(r)
        self.assertEquals(r, "<Response><Say>Hello World</Say></Response>")
           
    def testSayLoop(self):
        """should say hello monkey and loop 3 times"""
        r = twilio.Response()
        r.append(twilio.Say("Hello Monkey", loop=3))
        r = self.strip(r)
        self.assertEquals(r, '<Response><Say loop="3">Hello Monkey</Say></Response>')
        
    def testSayLoopWoman(self):
        """should say have a woman say hello monkey and loop 3 times"""
        r = twilio.Response()
        r.append(twilio.Say("Hello Monkey", loop=3, voice=twilio.Say.WOMAN))
        r = self.strip(r)
        self.assertEquals(r, '<Response><Say loop="3" voice="woman">Hello Monkey</Say></Response>')
        
    def testSayConvienceMethod(self):
        """convenience method: should say have a woman say hello monkey and loop 3 times and be in french"""
        r = twilio.Response()
        r.addSay("Hello Monkey", loop=3, voice=twilio.Say.MAN, language=twilio.Say.FRENCH)
        r = self.strip(r)
        self.assertEquals(r, '<Response><Say language="fr" loop="3" voice="man">Hello Monkey</Say></Response>')
    
    def testSayAddAttribute(self):
        """add attribute"""
        r = twilio.Say("",foo="bar")
        r = self.strip(r)
        self.assertEquals(r, '<Say foo="bar"/>')
    
    def testSayBadAppend(self):
        """ should raise exceptions for wrong appending"""
        self.improperAppend(twilio.Say(""))
        
class TestPlay(TwilioTest):
    
    def testEmptyPlay(self):
        """should play hello monkey"""
        r = twilio.Response()
        r.append(twilio.Play(""))
        r = self.strip(r)
        self.assertEqual(r,"<Response><Play/></Response>")
    
    def testPlayHello(self):
        """should play hello monkey"""
        r = twilio.Response()
        r.append(twilio.Play("http://hellomonkey.mp3"))
        r = self.strip(r)
        self.assertEqual(r, "<Response><Play>http://hellomonkey.mp3</Play></Response>")
        
    def testPlayHelloLoop(self):
        """should play hello monkey loop"""
        r = twilio.Response()
        r.append(twilio.Play("http://hellomonkey.mp3", loop=3))
        r = self.strip(r)
        self.assertEqual(r, '<Response><Play loop="3">http://hellomonkey.mp3</Play></Response>')
        
    def testPlayConvienceMethod(self):
        """convenience method: should play hello monkey"""
        r = twilio.Response()
        r.addPlay("http://hellomonkey.mp3", loop=3)
        r = self.strip(r)
        self.assertEqual(r, '<Response><Play loop="3">http://hellomonkey.mp3</Play></Response>')
        
    def testPlayAddAttribute(self):
        """add attribute"""
        r = twilio.Play("",foo="bar")
        r = self.strip(r)
        self.assertEquals(r, '<Play foo="bar"/>')

    def testPlayBadAppend(self):
        """ should raise exceptions for wrong appending"""
        self.improperAppend(twilio.Play(""))
        
class TestRecord(TwilioTest):
    
    def testRecordEmpty(self):
        """should record"""
        r = twilio.Response()
        r.append(twilio.Record())
        r = self.strip(r)
        self.assertEquals(r, '<Response><Record/></Response>')
        
    def testRecordActionMethod(self):
        """should record with an action and a get method"""
        r = twilio.Response()
        r.append(twilio.Record(action="example.com", method="GET"))
        r = self.strip(r)
        self.assertEquals(r, '<Response><Record action="example.com" method="GET"/></Response>')
        
    def testRecordMaxlengthFinishTimeout(self):
        """should record with an maxlength, finishonkey, and timeout"""
        r = twilio.Response()
        r.append(twilio.Record(timeout=4,finishOnKey="#", maxLength=30))
        r = self.strip(r)
        self.assertEquals(r, '<Response><Record finishOnKey="#" maxLength="30" timeout="4"/></Response>')
        
    def testRecordTranscribeCallback(self):
        """should record with a transcribe and transcribeCallback"""
        r = twilio.Response()
        r.append(twilio.Record(transcribeCallback="example.com"))
        r = self.strip(r)
        self.assertEquals(r, '<Response><Record transcribeCallback="example.com"/></Response>')
    
    def testRecordMaxlengthFinishTimeout(self):
        """should record with an maxlength, finishonkey, and timeout"""
        r = twilio.Response()
        r.addRecord(timeout=4,finishOnKey="#", maxLength=30)
        r = self.strip(r)
        self.assertEquals(r, '<Response><Record finishOnKey="#" maxLength="30" timeout="4"/></Response>')

    def testPlayAddAttribute(self):
        """add attribute"""
        r = twilio.Record("",foo="bar")
        r = self.strip(r)
        self.assertEquals(r, '<Record foo="bar"/>')

    def testPlayBadAppend(self):
        """ should raise exceptions for wrong appending"""
        self.improperAppend(twilio.Record())
        
class TestRedirect(TwilioTest):
    
    def testRedirectEmpty(self):
        r = twilio.Response()
        r.append(twilio.Redirect())
        r = self.strip(r)
        self.assertEquals(r, '<Response><Redirect/></Response>')
        
    def testRedirectMethod(self):
        r = twilio.Response()
        r.append(twilio.Redirect(url="example.com", method="POST"))
        r = self.strip(r)
        self.assertEquals(r, '<Response><Redirect method="POST">example.com</Redirect></Response>')

    def testRedirectMethodGetParams(self):
        r = twilio.Response()
        r.append(twilio.Redirect(url="example.com?id=34&action=hey", method="POST"))
        r = self.strip(r)
        self.assertEquals(r, '<Response><Redirect method="POST">example.com?id=34&amp;action=hey</Redirect></Response>')
     
    def testAddAttribute(self):
        """add attribute"""
        r = twilio.Redirect("",foo="bar")
        r = self.strip(r)
        self.assertEquals(r, '<Redirect foo="bar"/>')

    def testBadAppend(self):
        """ should raise exceptions for wrong appending"""
        self.improperAppend(twilio.Redirect())
        
        
class TestHangup(TwilioTest):
    
    def testHangup(self):
        """convenience: should Hangup to a url via POST"""
        r = twilio.Response()
        r.append(twilio.Hangup())
        r = self.strip(r)
        self.assertEquals(r, '<Response><Hangup/></Response>')
        
        
    def testHangupConvience(self):
        """should raises exceptions for wrong appending"""
        r = twilio.Response()
        r.addHangup()
        r = self.strip(r)
        self.assertEquals(r, '<Response><Hangup/></Response>')

    def testBadAppend(self):
        """ should raise exceptions for wrong appending"""
        self.improperAppend(twilio.Hangup())
        
class TestSms(TwilioTest):
    
    def testEmpty(self):
        """Test empty sms verb"""
        r = twilio.Response()
        r.append(twilio.Sms(""))
        r = self.strip(r)
        self.assertEquals(r, '<Response><Sms/></Response>')
        
    def testBody(self):
        """Test hello world"""
        r = twilio.Response()
        r.append(twilio.Sms("Hello, World"))
        r = self.strip(r)
        self.assertEquals(r, '<Response><Sms>Hello, World</Sms></Response>')
        
    def testToFromAction(self):
        """ Test the to, from, and status callback"""
        r = twilio.Response()
        r.append(twilio.Sms("Hello, World", to=1231231234, sender=3453453456, 
            statusCallback="example.com?id=34&action=hey"))
        r = self.strip(r)
        self.assertEquals(r, '<Response><Sms from="3453453456" statusCallback="example.com?id=34&amp;action=hey" to="1231231234">Hello, World</Sms></Response>')
        
    def testActionMethod(self):
        """ Test the action and method parameters on Sms"""
        r = twilio.Response()
        r.append(twilio.Sms("Hello", method="POST", action="example.com?id=34&action=hey"))
        r = self.strip(r)
        self.assertEquals(r, '<Response><Sms action="example.com?id=34&amp;action=hey" method="POST">Hello</Sms></Response>')
        
    def testConvience(self):
        """should raises exceptions for wrong appending"""
        r = twilio.Response()
        r.addSms("Hello")
        r = self.strip(r)
        self.assertEquals(r, '<Response><Sms>Hello</Sms></Response>')

    def testBadAppend(self):
        """ should raise exceptions for wrong appending"""
        self.improperAppend(twilio.Sms("Hello"))
        
class TestDial(TwilioTest):
    
    def testDial(self):
        """ should redirect the call"""
        r = twilio.Response()
        r.append(twilio.Dial("1231231234"))
        r = self.strip(r)
        self.assertEquals(r, '<Response><Dial>1231231234</Dial></Response>')
        
    def testConvienceMethod(self):
        """ should dial to a url via post"""
        r = twilio.Response()
        r.addDial()
        r = self.strip(r)
        self.assertEquals(r, '<Response><Dial/></Response>')
        
    def testAddNumber(self):
        """add a number to a dial"""
        r = twilio.Response()
        d = twilio.Dial()
        d.append(twilio.Number("1231231234"))
        r.append(d)
        r = self.strip(r)
        self.assertEquals(r, '<Response><Dial><Number>1231231234</Number></Dial></Response>')
        
    def testAddNumberConvience(self):
        """add a number to a dial, convience method"""
        r = twilio.Response()
        d = r.addDial()
        d.addNumber("1231231234")
        r = self.strip(r)
        self.assertEquals(r, '<Response><Dial><Number>1231231234</Number></Dial></Response>')  
        
    def testAddConference(self):
        """ add a conference to a dial"""
        r = twilio.Response()
        d = twilio.Dial()
        d.append(twilio.Conference("My Room"))
        r.append(d)
        r = self.strip(r)
        self.assertEquals(r, '<Response><Dial><Conference>My Room</Conference></Dial></Response>')
        
    def testAddConferenceConvenceMethod(self):
        """ add a conference to a dial, conviently"""
        r = twilio.Response()
        d = r.addDial()
        d.addConference("My Room")
        r = self.strip(r)
        self.assertEquals(r, '<Response><Dial><Conference>My Room</Conference></Dial></Response>')   
        
    def testAddAttribute(self):
        """add attribute"""
        r = twilio.Conference("MyRoom",foo="bar")
        r = self.strip(r)
        self.assertEquals(r, '<Conference foo="bar">MyRoom</Conference>')
    
        
    def testBadAppend(self):
        """ should raise exceptions for wrong appending"""
        self.improperAppend(twilio.Conference("Hello"))
        
        
class TestGather(TwilioTest):
    
    def testEmpty(self):
        """ a gather with nothing inside"""
        r = twilio.Response()
        r.append(twilio.Gather())
        r = self.strip(r)
        self.assertEquals(r, '<Response><Gather/></Response>')
    
    def testNestedSayPlayPause(self):
        """ a gather with a say, play, and pause"""
        r = twilio.Response()
        g = twilio.Gather()
        g.append(twilio.Say("Hey"))
        g.append(twilio.Play("hey.mp3"))
        g.append(twilio.Pause())
        r.append(g)
        r = self.strip(r)
        self.assertEquals(r, '<Response><Gather><Say>Hey</Say><Play>hey.mp3</Play><Pause/></Gather></Response>')
        
        
    def testNestedSayPlayPauseConvience(self):
        """ a gather with a say, play, and pause"""
        r = twilio.Response()
        g = r.addGather()
        g.addSay("Hey")
        g.addPlay("hey.mp3")
        g.addPause()
        r = self.strip(r)
        self.assertEquals(r, '<Response><Gather><Say>Hey</Say><Play>hey.mp3</Play><Pause/></Gather></Response>')
        
    def testAddAttribute(self):
        """add attribute"""
        r = twilio.Gather(foo="bar")
        r = self.strip(r)
        self.assertEquals(r, '<Gather foo="bar"/>')
        
    def testImproperNesting(self):
        """ bad nesting"""
        verb = twilio.Gather()
        self.assertRaises(twilio.TwilioException, verb.append, twilio.Gather())
        self.assertRaises(twilio.TwilioException, verb.append, twilio.Record())
        self.assertRaises(twilio.TwilioException, verb.append, twilio.Hangup())
        self.assertRaises(twilio.TwilioException, verb.append, twilio.Redirect())
        self.assertRaises(twilio.TwilioException, verb.append, twilio.Dial())
        self.assertRaises(twilio.TwilioException, verb.append, twilio.Conference(""))
        self.assertRaises(twilio.TwilioException, verb.append, twilio.Sms(""))
    
if __name__ == '__main__':
    unittest.main()

