#!/usr/bin/env python

import twilio

# Twilio REST API version
API_VERSION = '2008-08-01'

# Twilio AccountSid and AuthToken
ACCOUNT_SID = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
ACCOUNT_TOKEN = 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'

# Outgoing Caller ID previously validated with Twilio
CALLER_ID = 'NNNNNNNNNN';

# Create a Twilio REST account object using your Twilio account ID and token
account = twilio.Account(ACCOUNT_SID, ACCOUNT_TOKEN)

# ===========================================================================
# 1. Initiate a new outbound call to 415-555-1212
#    uses a HTTP POST
d = {
    'Caller' : CALLER_ID,
    'Called' : '415-555-1212',
    'Url' : 'http://demo.twilio.com/welcome',
}
print account.request('/%s/Accounts/%s/Calls' % \
    (API_VERSION, ACCOUNT_SID), 'POST', d)

# ===========================================================================
# 2. Get a list of recent completed calls (i.e. Status = 2)
#    uses a HTTP GET
d = { 'Status':2, }
print account.request('/%s/Accounts/%s/Calls' % \
    (API_VERSION, ACCOUNT_SID), 'GET', d)

# ===========================================================================
# 3. Get a list of recent notification log entries
#    uses a HTTP GET
print account.request('/%s/Accounts/%s/Notifications' % \
    (API_VERSION, ACCOUNT_SID), 'GET')

# ===========================================================================
# 4. Get a list of audio recordings for a certain call
#    uses a HTTP GET
d = { 'CallSid':'CA0c7001f3f3f5063b7f7d96def0f1ed00', }
print account.request('/%s/Accounts/%s/Recordings' % \
    (API_VERSION, ACCOUNT_SID), 'GET', d)

# ===========================================================================
# 5. Delete a specific recording
#    uses a HTTP DELETE, no response is returned when using DELETE
account.request( \
    '/%s/Accounts/%s/Recordings/RE4e75a0b62a5c52e5cb96dc25fb4101d9' % \
    (API_VERSION, ACCOUNT_SID), 'DELETE')
