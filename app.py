# from twilio.rest import Client
# from flask import Flask, request
# from twilio.twiml.voice_response import VoiceResponse
# import os
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# # Debug print statements
# print("TWILIO_ACCOUNT_SID:", os.getenv('TWILIO_ACCOUNT_SID'))
# print("TWILIO_AUTH_TOKEN:", os.getenv('TWILIO_AUTH_TOKEN'))

# # Twilio credentials from environment variables
# account_sid = os.getenv('TWILIO_ACCOUNT_SID')
# auth_token = os.getenv('TWILIO_AUTH_TOKEN')
# twilio_phone_number = os.getenv('TWILIO_PHONE_NUMBER')

# # Initialize Twilio client
# client = Client(account_sid, auth_token)

# # Flask app for handling incoming calls
# app = Flask(__name__)

# # Make an outbound call
# def make_call():
#     call = client.calls.create(
#         to='+919182591919',  # Replace with the recipient's phone number
#         from_=twilio_phone_number,  # Use the phone number from .env
#         url='https://2bcd-182-71-109-122.ngrok-free.app/incoming-call'  # Your ngrok URL
#     )
#     print(f"Call initiated with SID: {call.sid}")

# # Webhook for handling incoming calls
# @app.route("/incoming-call", methods=['POST'])
# def incoming_call():
#     response = VoiceResponse()
#     response.say('Hello, you have reached my Twilio number.')
#     return str(response)

# if __name__ == "__main__":
#     # Uncomment the next line to make an outbound call
#     make_call()

#     # Start Flask server to handle incoming calls
#     app.run(port=3000)

from twilio.rest import Client
from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Debug print statements
print("TWILIO_ACCOUNT_SID:", os.getenv('TWILIO_ACCOUNT_SID'))
print("TWILIO_AUTH_TOKEN:", os.getenv('TWILIO_AUTH_TOKEN'))
print("TWILIO_PHONE_NUMBER:", os.getenv('TWILIO_PHONE_NUMBER'))

# Twilio credentials from environment variables
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_phone_number = os.getenv('TWILIO_PHONE_NUMBER')

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Flask app for handling incoming calls
app = Flask(__name__)

# Make an outbound call
def make_call():
    call = client.calls.create(
        to='+919182591919',  # Replace with the recipient's phone number
        from_=+12677281042,  # Your Twilio phone number from .env
        url=' https://ce13-182-71-109-122.ngrok-free.app/incoming-call',  # Your ngrok URL
        status_callback=' https://ce13-182-71-109-122.ngrok-free.app/status-callback',
        status_callback_event=['completed']  # You can specify other events like 'initiated', 'ringing', etc.
    )
    print(f"Call initiated with SID: {call.sid}")

# Webhook for handling incoming calls
@app.route("/incoming-call", methods=['POST'])
def incoming_call():
    response = VoiceResponse() 
    response.say('Good Afternoon Authorities, We are Team Drona')
    target_number = '+919626231079'  # Replace with the second user's phone number
    response.dial(target_number, timeout=20)
    return str(response)

# Optional: Implement Status Callback
@app.route("/status-callback", methods=['POST'])
def status_callback():
    call_status = request.form.get('CallStatus')
    print(f"Call Status: {call_status}")
    return '', 200

if __name__ == "__main__":
    # Uncomment the next line to make an outbound call
    make_call()

    # Start Flask server to handle incoming calls
    app.run(port=5000)