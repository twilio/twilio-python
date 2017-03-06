import datetime

from twilio.base import values


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


def prefixed_collapsible_map(m, prefix):
    """
    Return a dict of params corresponding to those in m with the added prefix
    """
    if m == values.unset:
        return {}

    def flatten_dict(d, result={}, prv_keys=[]):
        for k, v in d.items():
            if isinstance(v, dict):
                flatten_dict(v, result, prv_keys + [k])
            else:
                result['.'.join(prv_keys + [k])] = v

        return result

    if isinstance(m, dict):
        flattened = flatten_dict(m)
        return {'{}.{}'.format(prefix, k): v for k, v in flattened.items()}

    return {}
