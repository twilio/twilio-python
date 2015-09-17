import datetime
import pytz


def iso8601_datetime(s):
    """
    Parses an ISO 8601 date string and returns a UTC datetime object,
    or the string if parsing failed.
    :param s: ISO 8601-formatted string date
    :return: datetime or str
    """
    format = "%Y-%m-%dT%H:%M:%SZ"
    try:
        return datetime.datetime.strptime(s, format).replace(tzinfo=pytz.utc)
    except ValueError:
        return s
