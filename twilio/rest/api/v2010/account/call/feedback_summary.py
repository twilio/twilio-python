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



class FeedbackSummaryList(ListResource):

    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the FeedbackSummaryList

        :param Version version: Version that contains the resource
        :param account_sid: The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
        
        :returns: twilio.rest.api.v2010.account.call.feedback_summary.FeedbackSummaryList
        :rtype: twilio.rest.api.v2010.account.call.feedback_summary.FeedbackSummaryList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid,  }
        self._uri = '/Accounts/{account_sid}/Calls/FeedbackSummary.json'.format(**self._solution)
        
        
    
    
    
    def create(self, start_date, end_date, include_subaccounts=values.unset, status_callback=values.unset, status_callback_method=values.unset):
        """
        Create the FeedbackSummaryInstance

        :param date start_date: Only include feedback given on or after this date. Format is `YYYY-MM-DD` and specified in UTC.
        :param date end_date: Only include feedback given on or before this date. Format is `YYYY-MM-DD` and specified in UTC.
        :param bool include_subaccounts: Whether to also include Feedback resources from all subaccounts. `true` includes feedback from all subaccounts and `false`, the default, includes feedback from only the specified account.
        :param str status_callback: The URL that we will request when the feedback summary is complete.
        :param str status_callback_method: The HTTP method (`GET` or `POST`) we use to make the request to the `StatusCallback` URL.
        
        :returns: The created FeedbackSummaryInstance
        :rtype: twilio.rest.api.v2010.account.call.feedback_summary.FeedbackSummaryInstance
        """
        data = values.of({ 
            'StartDate': serialize.iso8601_date(start_date),
            'EndDate': serialize.iso8601_date(end_date),
            'IncludeSubaccounts': include_subaccounts,
            'StatusCallback': status_callback,
            'StatusCallbackMethod': status_callback_method,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return FeedbackSummaryInstance(self._version, payload, account_sid=self._solution['account_sid'])
    

    def get(self, sid):
        """
        Constructs a FeedbackSummaryContext
        
        :param sid: A 34 character string that uniquely identifies this resource.
        
        :returns: twilio.rest.api.v2010.account.call.feedback_summary.FeedbackSummaryContext
        :rtype: twilio.rest.api.v2010.account.call.feedback_summary.FeedbackSummaryContext
        """
        return FeedbackSummaryContext(self._version, account_sid=self._solution['account_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a FeedbackSummaryContext
        
        :param sid: A 34 character string that uniquely identifies this resource.
        
        :returns: twilio.rest.api.v2010.account.call.feedback_summary.FeedbackSummaryContext
        :rtype: twilio.rest.api.v2010.account.call.feedback_summary.FeedbackSummaryContext
        """
        return FeedbackSummaryContext(self._version, account_sid=self._solution['account_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.FeedbackSummaryList>'

class FeedbackSummaryInstance(InstanceResource):

    class Status(object):
        QUEUED = "queued"
        IN_PROGRESS = "in-progress"
        COMPLETED = "completed"
        FAILED = "failed"

    def __init__(self, version, payload, account_sid: str, sid: str=None):
        """
        Initialize the FeedbackSummaryInstance
        :returns: twilio.rest.api.v2010.account.call.feedback_summary.FeedbackSummaryInstance
        :rtype: twilio.rest.api.v2010.account.call.feedback_summary.FeedbackSummaryInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'call_count': deserialize.integer(payload.get('call_count')),
            'call_feedback_count': deserialize.integer(payload.get('call_feedback_count')),
            'date_created': deserialize.rfc2822_datetime(payload.get('date_created')),
            'date_updated': deserialize.rfc2822_datetime(payload.get('date_updated')),
            'end_date': deserialize.iso8601_date(payload.get('end_date')),
            'include_subaccounts': payload.get('include_subaccounts'),
            'issues': payload.get('issues'),
            'quality_score_average': deserialize.decimal(payload.get('quality_score_average')),
            'quality_score_median': deserialize.decimal(payload.get('quality_score_median')),
            'quality_score_standard_deviation': deserialize.decimal(payload.get('quality_score_standard_deviation')),
            'sid': payload.get('sid'),
            'start_date': deserialize.iso8601_date(payload.get('start_date')),
            'status': payload.get('status'),
        }

        self._context = None
        self._solution = { 'account_sid': account_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: FeedbackSummaryContext for this FeedbackSummaryInstance
        :rtype: twilio.rest.api.v2010.account.call.feedback_summary.FeedbackSummaryContext
        """
        if self._context is None:
            self._context = FeedbackSummaryContext(self._version, account_sid=self._solution['account_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def call_count(self):
        """
        :returns: The total number of calls.
        :rtype: int
        """
        return self._properties['call_count']
    
    @property
    def call_feedback_count(self):
        """
        :returns: The total number of calls with a feedback entry.
        :rtype: int
        """
        return self._properties['call_feedback_count']
    
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
    def end_date(self):
        """
        :returns: The last date for which feedback entries are included in this Feedback Summary, formatted as `YYYY-MM-DD` and specified in UTC.
        :rtype: date
        """
        return self._properties['end_date']
    
    @property
    def include_subaccounts(self):
        """
        :returns: Whether the feedback summary includes subaccounts; `true` if it does, otherwise `false`.
        :rtype: bool
        """
        return self._properties['include_subaccounts']
    
    @property
    def issues(self):
        """
        :returns: A list of issues experienced during the call. The issues can be: `imperfect-audio`, `dropped-call`, `incorrect-caller-id`, `post-dial-delay`, `digits-not-captured`, `audio-latency`, or `one-way-audio`.
        :rtype: list[object]
        """
        return self._properties['issues']
    
    @property
    def quality_score_average(self):
        """
        :returns: The average QualityScore of the feedback entries.
        :rtype: float
        """
        return self._properties['quality_score_average']
    
    @property
    def quality_score_median(self):
        """
        :returns: The median QualityScore of the feedback entries.
        :rtype: float
        """
        return self._properties['quality_score_median']
    
    @property
    def quality_score_standard_deviation(self):
        """
        :returns: The standard deviation of the quality scores.
        :rtype: float
        """
        return self._properties['quality_score_standard_deviation']
    
    @property
    def sid(self):
        """
        :returns: A 34 character string that uniquely identifies this resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def start_date(self):
        """
        :returns: The first date for which feedback entries are included in this feedback summary, formatted as `YYYY-MM-DD` and specified in UTC.
        :rtype: date
        """
        return self._properties['start_date']
    
    @property
    def status(self):
        """
        :returns: 
        :rtype: Status
        """
        return self._properties['status']
    
    def delete(self):
        """
        Deletes the FeedbackSummaryInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the FeedbackSummaryInstance
        

        :returns: The fetched FeedbackSummaryInstance
        :rtype: twilio.rest.api.v2010.account.call.feedback_summary.FeedbackSummaryInstance
        """
        return self._proxy.fetch()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.FeedbackSummaryInstance {}>'.format(context)

class FeedbackSummaryContext(InstanceContext):

    def __init__(self, version: Version, account_sid: str, sid: str):
        """
        Initialize the FeedbackSummaryContext

        :param Version version: Version that contains the resource
        :param account_sid: The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.:param sid: A 34 character string that uniquely identifies this resource.

        :returns: twilio.rest.api.v2010.account.call.feedback_summary.FeedbackSummaryContext
        :rtype: twilio.rest.api.v2010.account.call.feedback_summary.FeedbackSummaryContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'account_sid': account_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/Calls/FeedbackSummary/{sid}.json'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the FeedbackSummaryInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the FeedbackSummaryInstance
        

        :returns: The fetched FeedbackSummaryInstance
        :rtype: twilio.rest.api.v2010.account.call.feedback_summary.FeedbackSummaryInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return FeedbackSummaryInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.FeedbackSummaryContext {}>'.format(context)


