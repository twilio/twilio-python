from setuptools import setup, find_packages
setup(
    name = "twilio",
    version = "3.0.1",
    description = "Twilio API client and TwiML generator",
    author = "Twilio",
    author_email = "help@twilio.com",
    url = "http://github.com/twilio/twilio-python/",
    keywords = ["twilio","twiml"],
    install_requires = ["httplib2"],
    packages = find_packages(),
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
    The Twilio REST API lets to you initiate outgoing calls, list previous calls,
    and much more.  See http://www.github.com/twilio/twilio-python for more information.

     LICENSE The Twilio Python Helper Library is distributed under the MIT
    License """ )
