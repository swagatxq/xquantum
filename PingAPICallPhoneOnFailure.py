import requests
from twilio.rest import Client

# Twilio credentials (replace with your own)
TWILIO_ACCOUNT_SID = 'your_twilio_account_sid'
TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'
TO_PHONE_NUMBER = 'recipient_phone_number'

# API configuration
API_URL = 'https://example.com/api'  # Replace with your API URL
API_NAME = 'Example API'  # Replace with your API name

# Function to ping the API
def ping_api(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return False

# Function to make a phone call using Twilio API
def make_phone_call(api_name, to_phone_number, twilio_phone_number, account_sid, auth_token):
    client = Client(account_sid, auth_token)
    call = client.calls.create(
        to=to_phone_number,
        from_=twilio_phone_number,
        twiml=f'<Response><Say>{api_name} is down! Please check the API immediately.</Say></Response>'
    )
    print(f"Call initiated with SID: {call.sid}")

# Main logic
if not ping_api(API_URL):
    make_phone_call(API_NAME, TO_PHONE_NUMBER, TWILIO_PHONE_NUMBER, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
