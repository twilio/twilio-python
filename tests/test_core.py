from datetime import datetime
from datetime import date
import unittest

from nose.tools import assert_equal

from twilio.rest.resources import parse_date
from twilio.rest.resources import transform_params
from twilio.rest.resources import convert_keys
from twilio.rest.resources import convert_case
from twilio.rest.resources import convert_boolean
from twilio.rest.resources import normalize_dates


class CoreTest(unittest.TestCase):

    def test_date(self):
        d = date(2009, 10, 10)
        assert_equal(parse_date(d), "2009-10-10")

    def test_datetime(self):
        d = datetime(2009, 10, 10)
        assert_equal(parse_date(d), "2009-10-10")

    def test_string_date(self):
        d = "2009-10-10"
        assert_equal(parse_date(d), "2009-10-10")

    def test_string_date_none(self):
        d = None
        assert_equal(parse_date(d), None)

    def test_string_date_false(self):
        d = False
        assert_equal(parse_date(d), None)

    def test_fparam(self):
        d = {"HEY": None, "YOU": 3}
        ed = {"YOU": 3}
        assert_equal(transform_params(d), ed)

    def test_multi_param(self):
        d = {"Normal": 3, "Multiple": ["One", "Two"]}
        ed = {"Normal": 3, "Multiple": ["One", "Two"]}
        assert_equal(transform_params(d), ed)

    def test_fparam_booleans(self):
        d = {"HEY": None, "YOU": 3, "Activated": False}
        ed = {"YOU": 3, "Activated": "false"}
        assert_equal(transform_params(d), ed)

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

        assert_equal(d["on"], "2009-10-10")
        assert_equal(d["after"], "2009-10-10")
        assert_equal(d["before"], "2009-10-10")

    def test_convert_case(self):
        assert_equal(convert_case("from_"), "From")
        assert_equal(convert_case("to"), "To")
        assert_equal(convert_case("friendly_name"), "FriendlyName")

    def test_convert_bool(self):
        assert_equal(convert_boolean(False), "false")
        assert_equal(convert_boolean(True), "true")
        assert_equal(convert_boolean(1), 1)

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

        assert_equal(ed, convert_keys(d))
