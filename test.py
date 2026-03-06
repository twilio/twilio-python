import os

from twilio.rest import Client

# Your Account SID and Auth Token from console.twilio.com
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token  = os.environ.get('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

memory = client.memory.v1.stores.get("mem_store_01kjyes5vnes3v6gnm954w455a").fetch()

print(memory)