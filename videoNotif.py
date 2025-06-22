import os
import requests
import tweepy
from atproto import Client
from dotenv import load_dotenv
load_dotenv()  



def create_message():
    yt_link = os.getenv("YOUTUBE_LINK")
    yt_title = os.getenv("YOUTUBE_TITLE")
    message = f"🎮 Canadian Gamer is Just uploaded a new video: {yt_title}: {yt_link}"
    return message

# Post to Twitter
def post_to_twitter():
    message = create_message()
    client = tweepy.Client(
    consumer_key=os.getenv("TWITTER_API_KEY"),
    consumer_secret=os.getenv("TWITTER_API_SECRET"),
    access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
    access_token_secret=os.getenv("TWITTER_ACCESS_SECRET"),
)

    # auth = tweepy.OAuth1UserHandler(
    #     os.getenv("TWITTER_API_KEY"),
    #     os.getenv("TWITTER_API_SECRET"),
    #     os.getenv("TWITTER_ACCESS_TOKEN"),
    #     os.getenv("TWITTER_ACCESS_SECRET")
    # )
    response = client.create_tweet(text=message)
    print(f"✅ Posted to Twitter: https://twitter.com/user/status/{response.data['id']}")

# Post to Bluesky
def post_to_bluesky():
    message = create_message()
    client = Client()
    client.login(os.getenv("BLUESKY_HANDLE"), os.getenv("BLUESKY_PASSWORD"))
    client.send_post(text=message)
    print("✅ Posted to Bluesky")

if __name__ == "__main__":
    post_to_twitter()
    post_to_bluesky()
