import tweepy
import random
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get Twitter API keys from environment variables
API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET_KEY = os.getenv("TWITTER_API_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Authenticate with Twitter API using tweepy
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# Function to read a random line from a txt file
def get_random_line(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return random.choice(lines).strip()

# List of your text files
txt_files = [
    'dev_quotes.txt',
    'code_banter.txt',
    'frontend_tips.txt',
    'react_tips.txt',
    'random_questions.txt'
]

# Choose a random file
random_file = random.choice(txt_files)

# Get a random line from the chosen file
random_text = get_random_line(random_file)

# Tweet the text
try:
    api.update_status(random_text)
    print(f"Successfully tweeted: {random_text}")
except tweepy.TweepError as e:
    print(f"Error: {e}")

