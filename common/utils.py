# # Download the helper library from https://www.twilio.com/docs/python/install
# import os
# from twilio.rest import Client
# # Set environment variables for your credentials
# # Read more at http://twil.io/secure
# account_sid = "AC7938ca81ff7404c7e95ac7c639db5de9"
# auth_token = "06ad1460866122093077ef19b1dd5265"
# client = Client(account_sid, auth_token)
# message = client.messages.create(
#   body="Hello from Twilio",
#   from_="+15676777115",
#   to="+923333998028"
# )
# print(message.sid)
#
# import time
# from time import sleep
# from sinchsms import SinchSMS
#
#
# # function for sending SMS
# def sendSMS():
#   # enter all the details
#   # get app_key and app_secret by registering
#   # a app on sinchSMS
#   number = 'your_mobile_number'
#   app_key = 'your_app_key'
#   app_secret = 'your_app_secret'
#
#   # enter the message to be sent
#   message = 'Hello Message!!!'
#
#   client = SinchSMS(app_key, app_secret)
#   print("Sending '%s' to %s" % (message, number))
#
#   response = client.send_message(number, message)
#   message_id = response['messageId']
#   response = client.check_status(message_id)
#
#   # keep trying unless the status returned is Successful
#   while response['status'] != 'Successful':
#     print(response['status'])
#     time.sleep(1)
#     response = client.check_status(message_id)
#
#   print(response['status'])
#
#
# Invoke-WebRequest -Method POST `
#   -Headers @{"Authorization" = "Bearer d063a374a23c427eaf1172f9ae20865e"} `
#   -ContentType "application/json" `
#   -Uri https://sms.api.sinch.com/xms/v1/60cedc57d35d4429896d8081ea6dd103/batches `
#   -Body '{
#     "from": "447520652428",
#     "to": [ "923333998028" ],
#     "body": "Enter test message here"
#   }'
