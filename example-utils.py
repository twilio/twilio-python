#!/usr/bin/env python

import twilio

# Twilio AccountSid and AuthToken
ACCOUNT_SID = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
ACCOUNT_TOKEN = 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'

# Create a Twilio utility object using your Twilio account ID and token
utils = twilio.Utils(ACCOUNT_SID, ACCOUNT_TOKEN)

# ===========================================================================
# 1. Validate a Twilio request

# the URL and POST parameters would typically be provided by the web
# framework that is recieving the request from Twilio (e.g. Django)
url = "http://UUUUUUUUUUUUUUUUUU"
postvars = {}

# the request from Twilio also includes the HTTP header: X-Twilio-Signature
# containing the expected signature
signature = "SSSSSSSSSSSSSSSSSSSSSSSSSSSS"

print "The request from Twilio to %s with the POST parameters %s " % \
    (url, postvars)
if utils.validateRequest(url, postVar, signature):
    print "was confirmed to have come from Twilio."
else:
    print "was NOT VALID.  It might have been spoofed!"
