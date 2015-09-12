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


class LastMonth(InstanceResource):
    """
    .. attribute:: account_sid
    
        The account_sid
    
    .. attribute:: api_version
    
        The api_version
    
    .. attribute:: category
    
        The category
    
    .. attribute:: count
    
        The count
    
    .. attribute:: count_unit
    
        The count_unit
    
    .. attribute:: description
    
        The description
    
    .. attribute:: end_date
    
        The end_date
    
    .. attribute:: price
    
        The price
    
    .. attribute:: price_unit
    
        The price_unit
    
    .. attribute:: start_date
    
        The start_date
    
    .. attribute:: subresource_uris
    
        The subresource_uris
    
    .. attribute:: uri
    
        The uri
    
    .. attribute:: usage
    
        The usage
    
    .. attribute:: usage_unit
    
        The usage_unit
    """
    id_key = "sid"
    CALLERIDLOOKUPS = "calleridlookups"
    CALLS = "calls"
    CALLS_CLIENT = "calls-client"
    CALLS_INBOUND = "calls-inbound"
    CALLS_INBOUND_LOCAL = "calls-inbound-local"
    CALLS_INBOUND_TOLLFREE = "calls-inbound-tollfree"
    CALLS_OUTBOUND = "calls-outbound"
    CALLS_SIP = "calls-sip"
    PHONENUMBERS = "phonenumbers"
    PHONENUMBERS_LOCAL = "phonenumbers-local"
    PHONENUMBERS_TOLLFREE = "phonenumbers-tollfree"
    RECORDINGS = "recordings"
    RECORDINGSTORAGE = "recordingstorage"
    SHORTCODES = "shortcodes"
    SHORTCODES_CUSTOMEROWNED = "shortcodes-customerowned"
    SHORTCODES_RANDOM = "shortcodes-random"
    SHORTCODES_VANITY = "shortcodes-vanity"
    SMS = "sms"
    SMS_INBOUND = "sms-inbound"
    SMS_INBOUND_LONGCODE = "sms-inbound-longcode"
    SMS_INBOUND_SHORTCODE = "sms-inbound-shortcode"
    SMS_OUTBOUND = "sms-outbound"
    SMS_OUTBOUND_LONGCODE = "sms-outbound-longcode"
    SMS_OUTBOUND_SHORTCODE = "sms-outbound-shortcode"
    TOTALPRICE = "totalprice"
    TRANSCRIPTIONS = "transcriptions"

    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        super(LastMonth, self).__init__(parent, None)

    def load(self, *args, **kwargs):
        super(LastMonth, self).load(*args, **kwargs)
        
        if hasattr(self, "end_date") and self.end_date:
            self.end_date = parse_iso_date(self.end_date)
        
        if hasattr(self, "start_date") and self.start_date:
            self.start_date = parse_iso_date(self.start_date)


class LastMonths(ListResource):
    name = "Usage/Records/LastMonth"
    mount_name = "last_month"
    key = "usage_records"
    instance = LastMonth

    def __init__(self, *args, **kwargs):
        super(LastMonths, self).__init__(*args, **kwargs)

    def list(self, **kwargs):
        """
        Retrieve a collection of :class:`LastMonth`
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`LastMonth`
        """
        return self.get_instances(kwargs)

    def iter(self, **kwargs):
        """
        Return all instances of :class:`LastMonth` using an iterator
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`LastMonth`
        """
        return super(LastMonths, self).iter(**kwargs)

    def load_instance(self, data):
        """ Override because LastMonth does not have a sid """
        instance = self.instance(self)
        instance.load(data)
        instance.load_subresources()
        return instance
