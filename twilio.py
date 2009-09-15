"""
Copyright (c) 2009 Twilio, Inc.

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
"""

__VERSION__ = "2.0.0"

import urllib, urllib2, base64, hmac
from hashlib import sha1
from xml.sax.saxutils import escape, quoteattr

try:
    from google.appengine.api import urlfetch
    APPENGINE = True
except:
    APPENGINE = False

_TWILIO_API_URL = 'https://api.twilio.com'

class TwilioException(Exception): pass

# Twilio REST Helpers
# ===========================================================================

class HTTPErrorProcessor(urllib2.HTTPErrorProcessor):
    def https_response(self, request, response):
        code, msg, hdrs = response.code, response.msg, response.info()
        if code >= 300:
            response = self.parent.error(
                'http', request, response, code, msg, hdrs)
        return response

class HTTPErrorAppEngine(Exception): pass

class TwilioUrlRequest(urllib2.Request):
    def get_method(self):
        if getattr(self, 'http_method', None):
            return self.http_method
        return urllib2.Request.get_method(self)

class Account:
    """Twilio account object that provides helper functions for making
    REST requests to the Twilio API.  This helper library works both in
    standalone python applications using the urllib/urlib2 libraries and
    inside Google App Engine applications using urlfetch.
    """
    def __init__(self, id, token):
        """initialize a twilio account object
        
        id: Twilio account SID/ID
        token: Twilio account token
        
        returns a Twilio account object
        """
        self.id = id
        self.token = token
        self.opener = None
    
    def _build_get_uri(self, uri, params):
        if params and len(params) > 0:
            if uri.find('?') > 0:
                if uri[-1] != '&':
                    uri += '&'
                uri = uri + urllib.urlencode(params)
            else:
                uri = uri + '?' + urllib.urlencode(params)
        return uri
    
    def _urllib2_fetch(self, uri, params, method=None):
        # install error processor to handle HTTP 201 response correctly
        if self.opener == None:
            self.opener = urllib2.build_opener(HTTPErrorProcessor)
            urllib2.install_opener(self.opener)
        
        if method and method == 'GET':
            uri = self._build_get_uri(uri, params)
            req = TwilioUrlRequest(uri)
        else:
            req = TwilioUrlRequest(uri, urllib.urlencode(params))
            if method and (method == 'DELETE' or method == 'PUT'):
                req.http_method = method
        
        authstring = base64.encodestring('%s:%s' % (self.id, self.token))
        authstring = authstring.replace('\n', '')
        req.add_header("Authorization", "Basic %s" % authstring)
        
        response = urllib2.urlopen(req)
        return response.read()
    
    def _appengine_fetch(self, uri, params, method):
        if method == 'GET':
            uri = self._build_get_uri(uri, params)
        
        try:
            httpmethod = getattr(urlfetch, method)
        except AttributeError:
            raise NotImplementedError(
                "Google App Engine does not support method '%s'" % method)
        
        authstring = base64.encodestring('%s:%s' % (self.id, self.token))
        authstring = authstring.replace('\n', '')
        r = urlfetch.fetch(url=uri, payload=urllib.urlencode(params),
            method=httpmethod,
            headers={'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': 'Basic %s' % authstring})
        if r.status_code >= 300:
            raise HTTPErrorAppEngine("HTTP %s: %s" % \
                (r.status_code, r.content))
        return r.content
    
    def request(self, path, method=None, vars={}):
        """sends a request and gets a response from the Twilio REST API
        
        path: the URL (relative to the endpoint URL, after the /v1
        url: the HTTP method to use, defaults to POST
        vars: for POST or PUT, a dict of data to send
        
        returns Twilio response in XML or raises an exception on error
        """
        if not path or len(path) < 1:
            raise ValueError('Invalid path parameter')
        if method and method not in ['GET', 'POST', 'DELETE', 'PUT']:
            raise NotImplementedError(
                'HTTP %s method not implemented' % method)
        
        if path[0] == '/':
            uri = _TWILIO_API_URL + path
        else:
            uri = _TWILIO_API_URL + '/' + path
        
        if APPENGINE:
            return self._appengine_fetch(uri, vars, method)
        return self._urllib2_fetch(uri, vars, method)

# TwiML Response Helpers
# ===========================================================================

class Verb:
    """Twilio basic verb object.
    """
    def __init__(self, **kwargs):
        self.name = self.__class__.__name__
        self.body = None
        self.nestables = None
        
        self.verbs = []
        self.attrs = {}
        for k, v in kwargs.items():
            if v: self.attrs[k] = quoteattr(str(v))
    
    def __repr__(self):
        s = '<%s' % self.name
        for a in self.attrs:
            s += ' %s=%s' % (a, self.attrs[a])
        if self.body or len(self.verbs) > 0:
            s += '>'
            if self.body:
                s += escape(self.body)
            if len(self.verbs) > 0:
                s += '\n'
                for v in self.verbs:
                    for l in str(v)[:-1].split('\n'):
                        s += "\t%s\n" % l
            s += '</%s>\n' % self.name
        else:
            s += '/>\n'
        return s
    
    def append(self, verb):
        if not self.nestables:
            raise TwilioException("%s is not nestable" % self.name)
        if verb.name not in self.nestables:
            raise TwilioException("%s is not nestable inside %s" % \
                (verb.name, self.name))
        self.verbs.append(verb)
        return verb
    
    def asUrl(self):
        return urllib.quote(str(self))
    
    def addSay(self, text, **kwargs):
        return self.append(Say(text, **kwargs))
    
    def addPlay(self, url, **kwargs):
        return self.append(Play(url, **kwargs))
    
    def addPause(self, **kwargs):
        return self.append(Pause(**kwargs))
    
    def addRedirect(self, url=None, **kwargs):
        return self.append(Redirect(url, **kwargs))   
    
    def addHangup(self, **kwargs):
        return self.append(Hangup(**kwargs)) 
    
    def addGather(self, **kwargs):
        return self.append(Gather(**kwargs))
    
    def addNumber(self, number, **kwargs):
        return self.append(Number(number, **kwargs))
    
    def addDial(self, number=None, **kwargs):
        return self.append(Dial(number, **kwargs))
    
    def addRecord(self, **kwargs):
        return self.append(Record(**kwargs))

class Response(Verb):
    """Twilio response object.
    
    version: Twilio API version e.g. 2008-08-01
    """
    def __init__(self, version=None, **kwargs):
        Verb.__init__(self, version=version, **kwargs)
        self.nestables = ['Say', 'Play', 'Gather', 'Record', 'Dial',
            'Redirect', 'Pause', 'Hangup']

class Say(Verb):
    """Say text
    
    text: text to say
    voice: MAN or WOMAN
    language: language to use
    loop: number of times to say this text
    """
    MAN = 'man'
    WOMAN = 'woman'
    
    ENGLISH = 'en'
    SPANISH = 'es'
    FRENCH = 'fr'
    GERMAN = 'de'
    
    def __init__(self, text, voice=None, language=None, loop=None, **kwargs):
        Verb.__init__(self, voice=voice, language=language, loop=loop,
            **kwargs)
        self.body = text
        if voice and (voice != self.MAN and voice != self.WOMAN):
            raise TwilioException( \
                "Invalid Say voice parameter, must be 'man' or 'woman'")
        if voice and (voice != self.MAN and voice != self.WOMAN):
            raise TwilioException( \
                "Invalid Say language parameter, must be " + \
                "'en', 'es', 'fr', or 'de'")

class Play(Verb):
    """Play audio file at a URL
    
    url: url of audio file, MIME type on file must be set correctly
    loop: number of time to say this text
    """
    def __init__(self, url, loop=None, **kwargs):
        Verb.__init__(self, loop=loop, **kwargs)
        self.body = url

class Pause(Verb):
    """Pause the call
    
    length: length of pause in seconds
    """
    def __init__(self, length=None, **kwargs):
        Verb.__init__(self, length=length, **kwargs)

class Redirect(Verb):
    """Redirect call flow to another URL
    
    url: redirect url
    """
    def __init__(self, url=None, **kwargs):
        Verb.__init__(self, **kwargs)
        self.body = url

class Hangup(Verb):
    """Hangup the call
    """
    def __init__(self, **kwargs):
        Verb.__init__(self)

class Gather(Verb):
    """Gather digits from the caller's keypad
    
    action: URL to which the digits entered will be sent
    method: submit to 'action' url using GET or POST
    numDigits: how many digits to gather before returning
    timeout: wait for this many seconds before returning
    finishOnKey: key that triggers the end of caller input
    """
    GET = 'GET'
    POST = 'POST'

    def __init__(self, action=None, method=None, numDigits=None, timeout=None,
        finishOnKey=None, **kwargs):
        
        Verb.__init__(self, action=action, method=method,
            numDigits=numDigits, timeout=timeout, finishOnKey=finishOnKey,
            **kwargs)
        if method and (method != self.GET and method != self.POST):
            raise TwilioException( \
                "Invalid method parameter, must be 'GET' or 'POST'")
        self.nestables = ['Say', 'Play', 'Pause']

class Number(Verb):
    """Specify phone number in a nested Dial element.
    
    sendDigits: key to press after connecting to the number
    """
    def __init__(self, number, sendDigits=None, **kwargs):
        Verb.__init__(self, sendDigits=sendDigits, **kwargs)
        self.body = number

class Dial(Verb):
    """Dial another phone number and connect it to this call
    
    action: submit the result of the dial to this URL
    method: submit to 'action' url using GET or POST
    """
    GET = 'GET'
    POST = 'POST'
    
    def __init__(self, number=None, action=None, method=None, **kwargs):
        Verb.__init__(self, action=action, method=method, **kwargs)
        self.nestables = ['Number']
        if number and len(number.split(',')) > 1:
            for n in number.split(','):
                self.append(Number(n.strip()))
        else:
            self.body = number
        if method and (method != self.GET and method != self.POST):
            raise TwilioException( \
                "Invalid method parameter, must be GET or POST")

class Record(Verb):
    """Record audio from caller
    
    action: submit the result of the dial to this URL
    method: submit to 'action' url using GET or POST
    maxLength: maximum number of seconds to record
    timeout: seconds of silence before considering the recording complete
    """
    GET = 'GET'
    POST = 'POST'
    
    def __init__(self, action=None, method=None, maxLength=None, 
        timeout=None, **kwargs):
        Verb.__init__(self, action=action, method=method, maxLength=maxLength,
            timeout=timeout, **kwargs)
        if method and (method != self.GET and method != self.POST):
            raise TwilioException( \
                "Invalid method parameter, must be GET or POST")

# Twilio Utility function and Request Validation
# ===========================================================================

class Utils:
    def __init__(self, id, token):
        """initialize a twilio utility object
        
        id: Twilio account SID/ID
        token: Twilio account token
        
        returns a Twilio util object
        """
        self.id = id
        self.token = token
    
    def validateRequest(self, uri, postVars, expectedSignature):
        """validate a request from twilio
        
        uri: the full URI that Twilio requested on your server
        postVars: post vars that Twilio sent with the request
        expectedSignature: signature in HTTP X-Twilio-Signature header
        
        returns true if the request passes validation, false if not
        """
        
        # append the POST variables sorted by key to the uri
        s = uri
        if len(postVars) > 0:
            for k, v in sorted(postVars.items()):
                s += k + v
        
        # compute signature and compare signatures
        return (base64.encodestring(hmac.new(self.token, s, sha1).digest()).\
            strip() == expectedSignature)
