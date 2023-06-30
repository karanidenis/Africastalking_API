import africastalking

# TODO: Initialize Africa's Talking

# username="karanidenis"
# api_key="35095b41ed745d38d682e004e6a78f6d4642c3320d792c30e763b22609c2a229"
username = "karanidenis"
api_key = "47585c2a5bd1955a7f43fb5871b90e78df8fb942f58c22d0ddcd67732c896f63"
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

