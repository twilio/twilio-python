"""
Test the base Resource class
"""
import unittest
from mock import Mock
from nose.tools import assert_equals
from nose.tools import raises
from twilio.rest.resources import Resource
from twilio.rest.resources import ListResource
from twilio.rest.resources import InstanceResource

base_uri = "https://api.twilio.com/2010-04-01"
account_sid = "AC123"
auth = (account_sid, "token")


def test_resource_init():
    r = Resource(base_uri, auth)
    uri = "{}/{}".format(base_uri, r.name)

    assert_equals(r.base_uri, base_uri)
    assert_equals(r.auth, auth)
    assert_equals(r.uri, uri)

def test_equivalence():
    p = ListResource(base_uri, auth)
    r1 = p.load_instance({"sid": "AC123"})
    r2 = p.load_instance({"sid": "AC123"})
    assert_equals(r1, r2)


class ListResourceTest(unittest.TestCase):

    def setUp(self):
        self.r = ListResource(base_uri, auth)

    def testListResourceInit(self):
        uri = "{}/{}".format(base_uri, self.r.name)
        self.assertEquals(self.r.uri, uri)

    def testKeyValue(self):
        self.assertEquals(self.r.key, self.r.name.lower())

    def testKeyValue(self):
        self.r.key = "Hey"
        self.assertEquals(self.r.key, "Hey")

    def testInstanceLoading(self):
        instance = self.r.load_instance({"sid": "foo"})

        self.assertIsInstance(instance, InstanceResource)
        self.assertEquals(instance.sid, "foo")


class testInstanceResourceInit(unittest.TestCase):

    def setUp(self):
        self.parent = ListResource(base_uri, auth)
        self.r = InstanceResource(self.parent, "123")
        self.uri = "%s/%s" % (self.parent.uri, "123")

    def testInit(self):
        self.assertEquals(self.r.uri, self.uri)

    def testLoad(self):
        self.r.load({"hey": "you"})
        self.assertEquals(self.r.hey, "you")

    def testLoadWithUri(self):
        self.r.load({"hey": "you", "uri": "foobar"})
        self.assertEquals(self.r.hey, "you")
        self.assertEquals(self.r.uri, self.uri)

    def testLoadWithFrom(self):
        self.r.load({"from": "foo"})
        self.assertEquals(self.r.from_, "foo")

    def testLoadSubresources(self):
        m = Mock()
        self.r.subresources = [m]
        self.r.load_subresources()
        m.assert_called_with(self.r.uri, self.r.auth)

