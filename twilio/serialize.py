import datetime

from twilio import values


def iso8601_date(d):
    """
    Return a string representation of a date that the Twilio API understands
    Format is YYYY-MM-DD. Returns None if d is not a string, datetime, or date
    """
    if d == values.unset:
        return d
    elif isinstance(d, datetime.datetime):
        return str(d.date())
    elif isinstance(d, datetime.date):
        return str(d)
    elif isinstance(d, str):
        return d


def iso8601_datetime(d):
    """
    Return a string representation of a date that the Twilio API understands
    Format is YYYY-MM-DD. Returns None if d is not a string, datetime, or date
    """
    if d == values.unset:
        return d
    elif isinstance(d, datetime.datetime) or isinstance(d, datetime.date):
        return d.strftime('%Y-%m-%dT%H:%M:%SZ')
    elif isinstance(d, str):
        return d
