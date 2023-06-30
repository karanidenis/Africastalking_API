import africastalking
import os
from dotenv import load_dotenv

# TODO: Initialize Africa's Talking

load_dotenv() 
username = os.getenv("sms_username")

api_key = os.getenv("africastalking_api_key")
africastalking.initialize(username, api_key)
sms = africastalking.SMS



def sending():
  recipients = ["+254716272778"]
  message = "Hello, Thank you for joining us..."
  try:
    response = sms.send(message, recipients)
    return response
  except Exception as e:
    return f'We have a problem: {e}'

