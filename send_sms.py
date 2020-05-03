"""Send messages to users"""

import os
from twilio.rest import Client
import puppies as pups
import messages as msg
import schedule
import time

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


'''Next up:
    - write code to schedule when sms messages will send
    - review python 'schedule' module instead of 'schedule_sms' code below.

# import datetime
# from datetime import timedelta

def schedule_sms():
    """schedule when an SMS will send"""
    
    #current time in UTC 
    now = datetime.datetime.now() # TO DO: update to be local time instead of UTC
    print(now)
    now_time = ('strip') #TO DO: strip the local time so it gives hours, minutes, seconds only
    print(now_time)

    # desired time to send the message
    schedule = 'something' # TO do: select a time to send the message
    print(schedule)

    if now_time == sched_time:
        send_sms(jk_num)
        return 'message sent'
'''


if __name__ == '__main__':



