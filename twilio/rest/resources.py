import re
import datetime
import logging
import twilio
from twilio import TwilioException
from twilio import TwilioRestException
from urllib import urlencode
from urlparse import urlparse

try:
    from urlparse import parse_qs
except ImportError:
    from cgi import parse_qs

# import json
try:
    import json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        from django.utils import simplejson as json

# import httplib2
try:
    import httplib2
except ImportError:
    from twilio.contrib import httplib2


def transform_params(p):
    """
    Transform parameters, throwing away any None values
    and convert False and True values to strings

    Ex:
    {"record": true, "date_created": "2012-01-02"}

    becomes:
    {"Record": "true", "DateCreated": "2012-01-02"}
    """
    p = [(format_name(d),
          convert_boolean(p[d])) for d in p if p[d] is not None]
    return dict(p)


def format_name(word):
    if word.lower() == word:
        return convert_case(word)
    else:
        return word


def parse_date(d):
    """
    Return a string representation of a date that the Twilio API understands
    Format is YYYY-MM-DD. Returns None if d is not a string, datetime, or date
    """
    if isinstance(d, datetime.datetime):
        return str(d.date())
    elif isinstance(d, datetime.date):
        return str(d)
    elif isinstance(d, str):
        return d


def convert_boolean(boolean):
    if isinstance(boolean, bool):
        return 'true' if boolean else 'false'
    return boolean


def convert_case(s):
    """
    Given a string in snake case, convert to CamelCase

    Ex:
    date_created -> DateCreated
    """
    return ''.join([a.title() for a in s.split("_") if a])


def convert_keys(d):
    """
    Return a dictionary with all keys converted from arguments
    """
    special = {
        "started_before": "StartTime<",
        "started_after":  "StartTime>",
        "started":        "StartTime",
        "ended_before":   "EndTime<",
        "ended_after":    "EndTime>",
        "ended":          "EndTime",
        "from_":          "From",
    }

    result = {}

    for k, v in d.iteritems():
        if k in special:
            result[special[k]] = v
        else:
            result[convert_case(k)] = v

    return result


def normalize_dates(myfunc):
    def inner_func(*args, **kwargs):
        for k, v in kwargs.iteritems():
            res = [True for s in ["after", "before", "on"] if s in k]
            if len(res):
                kwargs[k] = parse_date(v)
        return myfunc(*args, **kwargs)
    inner_func.__doc__ = myfunc.__doc__
    inner_func.__repr__ = myfunc.__repr__
    return inner_func


class Response(object):
    """
    Take a httplib2 response and turn it into a requests response
    """
    def __init__(self, httplib_resp, content, url):
        self.content = content
        self.cached = False
        self.status_code = int(httplib_resp.status)
        self.ok = self.status_code < 400
        self.url = url


def make_request(method, url,
    params=None, data=None, headers=None, cookies=None, files=None,
    auth=None, timeout=None, allow_redirects=False, proxies=None):
    """Sends an HTTP request Returns :class:`Response <models.Response>`

    See the requests documentation for explanation of all these parameters

    Currently proxies, files, and cookies are all ignored
    """
    http = httplib2.Http(timeout=timeout)
    http.follow_redirects = allow_redirects

    if auth is not None:
        http.add_credentials(auth[0], auth[1])

    if data is not None:
        udata = {}
        for k, v in data.iteritems():
            try:
                udata[k.encode('utf-8')] = unicode(v).encode('utf-8')
            except UnicodeDecodeError:
                udata[k.encode('utf-8')] = unicode(v, 'utf-8').encode('utf-8')
        data = urlencode(udata)

    if params is not None:
        enc_params = urlencode(params, doseq=True)
        if urlparse(url).query:
            url = '%s&%s' % (url, enc_params)
        else:
            url = '%s?%s' % (url, enc_params)

    resp, content = http.request(url, method, headers=headers, body=data)

    # Format httplib2 reqeusts as reqeusts objects
    return Response(resp, content, url)


def make_twilio_request(method, uri, **kwargs):
    """
    Make a request to Twilio. Throws an error
    """
    headers = kwargs.get("headers", {})
    headers["User-Agent"] = "twilio-python/%s" % twilio.__version__

    if method == "POST" and "Content-Type" not in headers:
        headers["Content-Type"] = "application/x-www-form-urlencoded"

    kwargs["headers"] = headers

    if "Accept" not in headers:
        headers["Accept"] = "application/json"
        uri = uri + ".json"

    resp = make_request(method, uri, **kwargs)

    if not resp.ok:
        try:
            error = json.loads(resp.content)
            message = "%s: %s" % (error["code"], error["message"])
        except:
            message = resp.content

        raise TwilioRestException(resp.status_code, resp.url, message)

    return resp


class Resource(object):
    """A REST Resource"""

    name = "Resource"

    def __init__(self, base_uri, auth):
        self.base_uri = base_uri
        self.auth = auth

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
                and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)

    def request(self, method, uri, **kwargs):
        """
        Send an HTTP request to the resource.

        Raise a TwilioRestException
        """
        resp = make_twilio_request(method, uri, auth=self.auth, **kwargs)

        logging.debug(resp.content)

        if method == "DELETE":
            return resp, {}
        else:
            return resp, json.loads(resp.content)

    @property
    def uri(self):
        format = (self.base_uri, self.name)
        return "%s/%s" % format


class InstanceResource(Resource):

    subresources = []
    id_key = "sid"

    def __init__(self, parent, sid):
        self.parent = parent
        self.name = sid
        super(InstanceResource, self).__init__(parent.uri,
            parent.auth)

    def load(self, entries):
        if "from" in entries.keys():
            entries["from_"] = entries["from"]
            del entries["from"]

        if "uri" in entries.keys():
            del entries["uri"]

        self.__dict__.update(entries)

    def load_subresources(self):
        """
        Load all subresources
        """
        for resource in self.subresources:
            list_resource = resource(self.uri, self.parent.auth)
            self.__dict__[list_resource.key] = list_resource

    def update_instance(self, **kwargs):
        a = self.parent.update(self.name, **kwargs)
        self.load(a.__dict__)

    def delete_instance(self):
        return self.parent.delete(self.name)


class ListResource(Resource):

    name = "Resources"
    instance = InstanceResource

    def __init__(self, *args, **kwargs):
        super(ListResource, self).__init__(*args, **kwargs)

        try:
            self.key
        except AttributeError:
            self.key = self.name.lower()

    def get(self, sid):
        """Return an instance resource """
        return self.get_instance(sid)

    def get_instance(self, sid):
        """Request the specified instance resource"""
        uri = "%s/%s" % (self.uri, sid)
        resp, item = self.request("GET", uri)
        return self.load_instance(item)

    def get_instances(self, params):
        """
        Query the list resource for a list of InstanceResources.

        Raises a TwilioRestException if requesting a page of results that does
        not exist.

        :param dict params: List of URL parameters to be included in request
        :param int page: The page of results to retrieve (most recent at 0)
        :param int page_size: The number of results to be returned.

        :returns: -- the list of resources
        """
        params = transform_params(params)

        resp, page = self.request("GET", self.uri, params=params)

        if self.key not in page:
            raise TwilioException("Key %s not present in response" % self.key)

        return [self.load_instance(ir) for ir in page[self.key]]

    def create_instance(self, body):
        """
        Create an InstanceResource via a POST to the List Resource

        :param dict body: Dictionary of POST data
        """
        resp, instance = self.request("POST", self.uri,
                                      data=transform_params(body))

        if resp.status_code != 201:
            raise TwilioRestException(resp.status,
                                      self.uri, "Resource not created")

        return self.load_instance(instance)

    def delete_instance(self, sid):
        """
        Delete an InstanceResource via DELETE

        body: string -- HTTP Body for the quest
        """
        uri = "%s/%s" % (self.uri, sid)
        resp, instance = self.request("DELETE", uri)
        return resp.status_code == 204

    def update_instance(self, sid, body):
        """
        Update an InstanceResource via a POST

        sid: string -- String identifier for the list resource
        body: dictionary -- Dict of items to POST
        """
        uri = "%s/%s" % (self.uri, sid)
        resp, entry = self.request("POST", uri, data=transform_params(body))
        return self.load_instance(entry)

    def count(self):
        """
        Return the number of instance resources contained in this list resource
        """
        resp, page = self.request("GET", self.uri)
        return page["total"]

    def iter(self, **kwargs):
        """
        Return all instance resources using an iterator
        """
        params = transform_params(kwargs)

        while True:
            resp, page = self.request("GET", self.uri, params=params)

            if self.key not in page:
                raise StopIteration()

            for ir in page[self.key]:
                yield self.load_instance(ir)

            if not page.get('next_page_uri', ''):
                raise StopIteration()

            o = urlparse(page['next_page_uri'])
            params.update(parse_qs(o.query))


    def load_instance(self, data):
        instance = self.instance(self, data[self.instance.id_key])
        instance.load(data)
        instance.load_subresources()
        return instance


class AvailablePhoneNumber(InstanceResource):
    """ An available phone number resource """

    def __init__(self, parent):
        super(AvailablePhoneNumber, self).__init__(parent, "")
        self.name = ""

    def purchase(self, **kwargs):
        return self.parent.purchase(phone_number=self.phone_number,
                                    **kwargs)


class AvailablePhoneNumbers(ListResource):

    name = "AvailablePhoneNumbers"
    key = "available_phone_numbers"
    instance = AvailablePhoneNumber

    types = {"local": "Local", "tollfree": "TollFree"}

    def __init__(self, base_uri, auth, phone_numbers):
        super(AvailablePhoneNumbers, self).__init__(base_uri, auth)
        self.phone_numbers = phone_numbers

    def get(self, sid):
        raise TwilioException("Individual AvailablePhoneNumbers have no sid")

    def list(self, type="local", country="US", region=None, postal_code=None,
             lata=None, rate_center=None, **kwargs):
        """
        Search for phone numbers
        """
        kwargs["in_region"] = kwargs.get("in_region", region)
        kwargs["in_postal_code"] = kwargs.get("in_postal_code", postal_code)
        kwargs["in_lata"] = kwargs.get("in_lata", lata)
        kwargs["in_rate_center"] = kwargs.get("in_rate_center", rate_center)
        params = transform_params(kwargs)

        uri = "%s/%s/%s" % (self.uri, country, self.types[type])
        resp, page = self.request("GET", uri, params=params)

        return [self.load_instance(i) for i in page[self.key]]

    def load_instance(self, data):
        instance = self.instance(self.phone_numbers)
        instance.load(data)
        instance.load_subresources()
        return instance


class Transcription(InstanceResource):
    pass


class Transcriptions(ListResource):

    name = "Transcriptions"
    instance = Transcription

    def list(self, **kwargs):
        """
        Return a list of :class:`Transcription` resources
        """
        return self.get_instances(kwargs)


class Recording(InstanceResource):

    subresources = [
        Transcriptions,
        ]

    def __init__(self, *args, **kwargs):
        super(Recording, self).__init__(*args, **kwargs)
        self.formats = {
            "mp3": self.uri + ".mp3",
            "wav": self.uri + ".wav",
            }

    def delete(self):
        """
        Delete this recording
        """
        return self.delete_instance()


class Recordings(ListResource):

    name = "Recordings"
    instance = Recording

    @normalize_dates
    def list(self, before=None, after=None, **kwargs):
        """
        Returns a page of :class:`Recording` resources as a list.
        For paging information see :class:`ListResource`.

        :param date after: Only list recordings logged after this datetime
        :param date before: Only list recordings logger before this datetime
        :param call_sid: Only list recordings from this :class:`Call`
        """
        kwargs["DateCreated<"] = before
        kwargs["DateCreated>"] = after
        return self.get_instances(kwargs)

    def delete(self, sid):
        """
        Delete the given recording
        """
        return self.delete_instance(sid)


class Notification(InstanceResource):

    def delete(self):
        """
        Delete this notification
        """
        return self.delete_instance()


class Notifications(ListResource):

    name = "Notifications"
    instance = Notification

    @normalize_dates
    def list(self, before=None, after=None, **kwargs):
        """
        Returns a page of :class:`Notification` resources as a list.
        For paging information see :class:`ListResource`.

        **NOTE**: Due to the potentially voluminous amount of data in a
        notification, the full HTTP request and response data is only returned
        in the Notification instance resource representation.

        :param date after: Only list notifications logged after this datetime
        :param date before: Only list notifications logger before this datetime
        :param log_level: If 1, only shows errors. If 0, only show warnings
        """
        kwargs["MessageDate<"] = before
        kwargs["MessageDate>"] = after
        return self.get_instances(kwargs)

    def delete(self, sid):
        """
        Delete a given Notificiation
        """
        return self.delete_instance(sid)


class ConnectApp(InstanceResource):
    """ An authorized connect app """
    pass


class ConnectApps(ListResource):
    """ A list of Connect App resources """

    name = "ConnectApps"
    instance = ConnectApp
    key = "connect_apps"

    def list(self, **kwargs):
        """
        Returns a page of :class:`ConnectApp` resources as a list. For paging
        informtion see :class:`ListResource`
        """
        return self.get_instances(kwargs)


class AuthorizedConnectApp(ConnectApp):
    """ An authorized connect app """

    id_key = "connect_app_sid"

    def load(self, entries):
        """ Translate certain parameters into others"""
        result = {}

        for k, v in entries.iteritems():
            k = k.replace("connect_app_", "")
            result[k] = v

        super(AuthorizedConnectApp, self).load(result)


class AuthorizedConnectApps(ConnectApps):
    """ A list of Authorized Connect App resources """

    name = "AuthorizedConnectApps"
    instance = AuthorizedConnectApp
    key = "authorized_connect_apps"


class Call(InstanceResource):
    """ A call resource """

    BUSY = "busy"
    CANCELED = "canceled"
    COMPLETED = "completed"
    FAILED = "failed"
    IN_PROGRESS = "in-progress"
    NO_ANSWER = "no-answer"
    QUEUED = "queued"
    RINGING = "ringing"

    subresources = [
        Notifications,
        Recordings,
        ]

    def hangup(self):
        """ If this call is currenlty active, hang up the call.
        If this call is scheduled to be made, remove the call
        from the queue
        """
        a = self.parent.hangup(self.name)
        self.load(a.__dict__)

    def cancel(self):
        """ If the called is queued or rining, cancel the calls.
        Will not affect in progress calls
        """
        a = self.parent.cancel(self.name)
        self.load(a.__dict__)

    def route(self, **kwargs):
        """Route the specified :class:`Call` to another url.

        :param url: A valid URL that returns TwiML.
        :param method: HTTP method Twilio uses when requesting the above URL.
        """
        a = self.parent.route(self.name, **kwargs)
        self.load(a.__dict__)


class Calls(ListResource):
    """ A list of Call resources """

    name = "Calls"
    instance = Call

    @normalize_dates
    def list(self, from_=None, ended_after=None,
             ended_before=None, ended=None, started_before=None,
             started_after=None, started=None, **kwargs):
        """
        Returns a page of :class:`Call` resources as a list. For paging
        informtion see :class:`ListResource`

        :param date after: Only list calls started after this datetime
        :param date before: Only list calls started before this datetime
        """
        kwargs["from"] = from_
        kwargs["StartTime<"] = started_before
        kwargs["StartTime>"] = started_after
        kwargs["StartTime"] = parse_date(started)
        kwargs["EndTime<"] = ended_before
        kwargs["EndTime>"] = ended_after
        kwargs["EndTime"] = parse_date(ended)
        return self.get_instances(kwargs)

    def create(self, to, from_, url, status_method=None, **kwargs):
        """
        Make a phone call to a number.

        :param string to: The phone number to call
        :param string `from_`: The caller ID (must be a verified Twilio number)
        :param string url: The URL to read TwiML from when the call connects
        :param method: The HTTP method Twilio should use to request the url
        :type method: None (defaults to 'POST'), 'GET', or 'POST'
        :param string fallback_url: A URL that Twilio will request if an error occurs requesting or executing the TwiML at url.
        :param string fallback_method: The HTTP method that Twilio should use to request the fallback_url
        :type fallback_method: None (will make a 'POST' request), 'GET', or 'POST'
        :param string status_callback: A URL that Twilio will request when the call ends to notify your app.
        :param string status_method: The HTTP method Twilio should use when requesting the above URL.
        :param string if_machine: Tell Twilio to try and determine if a machine
            (like voicemail) or a human has answered the call.
            See more in our `answering machine documentation
            <http://www.twilio.com/docs/api/rest/making_calls#handling-outcomes-answering-machines">`_.
        :type if_machine: None, 'Continue', or 'Hangup'
        :param string send_digits: A string of keys to dial after connecting to the number.
        :type send_digits: None or any combination of (0-9), '#', '*' or 'w' (to insert a half second pause).
        :param int timeout: The integer number of seconds that Twilio should allow the phone to ring before assuming there is no answer.
        :param string application_sid: The 34 character sid of the application Twilio should use to handle this phone call. Should not be used in conjunction with the url parameter.

        :return: A :class:`Call` object
        """
        kwargs["from"] = from_
        kwargs["to"] = to
        kwargs["url"] = url
        kwargs["status_callback_method"] = status_method
        return self.create_instance(kwargs)

    def update(self, sid, **kwargs):
        return self.update_instance(sid, kwargs)

    def cancel(self, sid):
        """ If this call is queued or ringing, cancel the call.
        Will not affect in-progress calls.

        :param sid: A Call Sid for a specific call
        :returns: Updated :class:`Call` resource
        """
        return self.update(sid, status=Call.CANCELED)

    def hangup(self, sid):
        """ If this call is currently active, hang up the call. If this call is
        scheduled to be made, remove the call from the queue.

        :param sid: A Call Sid for a specific call
        :returns: Updated :class:`Call` resource
        """
        return self.update(sid, status=Call.COMPLETED)

    def route(self, sid, url, method="POST"):
        """Route the specified :class:`Call` to another url.

        :param sid: A Call Sid for a specific call
        :param url: A valid URL that returns TwiML.
        :param method: The HTTP method Twilio uses when requesting the URL.
        :returns: Updated :class:`Call` resource
        """
        return self.update(sid, url=url, method=method)


class CallerId(InstanceResource):

    def delete(self):
        """
        Deletes this caller ID from the account.
        """
        return self.delete_instance()

    def update(self, **kwargs):
        """
        Update the CallerId
        """
        self.update_instance(**kwargs)


class CallerIds(ListResource):
    """ A list of :class:`CallerId` resources """

    name = "OutgoingCallerIds"
    key = "outgoing_caller_ids"
    instance = CallerId

    def delete(self, sid):
        """
        Deletes a specific :class:`CallerId` from the account.
        """
        self.delete_instance(sid)

    def list(self, **kwargs):
        """
        :param phone_number: Show caller ids with this phone number.
        :param friendly_name: Show caller ids with this friendly name.
        """
        return self.get_instances(kwargs)

    def update(self, sid, **kwargs):
        """
        Update a specific :class:`CallerId`
        """
        return self.update_instance(sid, kwargs)

    def validate(self, phone_number, **kwargs):
        """
        Begin the validation process for the given number.

        Returns a dictionary with the following keys

        **account_sid**:
        The unique id of the Account to which the Validation Request belongs.

        **phone_number**: The incoming phone number being validated,
        formatted with a '+' and country code e.g., +16175551212

        **friendly_name**: The friendly name you provided, if any.

        **validation_code**: The 6 digit validation code that must be entered
        via the phone to validate this phone number for Caller ID.

        :param phone_number: The phone number to call and validate
        :param friendly_name: A description for the new caller ID
        :param call_delay: Number of seconds to delay the validation call.
        :param extension: Digits to dial after connecting the validation call.
        :returns: A response dictionary
        """
        kwargs["phone_number"] = phone_number
        params = transform_params(kwargs)
        resp, validation = self.request("POST", self.uri, data=params)
        return validation


class PhoneNumber(InstanceResource):

    def load(self, entries):
        """ Set the proper Account owner of this phone number """

        # Only check if entries has a uri
        if "account_sid" in entries:
            # Parse the parent's uri to get the scheme and base
            uri = re.sub(r'AC(.*)', entries["account_sid"],
                self.parent.base_uri)

            self.parent = PhoneNumbers(uri, self.parent.auth)
            self.base_uri = self.parent.uri

        super(PhoneNumber, self).load(entries)

    def transfer(self, account_sid):
        """
        Transfer the phone number with sid from the current account to another
        identified by account_sid
        """
        a = self.parent.transfer(self.name, account_sid)
        self.load(a.__dict__)

    def update(self, **kwargs):
        """
        Update this phone number instance.
        """
        a = self.parent.update(self.name, **kwargs)
        self.load(a.__dict__)

    def delete(self):
        """
        Release this phone number from your account. Twilio will no longer
        answer calls to this number, and you will stop being billed the monthly
        phone number fees. The phone number will eventually be recycled and
        potentially given to another customer, so use with care. If you make a
        mistake, contact us... we may be able to give you the number back.
        """
        return self.parent.delete(self.name)


class PhoneNumbers(ListResource):

    name = "IncomingPhoneNumbers"
    key = "incoming_phone_numbers"
    instance = PhoneNumber

    def __init__(self, base_uri, auth):
        super(PhoneNumbers, self).__init__(base_uri, auth)
        self.available_phone_numbers = \
            AvailablePhoneNumbers(base_uri, auth, self)

    def delete(self, sid):
        """
        Release this phone number from your account. Twilio will no longer
        answer calls to this number, and you will stop being billed the
        monthly phone number fees. The phone number will eventually be
        recycled and potentially given to another customer, so use with care.
        If you make a mistake, contact us... we may be able to give you the
        number back.
        """
        return self.delete_instance(sid)

    def list(self, **kwargs):
        """
        :param phone_number: Show phone numbers that match this pattern.
        :param friendly_name: Show phone numbers with this friendly name

        You can specify partial numbers and use '*' as a wildcard.
        """
        return self.get_instances(kwargs)

    def purchase(self, status_callback_url=None, **kwargs):
        """
        Attempt to purchase the specified number. The only required parameters
        are **either** phone_number or area_code

        :returns: Returns a :class:`PhoneNumber` instance on success,
                  :data:`False` on failure
        """
        kwargs["StatusCallback"] = kwargs.get("status_callback", status_callback_url)

        if 'phone_number' not in kwargs and 'area_code' not in kwargs:
            raise TypeError("phone_number or area_code is required")

        return self.create_instance(kwargs)

    def search(self, **kwargs):
        """
        :param type: The type of phone number to search for.
        :param string country: Either "US" or "CA". Defaults to "US"
        :param string region: When searching the US, show numbers in this state
        :param string postal_code: Only show numbers in this area code
        :param string rate_center: US only.
        :param tuple near_lat_long: Find close numbers within Distance miles.
        :param integer distance: Search radius for a Near- query in miles.
        """
        return self.available_phone_numbers.list(**kwargs)

    def transfer(self, sid, account_sid):
        """
        Transfer the phone number with sid from the current account to another
        identified by account_sid
        """
        return self.update(sid, account_sid=account_sid)

    def update(self, sid, **kwargs):
        """
        Update this phone number instance
        """
        if "application_sid" in kwargs:
            for sid_type in ["voice_application_sid", "sms_application_sid"]:
                if sid_type not in kwargs:
                    kwargs[sid_type] = kwargs["application_sid"]
            del kwargs["application_sid"]
        return self.update_instance(sid, kwargs)


class Sandbox(InstanceResource):

    id_key = "pin"

    def update(self, **kwargs):
        """
        Update your Twilio Sandbox
        """
        a = self.parent.update(**kwargs)
        self.load(a.__dict__)


class Sandboxes(ListResource):

    name = "Sandbox"
    instance = Sandbox

    def get(self):
        """Request the specified instance resource"""
        return self.get_instance(self.uri)

    def update(self, **kwargs):
        """
        Update your Twilio Sandbox
        """
        resp, entry = self.request("POST", self.uri, body=transform_params(kwargs))
        return self.create_instance(entry)


class Sms(object):
    """
    Holds all the specific SMS list resources
    """

    name = "SMS"
    key = "sms"

    def __init__(self, base_uri, auth):
        self.uri = "%s/SMS" % base_uri
        self.messages = SmsMessages(self.uri, auth)
        self.short_codes = ShortCodes(self.uri, auth)


class SmsMessage(InstanceResource):
    pass


class SmsMessages(ListResource):

    name = "Messages"
    key = "sms_messages"
    instance = SmsMessage

    def create(self, from_=None, **kwargs):
        """
        Create and send a SMS Message.

        :param string to: The destination phone number.
        :param string `from_`: The phone number sending this message (must be a verified Twilio number)
        :param string body: The message you want to send, limited to 160 characters.
        :param status_callback: A URL that Twilio will POST to when your message is processed.
        :param string application_sid: The 34 character sid of the application Twilio should use to handle this phone call.
        """
        kwargs["from"] = from_
        return self.create_instance(kwargs)

    @normalize_dates
    def list(self, from_=None, before=None, after=None, date_sent=None, **kwargs):
        """
        Returns a page of :class:`SMSMessage` resources as a list. For
        paging informtion see :class:`ListResource`.

        :param to: Only show SMS messages to this phone number.
        :param from_: Only show SMS messages from this phone number.
        :param date after: Only list SMS messages sent after this date.
        :param date before: Only list SMS message sent before this date.
        :param date date_sent: Only list SMS message sent on this date.
        :param `from_`: Only show SMS messages from this phone number.
        :param date after: Only list recordings logged after this datetime
        :param date before: Only list recordings logged before this datetime
        """
        kwargs["From"] = from_
        kwargs["DateSent<"] = before
        kwargs["DateSent>"] = after
        kwargs["DateSent"] = parse_date(date_sent)
        return self.get_instances(kwargs)


class ShortCode(InstanceResource):

    def update(self, **kwargs):
        return self.parent.update(self.name, **kwargs)


class ShortCodes(ListResource):

    name = "ShortCodes"
    key = "short_codes"
    instance = ShortCode

    def list(self, **kwargs):
        """
        Returns a page of :class:`ShortCode` resources as a list. For
        paging information see :class:`ListResource`.

        :param short_code: Only show the ShortCode resources that match this
                           pattern. You can specify partial numbers and use '*'
                           as a wildcard for any digit.
        :param friendly_name: Only show the ShortCode resources with friendly
                              names that exactly match this name.
        """
        return self.get_instances(kwargs)

    def update(self, sid, url=None, method=None, fallback_url=None,
               fallback_method=None, **kwargs):
        """
        Update a specific :class:`ShortCode`, by specifying the sid.

        :param friendly_name: Description of the short code, with maximum
                              length 64 characters.
        :param api_version: SMSs to this short code will start a new TwiML
                            session with this API version.
        :param url: The URL that Twilio should request when somebody sends an
                    SMS to the short code.
        :param method: The HTTP method that should be used to request the url.
        :param fallback_url: A URL that Twilio will request if an error occurs
                             requesting or executing the TwiML at the url.
        :param fallback_method: The HTTP method that should be used to request
                                the fallback_url.
        """
        kwargs["sms_url"] = kwargs.get("sms_url", url)
        kwargs["sms_method"] = kwargs.get("sms_method", method)
        kwargs["sms_fallback_url"] = \
            kwargs.get("sms_fallback_url", fallback_url)
        kwargs["sms_fallback_method"] = \
            kwargs.get("sms_fallback_method", fallback_method)
        return self.update_instance(sid, kwargs)


class Participant(InstanceResource):

    id_key = "call_sid"

    def mute(self):
        """
        Mute the participant
        """
        self.update_instance(muted="true")

    def unmute(self):
        """
        Unmute the participant
        """
        self.update_instance(muted="false")

    def kick(self):
        """
        Remove the participant from the given conference
        """
        self.delete_instance()


class Participants(ListResource):

    name = "Participants"
    instance = Participant

    def list(self, **kwargs):
        """
        Returns a list of :class:`Participant` resources in the given
        conference

        :param conference_sid: Conference this participant is part of
        :param boolean muted: If True, only show participants who are muted
        """
        return self.get_instances(kwargs)

    def mute(self, call_sid):
        """
        Mute the given participant
        """
        return self.update(call_sid, muted=True)

    def unmute(self, call_sid):
        """
        Unmute the given participant
        """
        return self.update(call_sid, muted=False)

    def kick(self, call_sid):
        """
        Remove the participant from the given conference
        """
        return self.delete(call_sid)

    def delete(self, call_sid):
        """
        Remove the participant from the given conference
        """
        return self.delete_instance(call_sid)

    def update(self, sid, **kwargs):
        """
        :param sid: Paticipant identifier
        :param boolean muted: If true, mute this participant
        """
        return self.update_instance(sid, kwargs)


class Conference(InstanceResource):

    subresources = [
        Participants
        ]


class Conferences(ListResource):

    name = "Conferences"
    instance = Conference

    @normalize_dates
    def list(self, updated_before=None, updated_after=None, created_after=None,
             created_before=None, updated=None, created=None, **kwargs):
        """
        Return a list of :class:`Conference` resources

        :param status: Show conferences with this status
        :param friendly_name: Show conferences with this exact friendly_name
        :param date updated_after: List conferences updated after this date
        :param date updated_before: List conferences updated before this date
        :param date created_after: List conferences created after this date
        :param date created_before: List conferences created before this date
        """
        kwargs["DateUpdated"] = parse_date(kwargs.get("date_updated", updated))
        kwargs["DateCreated"] = parse_date(kwargs.get("date_created", created))
        kwargs["DateUpdated<"] = updated_before
        kwargs["DateUpdated>"] = updated_after
        kwargs["DateCreated<"] = created_before
        kwargs["DateCreated>"] = created_after
        return self.get_instances(kwargs)


class Member(InstanceResource):
    id_key = "call_sid"


class Members(ListResource):
    name = "Members"
    instance = Member
    key = "queue_members"

    def list(self, **kwargs):
        """
        Returns a list of :class:`Member` resources in the given queue

        :param queue_sid: Queue this participant is part of
        """
        return self.get_instances(kwargs)

    def dequeue(self, url, call_sid='Front', **kwargs):
        """
        Dequeues a member from the queue and have the member's call
        begin executing the TwiML document at the url.

        :param call_sid: Call sid specifying the member, if not given,
                         the member at the front of the queue will be used
        :param url: url of the TwiML document to be executed.
        """
        kwargs['url'] = url
        return self.update_instance(call_sid, kwargs)


class Queue(InstanceResource):

    subresources = [
        Members
    ]

    def update(self, **kwargs):
        """
        Update this queue

        :param friendly_name: A new friendly name for this queue
        :param max_size: A new max size. Changing a max size to less than the
                         current size results in the queue rejecting incoming
                         requests until it shrinks below the new max size
        """
        return self.parent.update_instance(self.name, kwargs)

    def delete(self):
        """
        Delete this queue.  Can only be run on empty queues.
        """
        return self.parent.delete_instance(self.name)


class Queues(ListResource):
    name = "Queues"
    instance = Queue

    def list(self, **kwargs):
        """
        Returns a page of :class:`Queue` resources as a list sorted by DateUpdated.
        For paging informtion see :class:`ListResource`
        """
        return self.get_instances(kwargs)

    def create(self, name, **kwargs):
        """ Create an :class:`Queue` with any of these optional parameters.

        :param name: A human readable description of the application,
                              with maximum length 64 characters.
        :param max_size: The limit on calls allowed into the queue (optional)
        """
        kwargs['friendly_name'] = name
        return self.create_instance(kwargs)

    def update(self, sid, **kwargs):
        """
        Update a :class:`Queue`
    
        :param sid: String identifier for a Queue resource
        :param friendly_name: A new friendly name for this queue
        :param max_size: A new max size. Changing a max size to less than the
                         current size results in the queue rejecting incoming
                         requests until it shrinks below the new max size
        """
        return self.update_instance(sid, kwargs)

    def delete(self, sid):
        """
        Delete a :class:`Queue`. Can only be run on empty queues.

        :param sid: String identifier for a Queue resource
        """
        return self.delete_instance(sid)


class Application(InstanceResource):
    """ An application resource """

    def update(self, **kwargs):
        """
        Update this application
        """
        return self.parent.update(self.sid, **kwargs)

    def delete(self):
        """
        Delete this application
        """
        return self.parent.delete(self.sid)


class Applications(ListResource):

    name = "Applications"
    instance = Application

    def list(self, **kwargs):
        """
        Returns a page of :class:`Application` resources as a list. For paging
        informtion see :class:`ListResource`

        :param date friendly_name: List applications with this friendly name
        """
        return self.get_instances(kwargs)

    def create(self, **kwargs):
        """
        Create an :class:`Application` with any of these optional parameters.

        :param friendly_name: A human readable description of the application,
                              with maximum length 64 characters.
        :param api_version: Requests to this application's URLs will start a
                            new TwiML session with this API version.
                            Either 2010-04-01 or 2008-08-01.
        :param voice_url: The URL that Twilio should request when somebody
                          dials a phone number assigned to this application.
        :param voice_method: The HTTP method that should be used to request the
                             VoiceUrl. Either GET or POST.
        :param voice_fallback_url: A URL that Twilio will request if an error
                                   occurs requesting or executing the TwiML
                                   defined by VoiceUrl.
        :param voice_fallback_method: The HTTP method that should be used to
                                      request the VoiceFallbackUrl. Either GET
                                      or POST.
        :param status_callback: The URL that Twilio will request to pass status
                                parameters (such as call ended) to your
                                application.
        :param status_callback_method: The HTTP method Twilio will use to make
                                       requests to the StatusCallback URL.
                                       Either GET or POST.
        :param voice_caller_id_lookup: Do a lookup of a caller's name from the
                                       CNAM database and post it to your app.
                                       Either true or false.
        :param sms_url: The URL that Twilio should request when somebody sends
                        an SMS to a phone number assigned to this application.
        :param sms_method: The HTTP method that should be used to request the
                           SmsUrl. Either GET or POST.
        :param sms_fallback_url: A URL that Twilio will request if an error
                                 occurs requesting or executing the TwiML
                                 defined by SmsUrl.
        :param sms_fallback_method: The HTTP method that should be used to
                                    request the SmsFallbackUrl. Either GET
                                    or POST.
        :param sms_status_callback: Twilio will make a POST request to this URL
                                    to pass status parameters (such as sent or
                                    failed) to your application if you specify
                                    this application's Sid as the
                                    ApplicationSid on an outgoing SMS request.
        """
        return self.create_instance(kwargs)

    def update(self, sid, **kwargs):
        """
        Update an :class:`Application` with the given parameters.

        All the parameters are describe above in :meth:`create`
        """
        return self.update_instance(sid, kwargs)

    def delete(self, sid):
        """
        Delete an :class:`Application`
        """
        return self.delete_instance(sid)


class Account(InstanceResource):
    """ An Account resource """

    ACTIVE = "active"
    SUSPENDED = "suspended"
    CLOSED = "closed"

    subresources = [
        Applications,
        Notifications,
        Transcriptions,
        Recordings,
        Calls,
        Sms,
        CallerIds,
        PhoneNumbers,
        Conferences,
        ConnectApps,
        Queues,
        AuthorizedConnectApps,
        ]

    def update(self, **kwargs):
        """
        :param friendly_name: Update the description of this account.
        :param status: Alter the status of this account

        Use :data:`CLOSED` to irreversibly close this account,
        :data:`SUSPENDED` to temporarily suspend it, or :data:`ACTIVE`
        to reactivate it.
        """
        self.update_instance(**kwargs)

    def close(self):
        """
        Permenently deactivate this account
        """
        return self.update_instance(status=Account.CLOSED)

    def suspend(self):
        """
        Temporarily suspend this account
        """
        return self.update_instance(status=Account.SUSPENDED)

    def activate(self):
        """
        Reactivate this account
        """
        return self.update_instance(status=Account.ACTIVE)


class Accounts(ListResource):
    """ A list of Account resources """

    name = "Accounts"
    instance = Account

    def list(self, **kwargs):
        """
        Returns a page of :class:`Account` resources as a list. For paging
        informtion see :class:`ListResource`

        :param date friendly_name: Only list accounts with this friendly name
        :param date status: Only list accounts with this status
        """
        return self.get_instances(kwargs)

    def update(self, sid, **kwargs):
        """
        :param sid: Account identifier
        :param friendly_name: Update the description of this account.
        :param status: Alter the status of this account

        Use :data:`CLOSED` to irreversibly close this account,
        :data:`SUSPENDED` to temporarily suspend it, or :data:`ACTIVE`
        to reactivate it.
        """
        return self.update_instance(sid, kwargs)

    def close(self, sid):
        """
        Permenently deactivate an account, Alias to update
        """
        return self.update(sid, status=Account.CLOSED)

    def suspend(self, sid):
        """
        Temporarily suspend an account, Alias to update
        """
        return self.update(sid, status=Account.SUSPENDED)

    def activate(self, sid):
        """
        Reactivate an account, Alias to update
        """
        return self.update(sid, status=Account.ACTIVE)

    def create(self, **kwargs):
        """
        Returns a newly created sub account resource.

        :param friendly_name: Update the description of this account.
        """
        return self.create_instance(kwargs)
