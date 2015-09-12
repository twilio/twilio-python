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
from twilio.rest.v2010.account.usage.record.all_time import (
    AllTimes,
    AllTime,
)
from twilio.rest.v2010.account.usage.record.daily import (
    Dailies,
    Daily,
)
from twilio.rest.v2010.account.usage.record.last_month import (
    LastMonths,
    LastMonth,
)
from twilio.rest.v2010.account.usage.record.monthly import (
    Monthlies,
    Monthly,
)
from twilio.rest.v2010.account.usage.record.this_month import (
    ThisMonths,
    ThisMonth,
)
from twilio.rest.v2010.account.usage.record.today import (
    Todays,
    Today,
)
from twilio.rest.v2010.account.usage.record.yearly import (
    Yearlies,
    Yearly,
)
from twilio.rest.v2010.account.usage.record.yesterday import (
    Yesterdays,
    Yesterday,
)


class Record(InstanceResource):
    """
    .. attribute:: account_sid
    
        The Account that accrued the usage
    
    .. attribute:: api_version
    
        The api_version
    
    .. attribute:: category
    
        The category of usage
    
    .. attribute:: count
    
        The number of usage events (e.g. the number of calls).
    
    .. attribute:: count_unit
    
        The units in which `Count` is measured.  For example `calls` for calls,
        `messages` for SMS.
    
    .. attribute:: description
    
        A human-readable description of the usage category.
    
    .. attribute:: end_date
    
        The last date for which usage is included in this UsageRecord, formatted
        as YYYY-MM-DD.  All dates are in GMT.
    
    .. attribute:: price
    
        The total price of the usage, in the currency associated with the
        account.
    
    .. attribute:: price_unit
    
        The currency in which `Price` is measured, in ISO 4127 format (e.g.
        `usd`, `eur`, `jpy`).
    
    .. attribute:: start_date
    
        The first date for which usage is included in this UsageRecord,
        formatted as YYYY-MM-DD.  All dates are in GMT.
    
    .. attribute:: subresource_uris
    
        Subresource Uris for this UsageRecord
    
    .. attribute:: uri
    
        The URI that returns only this UsageRecord, relative to
        `https://api.twilio.com`.
    
    .. attribute:: usage
    
        The amount of usage (e.g. the number of call minutes).  This is
        frequently the same as `Count`, but may be different for certain usage
        categories like calls, where `Count` represents the number of calls and
        `Usage` represents the number of minutes.
    
    .. attribute:: usage_unit
    
        The units in which `Usage` is measured.  For example `minutes` for
        calls, `messages` for SMS.
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
        super(Record, self).__init__(parent, None)

    def load(self, *args, **kwargs):
        super(Record, self).load(*args, **kwargs)
        
        if hasattr(self, "end_date") and self.end_date:
            self.end_date = parse_iso_date(self.end_date)
        
        if hasattr(self, "start_date") and self.start_date:
            self.start_date = parse_iso_date(self.start_date)


class Records(ListResource):
    name = "Usage/Records"
    mount_name = "records"
    key = "usage_records"
    instance = Record

    def __init__(self, *args, **kwargs):
        super(Records, self).__init__(*args, **kwargs)
        self.all_time = AllTimes(*args, **kwargs)
        self.daily = Dailies(*args, **kwargs)
        self.last_month = LastMonths(*args, **kwargs)
        self.monthly = Monthlies(*args, **kwargs)
        self.this_month = ThisMonths(*args, **kwargs)
        self.today = Todays(*args, **kwargs)
        self.yearly = Yearlies(*args, **kwargs)
        self.yesterday = Yesterdays(*args, **kwargs)

    def list(self, **kwargs):
        """
        Retrieve a list of usage-records belonging to the account used to make the request
        
        :param date end_date: Only include usage that has occurred on or after this
            date. Format is YYYY-MM-DD in GTM. As a convenience, you can also specify
            offsets to today, for example, EndDate=+30days, which will make EndDate 30 days
            from today
        :param date end_date_after: The end_date>
        :param date end_date_before: The end_date<
        :param date start_date: Only include usage that has occurred on or after this
            date. Format is YYYY-MM-DD in GTM. As a convenience, you can also specify
            offsets to today, for example, StartDate=-30days, which will make StartDate 30
            days before today
        :param date start_date_after: The start_date>
        :param date start_date_before: The start_date<
        :param record.category category: Only include usage of a given category
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`Record`
        """
        if "start_date_before" in kwargs:
            kwargs["StartDate<"] = parse_date(kwargs["start_date_before"])
            del kwargs["start_date_before"]
        if "start_date_after" in kwargs:
            kwargs["StartDate>"] = parse_date(kwargs["start_date_after"])
            del kwargs["start_date_after"]
        if "start_date" in kwargs:
            kwargs["StartDate"] = parse_date(kwargs["start_date"])
            del kwargs["start_date"]
        if "end_date_before" in kwargs:
            kwargs["EndDate<"] = parse_date(kwargs["end_date_before"])
            del kwargs["end_date_before"]
        if "end_date_after" in kwargs:
            kwargs["EndDate>"] = parse_date(kwargs["end_date_after"])
            del kwargs["end_date_after"]
        if "end_date" in kwargs:
            kwargs["EndDate"] = parse_date(kwargs["end_date"])
            del kwargs["end_date"]
        return self.get_instances(kwargs)

    def iter(self, **kwargs):
        """
        Retrieve a list of usage-records belonging to the account used to make the request
        
        :param date end_date: Only include usage that has occurred on or after this
            date. Format is YYYY-MM-DD in GTM. As a convenience, you can also specify
            offsets to today, for example, EndDate=+30days, which will make EndDate 30 days
            from today
        :param date end_date_after: The end_date>
        :param date end_date_before: The end_date<
        :param date start_date: Only include usage that has occurred on or after this
            date. Format is YYYY-MM-DD in GTM. As a convenience, you can also specify
            offsets to today, for example, StartDate=-30days, which will make StartDate 30
            days before today
        :param date start_date_after: The start_date>
        :param date start_date_before: The start_date<
        :param record.category category: Only include usage of a given category
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`Record`
        """
        if "start_date_before" in kwargs:
            kwargs["StartDate<"] = parse_date(kwargs["start_date_before"])
            del kwargs["start_date_before"]
        if "start_date_after" in kwargs:
            kwargs["StartDate>"] = parse_date(kwargs["start_date_after"])
            del kwargs["start_date_after"]
        if "start_date" in kwargs:
            kwargs["StartDate"] = parse_date(kwargs["start_date"])
            del kwargs["start_date"]
        if "end_date_before" in kwargs:
            kwargs["EndDate<"] = parse_date(kwargs["end_date_before"])
            del kwargs["end_date_before"]
        if "end_date_after" in kwargs:
            kwargs["EndDate>"] = parse_date(kwargs["end_date_after"])
            del kwargs["end_date_after"]
        if "end_date" in kwargs:
            kwargs["EndDate"] = parse_date(kwargs["end_date"])
            del kwargs["end_date"]
        return super(Records, self).iter(**kwargs)

    def load_instance(self, data):
        """ Override because Record does not have a sid """
        instance = self.instance(self)
        instance.load(data)
        instance.load_subresources()
        return instance
