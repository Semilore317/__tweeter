import tweepy
import random
import os

# Twitter credentials from GitHub secrets
api_key = os.environ["API_KEY"]
api_secret = os.environ["API_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

# Authenticate
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# List of categories
files = [
    "frontend_tips.txt",
    "code_banter.txt",
    "dev_quotes.txt",
    "react_tips.txt",
    "random_questions.txt"
]

# Pick a random category and a random line from it
chosen_file = random.choice(files)
with open(chosen_file, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]
    tweet = random.choice(lines)

# Send the tweet
api.update_status(tweet)
