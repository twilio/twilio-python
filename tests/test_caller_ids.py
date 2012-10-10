# -*- coding: utf-8 -*-
import sys

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

from twilio.rest.resources import CallerId, CallerIds


class CallerIdTests(unittest.TestCase):
    pass

