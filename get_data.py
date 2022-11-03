from flask import Flask, Request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

"""Sets up Twilio information"""
account_sid = 'AC2b3a0b688528b81a06196c9ea622f92d'
auth_token = '519e043d4978da36c241a570f9f3ea71'
client = Client(account_sid, auth_token)


for sms in client.messages.list():
  print(sms.to)
