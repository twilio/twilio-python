## Python Twilio Helper Library

### Description
The Twilio REST SDK simplifies the process of makes calls to the Twilio REST.
The Twilio REST API lets to you initiate outgoing calls, list previous call,
and much more.  See http://www.twilio.com/docs for more information.

### Installation

    $ sudo pip install twilio
    
### Manual Installation
Download the source and run

    $ python setup.py install

### Usage
To use the Twilio library, just 'import twilio' in the your current python
file. As shown in example-rest.py, you will need to specify the ACCOUNT_ID and
ACCOUNT_TOKEN given to you by Twilio before you can make REST requests. In
addition, you will need to choose a 'To' and 'From' before making
outgoing calls. See http://www.twilio.com/docs for more information.

### Files
  * **twilio.py**: include this library in your code
  * **examples/example-rest.py**: example usage of REST
  * **examples/example-twiml.py**: example usage of the TwiML generator
  * **examples/example-utils.py**: example usage of utilities

### License
The Twilio Python Helper Library is distributed under the MIT License