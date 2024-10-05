from openai import OpenAI
from datetime import datetime, timedelta
from requests_oauthlib import OAuth1Session
import tweepy
import requests



# Twitter API credentials (use your keys here)
BEARER_TOKEN = ''
API_KEY = ''
API_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_SECRET = ''


# Oauth2 twitter
CLIENT_ID = ''
CLIENT_SECRET = ''

# OpenAI API Key
OPENAI_API_KEY = ''

## Configurations
image_required = True
prompt = (
        f"""
            About Xq1: Xq1 by Xquantum is a platform where 
            you can deploy any code, AI generated or 
            custom written, on cron, with no additional infra.
            
            List of sample use cases (live) of Xq1:
            1) Growth marketing:
                a) Automatic Twitter/X posts using ChatGPT API on Xq1 -> Get more Twitter followers
                b) Automatic Reddit posts using ChatGPT API on Xq1 -> Get more Reddit followers
                c) Automatic Email retargeting using Sendgrid API to your DB connection on Xq1 -> Reactivate signed up users
                
            2) Functional development:
                a) Test if API or Website is up, and message / Slack / email if down -> Peace of mind
                b) Call internal APIs or services on cron -> No need to host another service.
                c) Scrape / crawl data / websites etc on cron -> Easy to build, deploy & maintain
                d) Outsource some business logic to non development team -> Save times for developers
                
            3) Financial markets:
                a) Fetch stock market data and dump to your Google Sheet or Database directly -> Trading profits
                b) Automatically calculate and place order to buy / sell -> Automatically extract value from stock market
                
            
            Now, pick up one use case at random, go into detail, come up with a tweet, 
            highlighting what can Indie builders, solopreneurs and developers use xq1 for. 
            Brownie points if it has keywords and 
            hashtags which are frequently searched.
            
            DO NOT EXCEED 200 characters.
            """
    )
tweet_self_reply_text = "Comment '#DeployOnXquantum' if you would like to run this same automation on your account."



# Authenticate OpenAI (ChatGPT)
openai = OpenAI(api_key=OPENAI_API_KEY)


def generate_media_for_tweet(tweet):
    response = openai.images.generate(
      model="dall-e-3",
      prompt=f"You are a social media graphic expert. Create a simple graphic with ZERO TEXT to go with tweet {tweet}",
      n=1,
      size="1024x1024"
    )
    return response.data[0].url
    
# Generate a tweet using ChatGPT from a list of content options
def generate_tweet(prompt):

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a top social media strategist, ex influencer, with a focus on twitter."},
            {"role": "user", "content": prompt},
        ]
    )
    
    tweet_content = response.choices[0].message.content
    tweet_content = tweet_content[1:-1] +  "\n\n - Built on AI, Run on Xq1"
    return tweet_content

def upload_media(image_url):
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    
    filename = 'generated_image.png'
    img_data = requests.get(image_url).content
    with open(filename, 'wb') as handler:
        handler.write(img_data)
        
    media = api.media_upload(filename)
    return media.media_id_string

# Post the new tweet on Twitter
def post_tweet(content, **kwargs):
    consumer_key = API_KEY
    consumer_secret = API_SECRET
    access_token = ACCESS_TOKEN
    access_token_secret = ACCESS_SECRET
    
    media_id = kwargs.get('media_id', None)

    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )
    
    if media_id:
        payload = {"text": content, "media": media_id}
    else:
        payload = {"text": content}
    # Making the request
    response = oauth.post(
        "https://api.twitter.com/2/tweets",
        json=payload,
    )
    return response


    
# Post the new tweet on Twitter
def comment_on_tweet(tweet_id):
    consumer_key = API_KEY
    consumer_secret = API_SECRET
    access_token = ACCESS_TOKEN
    access_token_secret = ACCESS_SECRET


    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    payload = {
        "text": tweet_self_reply_text,
        "reply": {
            "in_reply_to_tweet_id": tweet_id
        }
    }
    # Making the request
    response = oauth.post(
        "https://api.twitter.com/2/tweets",
        json=payload,
    )


def run_campaign():
    new_tweet_content = generate_tweet(prompt)
    if image_required:
        image_url = generate_media_for_tweet(new_tweet_content)
        media_id = upload_media(image_url)

    if len(new_tweet_content) > 280:
        print("Failed to generate a suitable tweet within the character limit.")
        return None
    try:
        if image_required:
            tweet_response = post_tweet(new_tweet_content, media_id)
        else:
            tweet_response = post_tweet(new_tweet_content, media_id)
        tweet_data = tweet_response.json()
        tweet_id = tweet_data['data']['id']
        comment_on_tweet(tweet_id)
    except:
        pass
        
        
run_campaign()

