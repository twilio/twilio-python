import sys
from twilio import __version__
from setuptools import setup, find_packages

# To install the twilio-python library, open a Terminal shell, then run this
# file by typing:
#
# python setup.py install
#
# You need to have the setuptools module installed. Try reading the setuptools
# documentation: http://pypi.python.org/pypi/setuptools
REQUIRES = ["httplib2 >= 0.7", "six"]

if sys.version_info < (2, 6):
    REQUIRES.append('simplejson')
if sys.version_info >= (3,0):
    REQUIRES.append('unittest2py3k')
    REQUIRES.append('socksipy-branch')
else:
    REQUIRES.append('unittest2')

setup(
    name = "twilio",
    version = __version__,
    description = "Twilio API client and TwiML generator",
    author = "Twilio",
    author_email = "help@twilio.com",
    url = "http://github.com/twilio/twilio-python/",
    keywords = ["twilio","twiml"],
    install_requires = REQUIRES,
    packages = find_packages(),
    include_package_data=True,
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Telephony",
        ],
    long_description = """\
    Python Twilio Helper Library
    ----------------------------

    DESCRIPTION
    The Twilio REST SDK simplifies the process of making calls using the Twilio REST API.
    The Twilio REST API lets to you initiate outgoing calls, list previous calls,
    and much more.  See http://www.github.com/twilio/twilio-python for more information.

     LICENSE The Twilio Python Helper Library is distributed under the MIT
    License """ )
