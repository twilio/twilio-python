import six
if six.PY3:
    import unittest
else:
    import unittest2 as unittest
from datetime import datetime
from datetime import date
from twilio.rest.resources import parse_date
from twilio.rest.resources import transform_params
from twilio.rest.resources import convert_keys
from twilio.rest.resources import convert_case
from twilio.rest.resources import convert_boolean
from twilio.rest.resources import normalize_dates


class CoreTest(unittest.TestCase):

    def test_date(self):
        d = date(2009, 10, 10)
        self.assertEquals(parse_date(d), "2009-10-10")

    def test_datetime(self):
        d = datetime(2009, 10, 10)
        self.assertEquals(parse_date(d), "2009-10-10")

    def test_string_date(self):
        d = "2009-10-10"
        self.assertEquals(parse_date(d), "2009-10-10")

    def test_string_date_none(self):
        d = None
        self.assertEquals(parse_date(d), None)

    def test_string_date_false(self):
        d = False
        self.assertEquals(parse_date(d), None)

    def test_fparam(self):
        d = {"HEY": None, "YOU": 3}
        ed = {"YOU": 3}
        self.assertEquals(transform_params(d), ed)

    def test_multi_param(self):
        d = {"Normal": 3, "Multiple": ["One", "Two"]}
        ed = {"Normal": 3, "Multiple": ["One", "Two"]}
        self.assertEquals(transform_params(d), ed)

    def test_fparam_booleans(self):
        d = {"HEY": None, "YOU": 3, "Activated": False}
        ed = {"YOU": 3, "Activated": "false"}
        self.assertEquals(transform_params(d), ed)

    def test_normalize_dates(self):

        @normalize_dates
        def foo(on=None, before=None, after=None):
            return {
                "on": on,
                "before": before,
                "after": after,
            }

        d = foo(on="2009-10-10", before=date(2009, 10, 10),
                after=datetime(2009, 10, 10))

        self.assertEquals(d["on"], "2009-10-10")
        self.assertEquals(d["after"], "2009-10-10")
        self.assertEquals(d["before"], "2009-10-10")

    def test_convert_case(self):
        self.assertEquals(convert_case("from_"), "From")
        self.assertEquals(convert_case("to"), "To")
        self.assertEquals(convert_case("friendly_name"), "FriendlyName")

    def test_convert_bool(self):
        self.assertEquals(convert_boolean(False), "false")
        self.assertEquals(convert_boolean(True), "true")
        self.assertEquals(convert_boolean(1), 1)

    def test_convert_keys(self):
        d = {
            "from_": 0,
            "to": 0,
            "friendly_name": 0,
            "ended": 0,
        }

        ed = {
            "From": 0,
            "To": 0,
            "FriendlyName": 0,
            "EndTime": 0,
        }

        self.assertEquals(ed, convert_keys(d))
