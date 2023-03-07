"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import date
from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version



class FeedbackList(ListResource):

    def __init__(self, version: Version, account_sid: str, call_sid: str):
        """
        Initialize the FeedbackList

        :param Version version: Version that contains the resource
        :param account_sid: The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
        :param call_sid: The call sid that uniquely identifies the call
        
        :returns: twilio.rest.api.v2010.account.call.feedback.FeedbackList
        :rtype: twilio.rest.api.v2010.account.call.feedback.FeedbackList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid, 'call_sid': call_sid,  }
        
        
        
    
    

    def get(self):
        """
        Constructs a FeedbackContext
        
        :returns: twilio.rest.api.v2010.account.call.feedback.FeedbackContext
        :rtype: twilio.rest.api.v2010.account.call.feedback.FeedbackContext
        """
        return FeedbackContext(self._version, account_sid=self._solution['account_sid'], call_sid=self._solution['call_sid'])

    def __call__(self):
        """
        Constructs a FeedbackContext
        
        :returns: twilio.rest.api.v2010.account.call.feedback.FeedbackContext
        :rtype: twilio.rest.api.v2010.account.call.feedback.FeedbackContext
        """
        return FeedbackContext(self._version, account_sid=self._solution['account_sid'], call_sid=self._solution['call_sid'])

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.FeedbackList>'

class FeedbackInstance(InstanceResource):

    class Issues(object):
        AUDIO_LATENCY = "audio-latency"
        DIGITS_NOT_CAPTURED = "digits-not-captured"
        DROPPED_CALL = "dropped-call"
        IMPERFECT_AUDIO = "imperfect-audio"
        INCORRECT_CALLER_ID = "incorrect-caller-id"
        ONE_WAY_AUDIO = "one-way-audio"
        POST_DIAL_DELAY = "post-dial-delay"
        UNSOLICITED_CALL = "unsolicited-call"

    def __init__(self, version, payload, account_sid: str, call_sid: str):
        """
        Initialize the FeedbackInstance
        :returns: twilio.rest.api.v2010.account.call.feedback.FeedbackInstance
        :rtype: twilio.rest.api.v2010.account.call.feedback.FeedbackInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'date_created': deserialize.rfc2822_datetime(payload.get('date_created')),
            'date_updated': deserialize.rfc2822_datetime(payload.get('date_updated')),
            'issues': payload.get('issues'),
            'quality_score': deserialize.integer(payload.get('quality_score')),
            'sid': payload.get('sid'),
        }

        self._context = None
        self._solution = { 'account_sid': account_sid, 'call_sid': call_sid,  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: FeedbackContext for this FeedbackInstance
        :rtype: twilio.rest.api.v2010.account.call.feedback.FeedbackContext
        """
        if self._context is None:
            self._context = FeedbackContext(self._version, account_sid=self._solution['account_sid'], call_sid=self._solution['call_sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def date_created(self):
        """
        :returns: The date that this resource was created, given in [RFC 2822](https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date that this resource was last updated, given in [RFC 2822](https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def issues(self):
        """
        :returns: A list of issues experienced during the call. The issues can be: `imperfect-audio`, `dropped-call`, `incorrect-caller-id`, `post-dial-delay`, `digits-not-captured`, `audio-latency`, `unsolicited-call`, or `one-way-audio`.
        :rtype: list[FeedbackInstance.Issues]
        """
        return self._properties['issues']
    
    @property
    def quality_score(self):
        """
        :returns: `1` to `5` quality score where `1` represents imperfect experience and `5` represents a perfect call.
        :rtype: int
        """
        return self._properties['quality_score']
    
    @property
    def sid(self):
        """
        :returns: A 34 character string that uniquely identifies this resource.
        :rtype: str
        """
        return self._properties['sid']
    
    def fetch(self):
        """
        Fetch the FeedbackInstance
        

        :returns: The fetched FeedbackInstance
        :rtype: twilio.rest.api.v2010.account.call.feedback.FeedbackInstance
        """
        return self._proxy.fetch()
    
    def update(self, quality_score=values.unset, issue=values.unset):
        """
        Update the FeedbackInstance
        
        :params int quality_score: The call quality expressed as an integer from `1` to `5` where `1` represents very poor call quality and `5` represents a perfect call.
        :params list[FeedbackInstance.Issues] issue: One or more issues experienced during the call. The issues can be: `imperfect-audio`, `dropped-call`, `incorrect-caller-id`, `post-dial-delay`, `digits-not-captured`, `audio-latency`, `unsolicited-call`, or `one-way-audio`.

        :returns: The updated FeedbackInstance
        :rtype: twilio.rest.api.v2010.account.call.feedback.FeedbackInstance
        """
        return self._proxy.update(quality_score=quality_score, issue=issue, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.FeedbackInstance {}>'.format(context)

class FeedbackContext(InstanceContext):

    def __init__(self, version: Version, account_sid: str, call_sid: str):
        """
        Initialize the FeedbackContext

        :param Version version: Version that contains the resource
        :param account_sid: The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
        :param call_sid: The call sid that uniquely identifies the call

        :returns: twilio.rest.api.v2010.account.call.feedback.FeedbackContext
        :rtype: twilio.rest.api.v2010.account.call.feedback.FeedbackContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'account_sid': account_sid,
            'call_sid': call_sid,
        }
        self._uri = '/Accounts/{account_sid}/Calls/{call_sid}/Feedback.json'.format(**self._solution)
        
    
    def fetch(self):
        """
        Fetch the FeedbackInstance
        

        :returns: The fetched FeedbackInstance
        :rtype: twilio.rest.api.v2010.account.call.feedback.FeedbackInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return FeedbackInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            call_sid=self._solution['call_sid'],
            
        )
        
    def update(self, quality_score=values.unset, issue=values.unset):
        """
        Update the FeedbackInstance
        
        :params int quality_score: The call quality expressed as an integer from `1` to `5` where `1` represents very poor call quality and `5` represents a perfect call.
        :params list[FeedbackInstance.Issues] issue: One or more issues experienced during the call. The issues can be: `imperfect-audio`, `dropped-call`, `incorrect-caller-id`, `post-dial-delay`, `digits-not-captured`, `audio-latency`, `unsolicited-call`, or `one-way-audio`.

        :returns: The updated FeedbackInstance
        :rtype: twilio.rest.api.v2010.account.call.feedback.FeedbackInstance
        """
        data = values.of({ 
            'QualityScore': quality_score,
            'Issue': serialize.map(issue, lambda e: e),
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return FeedbackInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            call_sid=self._solution['call_sid']
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.FeedbackContext {}>'.format(context)


