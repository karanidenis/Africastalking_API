from flask import Flask, request

app = Flask(__name__)

response = ""

@app.route('/ussd', methods=['GET', 'POST'])
def ussd_callback():
  global response
  session_id = request.values.get("sessionId", None)
  service_code = request.values.get("serviceCode", None)
  phone_number = request.values.get("phoneNumber", None)
  text = request.values.get("text", "default")
  
  if text == '':
    response  = "CON Welcome to our anonymous mental health friend to talk to when lonely \n Press: \n"
    response += "1. Continue \n"
    
  elif text == '1':
      response = "CON Would you like to continue as anonymous? \n"
      response += "1. Yes \n"
      response += "2. No \n"

  elif text == '1*2':
    response = "CON Enter your name \n"
    
  elif text == '1*1' or '1**':
      response = "END Thank you for choosing to get connected to an anonymous chat friend. You will receive an SMS shortly. \n"

  return response 

app.run(host='0.0.0.0', port=85)

