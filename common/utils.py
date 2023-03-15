# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

from Optics.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_NUMBER

# Set environment variables for your credentials
# Read more at http://twil.io/secure

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
message = client.messages.create(
    body="Hello from papa",
    from_=TWILIO_NUMBER,
    to="+923333998028"
)
print(message.body)
