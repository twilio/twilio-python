import unittest
import warnings

from twilio.base.obsolete import deprecated_method


class DeprecatedMethodTest(unittest.TestCase):

    def test_deprecation_decorator(self):

        @deprecated_method
        def old_method():
            return True

        with warnings.catch_warnings(record=True) as caught_warnings:
            warnings.simplefilter("always")
            # Call function that should raise a warning, but still execute
            self.assertTrue(old_method())
            self.assertTrue(len(caught_warnings))
            self.assertEqual(
                str(caught_warnings[0].message),
                'Function method .old_method() is deprecated'
            )
            assert issubclass(caught_warnings[0].category, DeprecationWarning)

    def test_deprecation_decorator_with_new_method(self):

        @deprecated_method('new_method')
        def old_method():
            return True

        with warnings.catch_warnings(record=True) as caught_warnings:
            warnings.simplefilter("always")

            # Call function that should raise a warning, but still execute
            self.assertTrue(old_method())
            self.assertTrue(len(caught_warnings))
            self.assertEqual(
                str(caught_warnings[0].message),
                'Function method .old_method() is deprecated in favor of .new_method()'
            )
            assert issubclass(caught_warnings[0].category, DeprecationWarning)
