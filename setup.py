from setuptools import setup
setup(
    name = "twilio",
    py_modules = ['twilio'],
    version = "2.0.10",
    description = "Twilio API client and TwiML generator",
    author = "Twilio",
    author_email = "help@twilio.com",
    url = "http://github.com/twilio/twilio-python/",
    keywords = ["twilio","twiml"],
    classifiers = [
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Telephony"
        ],
    long_description = """\
    Python Twilio Helper Library
    ----------------------------

    DESCRIPTION
    The Twilio REST SDK simplifies the process of makes calls to the Twilio REST.
    The Twilio REST API lets to you initiate outgoing calls, list previous call,
    and much more.  See http://www.twilio.com/docs for more information.

    USAGE
    To use the Twilio library, just 'import twilio' in the your current py
    file. As shown in example-rest.py, you will need to specify the ACCOUNT_ID
    and ACCOUNT_TOKEN given to you by Twilio before you can make REST
    requests. In addition, you will need to choose a 'To' and 'From' before
    making outgoing calls. See http://www.twilio.com/docs for more
    information.

     LICENSE The Twilio Python Helper Library is distributed under the MIT
    License """ )
