import datetime


def transform_params(p):
    """
    Transform parameters, throwing away any None values
    and convert False and True values to strings

    Ex:
    {"record": true, "date_created": "2012-01-02"}

    becomes:
    {"Record": "true", "DateCreated": "2012-01-02"}
    """
    p = [(format_name(d), convert_boolean(p[d])) for d in p
         if p[d] is not None
    ]
    return dict(p)


def format_name(word):
    if word.lower() == word:
        return convert_case(word)
    else:
        return word


def parse_date(d):
    """
    Return a string representation of a date that the Twilio API understands
    Format is YYYY-MM-DD. Returns None if d is not a string, datetime, or date
    """
    if isinstance(d, datetime.datetime):
        return str(d.date())
    elif isinstance(d, datetime.date):
        return str(d)
    elif isinstance(d, str):
        return d


def convert_boolean(boolean):
    if isinstance(boolean, bool):
        return 'true' if boolean else 'false'
    return boolean


def convert_case(s):
    """
    Given a string in snake case, convert to CamelCase

    Ex:
    date_created -> DateCreated
    """
    return ''.join([a.title() for a in s.split("_") if a])


def convert_keys(d):
    """
    Return a dictionary with all keys converted from arguments
    """
    special = {
        "started_before": "StartTime<",
        "started_after":  "StartTime>",
        "started":        "StartTime",
        "ended_before":   "EndTime<",
        "ended_after":    "EndTime>",
        "ended":          "EndTime",
        "from_":          "From",
    }

    result = {}

    for k, v in d.iteritems():
        if k in special:
            result[special[k]] = v
        else:
            result[convert_case(k)] = v

    return result


def normalize_dates(myfunc):
    def inner_func(*args, **kwargs):
        for k, v in kwargs.iteritems():
            res = [True for s in ["after", "before", "on"] if s in k]
            if len(res):
                kwargs[k] = parse_date(v)
        return myfunc(*args, **kwargs)
    inner_func.__doc__ = myfunc.__doc__
    inner_func.__repr__ = myfunc.__repr__
    return inner_func
