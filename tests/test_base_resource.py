# -*- coding: utf-8 -*-
from datetime import datetime
import unittest

from mock import Mock, patch
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
    r = Resource(Mock(), base_uri, auth)
    uri = "%s/%s" % (base_uri, r.name)

    assert_equal(r.base_uri, base_uri)
    assert_equal(r.auth, auth)
    assert_equal(r.uri, uri)


class ListResourceTest(unittest.TestCase):

    def setUp(self):
        self.client = Mock()
        self.r = ListResource(self.client, base_uri, auth)

    def testListResourceInit(self):
        uri = "%s/%s" % (base_uri, self.r.name)
        assert_equal(self.r.uri, uri)
        assert_equal(str(self.r), "<ListResource>")

    def testKeyValueLower(self):
        assert_equal(self.r.key, self.r.name.lower())

    @patch('twilio.rest.resources.base.make_twilio_request')
    def testIterNoKey(self, mock):
        resp = Mock()
        resp.status_code = 200
        resp.content = "{}"
        mock.return_value = resp

        self.assertRaises(StopIteration, advance_iterator, self.r.iter())

    @patch('twilio.rest.resources.base.make_twilio_request')
    def testRequest(self, mock):
        resp = Mock()
        resp.status_code = 200
        resp.content = json.dumps({self.r.key: [{'sid': 'foo'}]})
        mock.return_value = resp

        advance_iterator(self.r.iter())

        mock.assert_called_with("GET", "https://api.twilio.com/2010-04-01/Resources",
                                auth=auth, use_json_extension=True,
                                client=self.client)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def testIterOneItem(self, mock):
        resp = Mock()
        resp.status_code = 200
        resp.content = json.dumps({self.r.key: [{'sid': 'foo'}]})
        mock.return_value = resp

        items = self.r.iter()
        advance_iterator(items)

        self.assertRaises(StopIteration, advance_iterator, items)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def testIterNoNextPage(self, mock):
        resp = Mock()
        resp.status_code = 200
        resp.content = json.dumps({self.r.key: []})
        mock.return_value = resp

        self.assertRaises(StopIteration, advance_iterator, self.r.iter())

    def testKeyValue(self):
        self.r.key = "Hey"
        assert_equal(self.r.key, "Hey")

    def testInstanceLoading(self):
        instance = self.r.load_instance({"sid": "foo"})

        assert_true(isinstance(instance, InstanceResource))
        assert_equal(instance.sid, "foo")

    def test_equivalence(self):
        r1 = self.r.load_instance({"sid": "AC123"})
        r2 = self.r.load_instance({"sid": "AC123"})
        assert_equal(r1, r2)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def testListResourceCreateResponse200(self, mock):
        """We should accept 200 OK in response to a POST creating a resource."""
        return_value = Mock()
        return_value.status_code = 200
        return_value.content = json.dumps({'sid': 'foo'})
        mock.return_value = return_value

        self.r.create_instance({}).execute()

        mock.assert_called_with("POST", "https://api.twilio.com/2010-04-01/Resources",
                                auth=auth, use_json_extension=True,
                                client=self.client)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def testListResourceCreateResponse201(self, mock):
        """We should accept 201 Created in response to a POST creating a resource."""
        return_value = Mock()
        return_value.status_code = 200
        return_value.content = json.dumps({'sid': 'foo'})
        mock.return_value = return_value

        self.r.create_instance({}).execute()

        mock.assert_called_with("POST", "https://api.twilio.com/2010-04-01/Resources",
                                auth=auth, use_json_extension=True,
                                client=self.client)


class NextGenListResourceTest(unittest.TestCase):

    def setUp(self):
        self.client = Mock()
        self.r = NextGenListResource(self.client, base_uri, auth)

    def test_list_resource_init(self):
        uri = "%s/%s" % (base_uri, self.r.name)
        assert_equal(self.r.uri, uri)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_iter_key_not_present(self, mock):
        resp = Mock()
        resp.status_code = 200
        resp.content = "{}"
        mock.return_value = resp

        self.assertRaises(StopIteration, advance_iterator, self.r.iter())

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_iter_request(self, mock):
        resp = Mock()
        resp.status_code = 200
        resp.content = json.dumps({'meta': {'key': 'foos'}, 'foos': [{'sid': '123'}]})
        mock.return_value = resp

        item = advance_iterator(self.r.iter())

        mock.assert_called_with("GET", "https://api.twilio.com/2010-04-01/Resources",
                                auth=auth, use_json_extension=False,
                                client=self.client)
        assert_equal(item.sid, '123')

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_iter_next_page_not_present(self, mock):
        resp = Mock()
        resp.status_code = 200
        resp.content = json.dumps({'meta': {'key': 'foos', 'next_page_url': None}, 'foos': [{'sid': '123'}]})
        mock.return_value = resp

        items = self.r.iter()
        advance_iterator(items)

        self.assertRaises(StopIteration, advance_iterator, items)

    def test_instance_loading(self):
        instance = self.r.load_instance({"sid": "foo"})

        assert_true(isinstance(instance, NextGenInstanceResource))
        assert_equal(instance.sid, "foo")


class testInstanceResourceInit(unittest.TestCase):

    def setUp(self):
        self.client = Mock()
        self.parent = ListResource(self.client, base_uri, auth)
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
        m.assert_called_with(self.client, self.r.uri, self.r.auth, self.r.timeout)


class NextGenInstanceResourceTest(unittest.TestCase):
    def setUp(self):
        self.client = Mock(0)
        self.parent = NextGenListResource(self.client, base_uri, auth)
        self.r = NextGenInstanceResource(self.parent, "123")

    def test_load(self):
        self.r.load({"hey": "you"})
        assert_equal(self.r.hey, "you")
