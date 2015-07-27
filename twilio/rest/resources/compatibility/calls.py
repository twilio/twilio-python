from twilio.rest.resources.base import ListResource, InstanceResource
from twilio.rest.resources.call_feedback import CallFeedbackFactory
from twilio.rest.resources.call_feedback_summary import CallFeedbackSummary


class Call(InstanceResource):
    pass


class Calls(ListResource):

    def __init__(self, *args, **kwargs):
        super(Calls, self).__init__(*args, **kwargs)
        self.summary = CallFeedbackSummary(*args, **kwargs)

    def feedback(self, sid, quality_score, issue=None):
        """ Create feedback for the given call.

        :param sid: A Call Sid for a specific call
        :param quality_score: The quality of the call
        :param issue: A list of issues experienced during the call
        :returns: A :class:`CallFeedback` object
        """
        uri = "%s/%s" % (self.uri, sid)
        call_feedback_factory = CallFeedbackFactory(
            uri, self.auth, self.timeout
        )
        return call_feedback_factory.create(
            quality_score=quality_score, issue=issue
        )
