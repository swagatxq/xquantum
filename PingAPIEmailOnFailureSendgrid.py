import requests
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

############# Replace this with your configuration ############
SENDGRID_API_KEY= 'sendgridAPIKEY'
FROM_EMAIL = 'from_email@gmail.com'
TO_EMAIL = 'to_email@gmail.com'
API_URL = 'https://google.com/test'
API_NAME = 'Your API name'
###############################################################


############# Be careful in changing the code below ############
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

# Function to send email alert using SendGrid API
def send_email_alert(api_name, recipient_email, sender_email, api_key):
    message = Mail(
        from_email=sender_email,
        to_emails=recipient_email,
        subject='API Alert: ' + api_name + ' is down!',
        html_content='<strong>' + api_name + '</strong> is not responding. Please check the API.'
    )
    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        print("Email sent!")
    except Exception as e:
        print("Error sending email:", e)


if not ping_api(API_URL):
    send_email_alert(API_NAME, FROM_EMAIL, TO_EMAIL, SENDGRID_API_KEY)
