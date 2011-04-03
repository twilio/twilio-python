try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
__version__ = "2.0.8"

package_info = {
    "name": "twilio",
    "version": __version__,
    "py_modules": ['twilio'],
    "description": "Twilio API client and TwiML generator",
    "long_description": open("README.markdown").read(),
    "author": "Twilio",
    "author_email": "help@twilio.com",
    "url": "http://github.com/twilio/twilio-python/",
    "download_url": "http://github.com/twilio/twilio-python/tarball/" + __version__,
    "keywords": ["twilio","twiml"],
    "classifiers": [
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Telephony"
    ],
}

setup(**package_info)
