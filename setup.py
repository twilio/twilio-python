from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

# To install the twilio-python library, open a Terminal shell, then run this
# file by typing:
#
# python setup.py install
#
# You need to have the setuptools module installed. Try reading the setuptools
# documentation: http://pypi.python.org/pypi/setuptools

setup(
    name="twilio",
    version="7.4.0",
    description="Twilio API client and TwiML generator",
    author="Twilio",
    author_email="help@twilio.com",
    url="https://github.com/twilio/twilio-python/",
    keywords=["twilio", "twiml"],
    python_requires='>=3.6.0',
    install_requires=[
        "pytz",
        "requests >= 2.0.0",
        "PyJWT >= 2.0.0, < 3.0.0",
    ],
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Telephony",
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
