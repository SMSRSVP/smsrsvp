# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "ACb4601ebfba5a649c4aae1ccbf6b1ee8f"
auth_token = "a4d6a5026b373ccd8cd7405d8026adfa"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+17033444899", from_="+17038280845",
                                     body="Hello there!")
