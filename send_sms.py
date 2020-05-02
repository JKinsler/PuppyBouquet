import os
from twilio.rest import Client
import puppies as pups


"""sample message
# MUST SOURCE THE ENVIRONMENT VARIABLES BEFORE RUNNING THIS
account_sid = os.environ["TWILIO_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

client = Client(account_sid, auth_token)
client.messages.create(
    to=os.environ["JK_PHONE_NUM"],
    from_=os.environ["TWILIO_PHONE_NUM"], 
    body="You are a magical unicorn on your first Twilio Rainbow journey."
    )
"""

vid_img = pups.choose_image()

account_sid = os.environ["TWILIO_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
jk_num = os.environ["JK_PHONE_NUM"]
client = Client(account_sid, auth_token)


def send_sms(phone_num, msg=vid_img):
    """Send an sms message to the phone number which is given as an input 
    parameter"""

    client.messages.create(
    to=jk_num,
    from_=os.environ["TWILIO_PHONE_NUM"], 
    body=msg
    )

    return "message sent to {phone_num}, {msg}".format(phone_num = phone_num,\
                                                        msg = msg)

