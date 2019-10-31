import unittest
import warnings

from twilio.base.obsolete import deprecated_method


class DeprecatedMethodTest(unittest.TestCase):

    def test_deprecation_decorator(self):

        @deprecated_method('new_method')
        def old_method():
            pass

        with warnings.catch_warnings(record=True) as caught_warnings:
            warnings.simplefilter("always")

            # Call function that should raise a warning
            old_method()

            if len(caught_warnings):
                self.assertEqual(
                    str(caught_warnings[0].message),
                    'Function method .old_method() is being deprecated in favor of .new_method()'
                )
                assert issubclass(caught_warnings[0].category, DeprecationWarning)

