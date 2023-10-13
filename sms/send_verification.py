import africastalking
import os
from dotenv import load_dotenv

load_dotenv()

username = 'musat' 
api_key = 'd46fe22e676feddca9f9dffec26e9c0d380858ea8846eee19e505bd0091974a6'


africastalking.initialize(username, api_key)

sms = africastalking.SMS

class SMSClient:
    def __init__(self, phone_number, message):
        self.phone_number = phone_number
        self.message = message

    def send_sms(self):
        sms.send(self.message, [self.phone_number], callback=on_finish)
        

def on_finish(error, response):
    if error is not None:
        raise error
    print(response)

def send(phone, code):
    try:
        sms_client = SMSClient(phone, code)
        sms_client.send_sms()
        return 1
    except Exception as e:
        return{"Error": str(e), "statusCode": 500}


message = 'wassup'
sms_client = SMSClient('+254742079321', message)
sms_client.send_sms()