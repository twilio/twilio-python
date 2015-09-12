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
from twilio.rest.resources.base import GetQuery
from twilio.rest.resources.base import UpdateQuery


class Feedback(InstanceResource):
    """
    .. attribute:: account_sid
    
        The account_sid
    
    .. attribute:: date_created
    
        The date_created
    
    .. attribute:: date_updated
    
        The date_updated
    
    .. attribute:: issues
    
        The issues
    
    .. attribute:: quality_score
    
        1 to 5 quality score where 1 represents imperfect experience and 5
        represents a perfect call
    
    .. attribute:: sid
    
        The sid
    """
    id_key = "sid"
    AUDIO_LATENCY = "audio-latency"
    DIGITS_NOT_CAPTURED = "digits-not-captured"
    DROPPED_CALL = "dropped-call"
    IMPERFECT_AUDIO = "imperfect-audio"
    INCORRECT_CALLER_ID = "incorrect-caller-id"
    ONE_WAY_AUDIO = "one-way-audio"
    POST_DIAL_DELAY = "post-dial-delay"
    UNSOLICITED_CALL = "unsolicited-call"

    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        super(Feedback, self).__init__(parent, None)

    def load(self, *args, **kwargs):
        super(Feedback, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)

    def update(self, **kwargs):
        """
        Create or update a feedback entry for a call
        
        :param feedback.issues issue: One or more of the issues experienced during the
            call
        :param str quality_scored: The quality_scored
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns a new instance of the updated :class:`Feedback`
        """
        return self.update_instance(kwargs)


class Feedbacks(ListResource):
    name = "Feedback"
    mount_name = "feedback"
    key = "feedback"
    instance = Feedback

    def __init__(self, *args, **kwargs):
        super(Feedbacks, self).__init__(*args, **kwargs)

    def create(self, quality_score, **kwargs):
        """
        Create a new :class:`Feedback`
        
        :param feedback.issues issue: The issue
        :param str quality_score: The quality_score
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`CreateQuery`
        :returns: A CreateQuery when executed returns an instance of the created :class:`Feedback`
        """
        kwargs["QualityScore"] = quality_score
        return self.create_instance(kwargs)

    def get(self, **kwargs):
        """ Get the Feedback """
        return GetQuery(self, self.uri, self.use_json_extension,
                        params=kwargs)

    def update(self, quality_scored, **kwargs):
        """
        Create or update a feedback entry for a call
        
        :param feedback.issues issue: One or more of the issues experienced during the
            call
        :param str quality_scored: The quality_scored
        
        :raises TwilioRestException: when the request fails on execute
        """
        kwargs["QualityScored"] = quality_scored
        return UpdateQuery(self, self.uri, kwargs,
            self.use_json_extension)

    def load_instance(self, data):
        """ Override because Feedback does not have a sid """
        instance = self.instance(self)
        instance.load(data)
        instance.load_subresources()
        return instance
