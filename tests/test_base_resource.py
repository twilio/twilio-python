# -*- coding: utf-8 -*-
from datetime import datetime
import unittest

from mock import Mock, sentinel, patch, ANY
from nose.tools import assert_equal, assert_true
import pytz
from six import advance_iterator

from twilio.rest.resources.imports import json
from twilio.rest.resources import Resource, NextGenListResource, NextGenInstanceResource
from twilio.rest.resources import ListResource
from twilio.rest.resources import InstanceResource

base_uri = "https://api.twilio.com/2010-04-01"
account_sid = "AC123"
auth = (account_sid, "token")


def test_resource_init():
    r = Resource(base_uri, auth)
    uri = "%s/%s" % (base_uri, r.name)

    assert_equal(r.base_uri, base_uri)
    assert_equal(r.auth, auth)
    assert_equal(r.uri, uri)


def test_equivalence():
    p = ListResource(base_uri, auth)
    r1 = p.load_instance({"sid": "AC123"})
    r2 = p.load_instance({"sid": "AC123"})
    assert_equal(r1, r2)


class ListResourceTest(unittest.TestCase):

    def setUp(self):
        self.r = ListResource(base_uri, auth)

    def testListResourceInit(self):
        uri = "%s/%s" % (base_uri, self.r.name)
        assert_equal(self.r.uri, uri)
        assert_equal(str(self.r), "<ListResource>")

    def testKeyValueLower(self):
        assert_equal(self.r.key, self.r.name.lower())

    def testIterNoKey(self):
        self.r.request = Mock()
        self.r.request.return_value = Mock(), {}

        self.assertRaises(StopIteration, advance_iterator, self.r.iter())

    def testRequest(self):
        self.r.request = Mock()
        self.r.request.return_value = Mock(), {self.r.key: [{'sid': 'foo'}]}
        advance_iterator(self.r.iter())
        self.r.request.assert_called_with("GET", "https://api.twilio.com/2010-04-01/Resources", params={})

    def testIterOneItem(self):
        self.r.request = Mock()
        self.r.request.return_value = Mock(), {self.r.key: [{'sid': 'foo'}]}

        items = self.r.iter()
        advance_iterator(items)

        self.assertRaises(StopIteration, advance_iterator, items)

    def testIterNoNextPage(self):
        self.r.request = Mock()
        self.r.request.return_value = Mock(), {self.r.key: []}

        self.assertRaises(StopIteration, advance_iterator, self.r.iter())

    def testKeyValue(self):
        self.r.key = "Hey"
        assert_equal(self.r.key, "Hey")

    def testInstanceLoading(self):
        instance = self.r.load_instance({"sid": "foo"})

        assert_true(isinstance(instance, InstanceResource))
        assert_equal(instance.sid, "foo")

    def testListResourceCreateResponse200(self):
        """We should accept 200 OK in response to a POST creating a resource."""
        self.r.request = Mock()
        return_value = Mock()
        return_value.status_code = 200
        self.r.request.return_value = return_value, {'sid': 'foo'}
        self.r.create_instance({})
        self.r.request.assert_called_with("POST", "https://api.twilio.com/2010-04-01/Resources", data={})

    def testListResourceCreateResponse201(self):
        """We should accept 201 Created in response to a POST creating a resource."""
        self.r.request = Mock()
        return_value = Mock()
        return_value.status_code = 201
        self.r.request.return_value = return_value, {'sid': 'foo'}
        self.r.create_instance({})
        self.r.request.assert_called_with("POST", "https://api.twilio.com/2010-04-01/Resources", data={})


class NextGenListResourceTest(unittest.TestCase):

    def setUp(self):
        self.r = NextGenListResource(base_uri, auth)

    def test_list_resource_init(self):
        uri = "%s/%s" % (base_uri, self.r.name)
        assert_equal(self.r.uri, uri)

    def test_iter_no_key(self):
        self.r.request = Mock()
        self.r.request.return_value = Mock(), {}

        self.assertRaises(StopIteration, advance_iterator, self.r.iter())

    def test_iter_key_not_present(self):
        self.r.request = Mock()
        self.r.request.return_value = Mock(), {'meta': {'key': 'foobars'}}

    def test_iter_request(self):
        self.r.request = Mock()
        self.r.request.return_value = Mock(), {'meta': {'key': 'foos'}, 'foos': [{'sid': '123'}]}
        item = advance_iterator(self.r.iter())
        self.r.request.assert_called_with("GET", "https://api.twilio.com/2010-04-01/Resources")
        assert_equal(item.sid, '123')

    def test_iter_one_item(self):
        self.r.request = Mock()
        self.r.request.return_value = Mock(), {'meta': {'key': 'foos', 'next_page_url': None}, 'foos': [{'sid': '123'}]}

        items = self.r.iter()
        advance_iterator(items)

        self.assertRaises(StopIteration, advance_iterator, items)

    def test_instance_loading(self):
        instance = self.r.load_instance({"sid": "foo"})

        assert_true(isinstance(instance, NextGenInstanceResource))
        assert_equal(instance.sid, "foo")


class testInstanceResourceInit(unittest.TestCase):

    def setUp(self):
        self.parent = ListResource(base_uri, auth)
        self.r = InstanceResource(self.parent, "123")
        self.uri = "%s/%s" % (self.parent.uri, "123")

    def testInit(self):
        assert_equal(self.r.uri, self.uri)

    def testLoad(self):
        self.r.load({"hey": "you"})
        assert_equal(self.r.hey, "you")

    def testLoadWithUri(self):
        self.r.load({"hey": "you", "uri": "foobar"})
        assert_equal(self.r.hey, "you")
        assert_equal(self.r.uri, self.uri)

    def testLoadDateCreated(self):
        self.r.load({"date_created": "Sat, 29 Sep 2012 12:47:54 +0000",
                     "uri": "foobar"})
        try:
            assert_true(hasattr(self.r.date_created, "day"))
            assert_equal(self.r.date_created.day, 29)
        except AttributeError:
            pass

    def testLoadNullDate(self):
        self.r.load({"date_created": None, "uri": "foobar"})
        assert self.r.date_created is None

    def testLoadWithFrom(self):
        self.r.load({"from": "foo"})
        assert_equal(self.r.from_, "foo")

    def testLoadSubresources(self):
        m = Mock()
        self.r.subresources = [m]
        self.r.load_subresources()
        m.assert_called_with(self.r.uri, self.r.auth, self.r.timeout)


class NextGenInstanceResourceTest(unittest.TestCase):
    def setUp(self):
        self.parent = NextGenListResource(base_uri, auth)
        self.r = NextGenInstanceResource(self.parent, "123")

    def test_load(self):
        self.r.load({"hey": "you"})
        assert_equal(self.r.hey, "you")

    def test_iso_date_parser(self):
        self.r.load({"date_created": "2015-01-01T00:00:00Z"})
        assert_equal(
            self.r.date_created,
            datetime(2015, 1, 1, 0, 0, 0, tzinfo=pytz.utc),
        )


class testTimeoutPropagation(unittest.TestCase):
    def setUp(self):
        self.parent = ListResource(base_uri, auth, timeout=sentinel.timeout)
        self.r = InstanceResource(self.parent, "123")
        self.uri = "%s/%s" % (self.parent.uri, "123")

    @patch('twilio.rest.resources.base.make_request')
    def testPassThrough(self, mock_request):
        mock_response = Mock()
        mock_response.ok = True,
        mock_response.content = json.dumps({'key': 'value'})
        mock_request.return_value = mock_response

        assert_equal(self.r.timeout, sentinel.timeout)
        assert_equal((mock_response, {'key': 'value'}), self.r.request('GET', base_uri))

        mock_request.assert_called_once_with(
            'GET',
            base_uri + '.json',
            headers=ANY,
            timeout=sentinel.timeout,
            auth=ANY
        )
