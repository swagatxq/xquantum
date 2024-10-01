from openai import OpenAI
from datetime import datetime, timedelta
from requests_oauthlib import OAuth1Session


# Twitter API credentials (use your keys here)
BEARER_TOKEN = ''
API_KEY = ''
API_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_SECRET = ''


# OpenAI API Key
OPENAI_API_KEY = ''


# Authenticate OpenAI (ChatGPT)
openai = OpenAI(api_key=OPENAI_API_KEY)


# Generate a tweet using ChatGPT from a list of content options
def generate_tweet():

    prompt = (
        f"""
            Generate a snarky, quotable tweet promoting Xquantum’s no-code automation platform with cron scheduling.
            DO NOT EXCEED 200 characters.

            Maximize reader value; don’t just market. Focus on:

                1.	Ease of Use: Mock outdated cron setups; highlight Xquantum’s UI-driven solution over terminal commands.
                2.	Versatility: Sarcastically note BYOC (Bring Your Own Code)—toss those DIY duct-tape automations!
                3.	Reliability: Emphasize server/database restarts and alerts to save users from “API is down at 2 AM” horror stories.
                4.	Industry Automation: Use funny examples: trade while sipping coffee, automate HR so onboarding isn’t forgotten.
                5.	No Infrastructure Hassle: Jokingly dismiss server management; let machines do the work!
                6.	Cutting-edge Features: Playfully mention running Jupyter Notebooks on cron—sounds fancy, but easy!

            Include funny hashtags targeting tech pros, engineers, and business owners.

            DO NOT EXCEED 200 characters.
            """
    )

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a top social media strategist, ex influencer, with a focus on twitter."},
            {"role": "user", "content": prompt},
        ]
    )
    
    tweet_content = response.choices[0].message.content
    tweet_content = tweet_content[1:-1] +  "\n\n - Built on AI, Run on Xquantum"
    return tweet_content

# Post the new tweet on Twitter
def post_tweet(content):
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
        "text": "Comment 'DM' if you would like to run this same automation on your account.",
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
    new_tweet_content = generate_tweet()      
    print(new_tweet_content)
    print(len(new_tweet_content))
    if len(new_tweet_content) > 280:
        print("Failed to generate a suitable tweet within the character limit.")
        return None
    try:
        tweet_response = post_tweet(new_tweet_content)
        tweet_data = tweet_response.json()
        tweet_id = tweet_data['data']['id']
        comment_on_tweet(tweet_id)
    except:
        pass

## call run campaign
run_campaign()
        
        
run_campaign()

