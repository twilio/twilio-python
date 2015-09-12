# coding=utf-8
"""
__  __                      __
\ \/ /___  __  ______  ____/ /_  ______  ___
 \  / __ \/ / / / __ \/ __  / / / / __ \/ _ \
 / / /_/ / /_/ / /_/ / /_/ / /_/ / / / /  __/
/_/\____/\__. /\____/\__._/\__. /_/ /_/\___/      version 0.0.1
        /____/            /____/
"""

from twilio.rest.resources.util import (
    parse_date,
    parse_iso_date,
)
from twilio.rest.resources.base import InstanceResource
from twilio.rest.resources.base import ListResource


class FeedbackSummary(InstanceResource):
    """
    .. attribute:: account_sid
    
        The account_sid
    
    .. attribute:: call_count
    
        The call_count
    
    .. attribute:: call_feedback_count
    
        The call_feedback_count
    
    .. attribute:: date_created
    
        The date_created
    
    .. attribute:: date_updated
    
        The date_updated
    
    .. attribute:: end_date
    
        The end_date
    
    .. attribute:: include_subaccounts
    
        The include_subaccounts
    
    .. attribute:: issues
    
        The issues
    
    .. attribute:: quality_score_average
    
        The quality_score_average
    
    .. attribute:: quality_score_median
    
        The quality_score_median
    
    .. attribute:: quality_score_standard_deviation
    
        The quality_score_standard_deviation
    
    .. attribute:: sid
    
        The sid
    
    .. attribute:: start_date
    
        The start_date
    
    .. attribute:: status
    
        The status
    """
    id_key = "sid"
    COMPLETED = "completed"
    FAILED = "failed"
    IN_PROGRESS = "in-progress"
    QUEUED = "queued"

    def load(self, *args, **kwargs):
        super(FeedbackSummary, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)
        
        if hasattr(self, "end_date") and self.end_date:
            self.end_date = parse_iso_date(self.end_date)
        
        if hasattr(self, "start_date") and self.start_date:
            self.start_date = parse_iso_date(self.start_date)

    def delete(self):
        """
        Delete the instance
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance()


class FeedbackSummaries(ListResource):
    name = "Calls/FeedbackSummary"
    mount_name = "feedback_summaries"
    key = "feedback_summaries"
    instance = FeedbackSummary

    def __init__(self, *args, **kwargs):
        super(FeedbackSummaries, self).__init__(*args, **kwargs)

    def create(self, start_date, end_date, **kwargs):
        """
        Create a new :class:`FeedbackSummary`
        
        :param bool include_subaccounts: The include_subaccounts
        :param date end_date: The end_date
        :param date start_date: The start_date
        :param str status_callback: The status_callback
        :param str status_callback_method: The status_callback_method
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`CreateQuery`
        :returns: A CreateQuery when executed returns an instance of the created :class:`FeedbackSummary`
        """
        kwargs["StartDate"] = parse_date(start_date)
        kwargs["EndDate"] = parse_date(end_date)
        return self.create_instance(kwargs)

    def get(self, sid):
        """
        Get a placeholder for an instance resource.
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`FeedbackSummary`
        :returns: A placeholder for a :class:`FeedbackSummary` resource
        """
        return self.get_instance(sid)

    def delete(self, sid):
        """
        Delete the :class:`FeedbackSummary`
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance(sid)
