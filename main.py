from flask import Flask, request
import africastalking
from texts import sending
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()
# Set your Africa's Talking API credentials
africastalking_username = os.getenv("africastalking_username")
africastalking_api_key = os.getenv("africastalking_api_key")

# Initialize the Africa's Talking SDK
africastalking.initialize(africastalking_username, africastalking_api_key)

# Get the SMS service


@app.route('/ussd', methods=['GET', 'POST'])
def ussd_callback():
    response = ""
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")
    
    if text == '':
        response = "CON Welcome to our anonymous mental health friend to talk to when lonely \n Press: \n"
        response += "1. Continue \n"
        
    elif text == '1':
        response = "CON Would you like to continue as anonymous? \n"
        response += "1. Yes \n"
        response += "2. No \n"

    elif text == '1*2':
        response = "CON Enter your name \n"
        
    elif text == '1*1' or '1**':
        response = "END Thank you for choosing to get connected to an anonymous chat friend. You will receive an SMS shortly. \n"

 
        
    try:
      resp = sending()
      print(resp)
    except Exception as e:
        print(f'Encountered an error while sending SMS: {str(e)}')

    return response

#TODO: create incoming messages route
# @app.route('/incoming-messages', methods=['POST'])
# def incoming_messages():
#    data = request.get_json(force=True)
#    print(f'Incoming message...\n ${data}')
#    return Response(status=200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)

