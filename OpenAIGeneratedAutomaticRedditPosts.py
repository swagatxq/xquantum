from openai import OpenAI
import praw
import json

# Reddit API credentials
CLIENT_ID = ''
CLIENT_SECRET = ''
USERNAME = ''
PASSWORD = ''
USER_AGENT = ''


# Open AI API credentials
OPENAI_API_KEY = ''



# Prompt for OpenAI to generate content
prompt = (
    f"""
    About Xq1: Xq1 by Xquantum is a platform where you can deploy any code, 
    AI generated or custom written, on cron, with no additional infra. 
    
    Using Xq1 is as simple as pasting any code on Xq1, choosing a schedule,
    and pressing a button.

    List of sample use cases of Xq1:
    
    Growth Marketing Use Cases:

        1.	Auto-post Instagram updates using API at peak engagement times.
        2.	Auto-schedule LinkedIn posts for product announcements.
        3.	Post daily Facebook content automatically using ChatGPT for content creation.
        4.	Automatically respond to Twitter DMs using AI-generated replies.
        5.	Schedule TikTok posts and automate captions using AI.
        6.	Automate weekly newsletters using custom Mailchimp templates on cron.
        7.	Set up an auto-response to blog comments using sentiment analysis.
        8.	Auto-refresh Google Ads bids daily based on keyword performance.
        9.	Automatically optimize Facebook ad spending based on conversion data.
        10.	Generate dynamic reports on social media engagement and email them to the marketing team.

    Functional Development Use Cases:

        11.	Auto-backup website data to AWS S3 every night.
        12.	Automatically test API latency at intervals and alert if response time spikes.
        13.	Scrape competitor pricing data daily and notify via Slack.
        14.	Regularly update a MySQL database with data from external sources.
        15.	Auto-update project dependencies and alert if a new version is available.
        16.	Monitor memory/CPU usage on servers and restart processes if thresholds are exceeded.
        17.	Auto-generate and send weekly reports on server uptime to stakeholders.
        18.	Schedule weekly database cleanups to optimize performance.
        19.	Automatically rotate encryption keys for cloud services every month.
        20.	Periodically pull financial data from APIs and trigger calculations.

    Indie Developer Use Cases:

        21.	Deploy blog content updates using Markdown files.
        22.	Monitor uptime of side project websites and alert if down.
        23.	Automatically renew SSL certificates on custom domains.
        24.	Generate GitHub release notes automatically after each push to production.
        25.	Pull product reviews from eCommerce platforms and notify about negative feedback.
        26.	Auto-update side project apps with new code without managing servers.
        27.	Schedule automated tests for open-source projects to check for regressions.
        28.	Automate email sequences to keep users engaged with your project.
        29.	Generate user activity reports and email to yourself every Monday morning.
        30.	Auto-fetch the latest data from external APIs and cache it for faster access.

    Data Science & Machine Learning Use Cases:

        31.	Schedule nightly retraining of machine learning models using fresh data.
        32.	Automatically run AI simulations on EC2 and collect results via email.
        33.	Regularly scrape financial news sites for stock market sentiment analysis.
        34.	Auto-generate and deploy updated datasets to AI models at intervals.
        35.	Automate data cleaning tasks and prepare for the next day’s model training.
        36.	Schedule experiments to run on multiple datasets and compare results.
        37.	Automatically run feature selection for machine learning models every month.
        38.	Set up automatic model performance monitoring and alert on significant deviations.
        39.	Auto-fetch new data from APIs and append to a training dataset.
        40.	Regularly monitor model predictions and alert if performance drops.


    E-commerce & SaaS Use Cases:

        52.	Auto-send reminders to customers with abandoned carts.
        53.	Automatically push product updates to an eCommerce site.
        56.	Automatically pull reviews from marketplaces and notify the support team.
        58.	Schedule email campaigns for product launches and discounts.
        60.	Schedule a recurring check for site load times and alert the developer if it’s too slow.

    Personal Projects Use Cases:

        64.	Regularly check your side project’s uptime and get SMS alerts.
        65.	Pull personal financial data from APIs and analyze it.
        66.	Set reminders to refactor code every few months.
        67.	Automatically tweet progress updates about personal side projects.
        68.	Schedule periodic checks on personal domains for upcoming expiration dates.
        69.	Schedule backup of family photos to Google Drive on the first of every month.

    FinTech Use Cases:

        71.	Auto-pull exchange rates from financial APIs and update databases.
        72.	Monitor stock market price movements and notify if thresholds are met.
        73.	Automate analysis of financial portfolios and email clients updates.
        74.	Regularly calculate the risk levels of investment portfolios.
        75.	Automatically fetch and process transaction records for reconciliation.
        76.	Automatically notify about suspicious transactions in banking apps.
        77.	Auto-fetch crypto price data and generate daily summary reports.
        78.	Regularly scrape regulatory updates and notify the finance team.
        79.	Automate the creation of tax reports and send them to accountants.
        80.	Schedule financial dashboards to update every day with the latest metrics.

    Web Development Use Cases:

        81.	Auto-refresh CDN caches every night for updated web content.
        82.	Schedule testing of website load times at peak and off-peak hours.
        84.	Schedule recurring scans for broken links on your website.
        85.	Automatically update website meta tags based on performance metrics.
        86.	Monitor the performance of web apps and alert if downtime occurs.
        87.	Schedule deployment of new content to production servers without manual intervention.
        88.	Automatically convert blog drafts to HTML and push live.
        89.	Periodically check website SEO performance and notify of needed improvements.
        90.	Schedule the generation of website accessibility reports for compliance.


    Now, pick up one use case at random, describe the use case in detail and 
    how can Xq1 potentially solve it with instant serverless cron deployment, 
    and come up with a Reddit post (LESS THAN 400 words). In the same reddit post, generate
    sample python script that be used to solve that particular use in Xq1 (dont call main
    function to run the script - just call the last function). Make sure
    the generated code is in code markdown that reddit can handle. The title should be
    start with "How to", "Why should", so that readers are enticed to read the entirety of the post.
    
    Respond in JSON in the following format -> {{'title':'', 'body':''}}
    """
)

openai = OpenAI(api_key=OPENAI_API_KEY)

# Function to post to Reddit
def post_to_reddit(title, message):
    reddit.subreddit("u_" + reddit.user.me().name).submit(title, selftext=message)

# Generate a Reddit post using OpenAI
def generate_post(prompt):
    response = openai.chat.completions.create(
        max_completion_tokens=510,
        model="gpt-3.5-turbo",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": "You are a top social media strategist, ex influencer, with a focus on Reddit."},
            {"role": "user", "content": prompt},
        ]
    )
    post_content = json.loads(response.choices[0].message.content).get('body')
    post_content = post_content[0:-1] + "\n\n - This post was run on Xq1! Upvote if you like it!"

    post_title = json.loads(response.choices[0].message.content).get('title')
    return post_content, post_title


# Authenticate to Reddit using PRAW
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT,
    username=USERNAME,
    password=PASSWORD
)

try:
    post_content, post_title = generate_post(prompt)
    post_to_reddit(post_title.strip('"'), post_content)
except:
    pass
