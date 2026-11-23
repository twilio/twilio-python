import datetime
import json

from twilio.base import values
from twilio.base.exceptions import TwilioException

_INVALID_PATH_PARAM_MESSAGE = (
    "Invalid path parameter: must not be empty, '.', '..' "
    "or contain '/', '?', '#': {!r}"
)


def validate_path_param(value):
    """
    Validate a value that will be interpolated into a URL path segment.

    Rejects values that could change the target endpoint: None, empty,
    '.', '..', or anything containing '/', '?' or '#'. Non-string values
    are converted with str().

    :param value: the path parameter value
    :return: the value as a str, unchanged
    :raises TwilioException: if the value is not a safe path segment
    """
    if value is None:
        raise TwilioException(_INVALID_PATH_PARAM_MESSAGE.format(value))
    value = str(value)
    if value in ("", ".", "..") or "/" in value or "?" in value or "#" in value:
        raise TwilioException(_INVALID_PATH_PARAM_MESSAGE.format(value))
    return value


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
        return d.strftime("%Y-%m-%dT%H:%M:%SZ")
    elif isinstance(d, str):
        return d


def prefixed_collapsible_map(m, prefix):
    """
    Return a dict of params corresponding to those in m with the added prefix
    """
    if m == values.unset:
        return {}

    def flatten_dict(d, result=None, prv_keys=None):
        if result is None:
            result = {}

        if prv_keys is None:
            prv_keys = []

        for k, v in d.items():
            if isinstance(v, dict):
                flatten_dict(v, result, prv_keys + [k])
            else:
                result[".".join(prv_keys + [k])] = v

        return result

    if isinstance(m, dict):
        flattened = flatten_dict(m)
        return {"{}.{}".format(prefix, k): v for k, v in flattened.items()}

    return {}


def boolean_to_string(bool_or_str):
    if bool_or_str == values.unset:
        return bool_or_str

    if bool_or_str is None:
        return bool_or_str

    if isinstance(bool_or_str, str):
        return bool_or_str.lower()

    return "true" if bool_or_str else "false"


def object(obj):
    """
    Return a jsonified string represenation of obj if obj is jsonifiable else
    return obj untouched
    """
    if isinstance(obj, dict) or isinstance(obj, list):
        return json.dumps(obj)
    return obj


def map(lst, serialize_func):
    """
    Applies serialize_func to every element in lst
    """
    if not isinstance(lst, list):
        return lst
    return [serialize_func(e) for e in lst]
