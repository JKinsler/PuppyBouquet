"""Send messages to users"""

import os
from twilio.rest import Client
import puppies as pups
import messages as msg
from datetime import datetime

# universal variables for send_sms.py file
account_sid = os.environ["TWILIO_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
jk_num = os.environ["JK_PHONE_NUM"]
client = Client(account_sid, auth_token)

#choose a random
vid_img = pups.choose_image()
saying=msg.choose_msg()


def send_sms(phone_num):
    """Send an sms message to the phone number which is given as an input 
    parameter

    MUST SOURCE THE ENVIRONMENT VARIABLES BEFORE RUNNING THIS CODE"""

    message = client.messages.\
    create(
        to=jk_num,
        from_=os.environ["TWILIO_PHONE_NUM"], 
        body=msg.choose_msg(),
        media_url=[pups.choose_image()]
    )

    return message.sid

# # schedule and sms
# now = datetime.now()
# print(now)
# today = datetime.today()
# print(today)

# def schedule_sms():
#     now = datetime.today()
    

# send_time = '2020-05-03 00:22:40.927728'



