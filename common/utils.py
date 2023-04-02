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

def get_default_query_param(request, key, default):
    """

    @param request: request object
    @type request: request
    @param key: key to get data from
    @type key: str
    @param default: default variable to return if key is empty or doesn't exist
    @type default: str/None
    @return: key
    @rtype: str/None
    """
    if key in request.query_params:
        key = request.query_params.get(key)
        if key:
            return key
    return default
