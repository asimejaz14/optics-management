# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

from Optics.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_NUMBER

# Set environment variables for your credentials
# Read more at http://twil.io/secure


def send_message(receiver_number, content):
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=content,
            from_=TWILIO_NUMBER,
            to=receiver_number
        )
        print(message.body)
    except Exception as e:
        print("TWILIO", e)
