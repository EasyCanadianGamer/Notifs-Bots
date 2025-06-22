import os
import requests
import tweepy
from atproto import Client
from dotenv import load_dotenv
load_dotenv()  

message = """🎮 Canadian Gamer is LIVE!

📺 Twitch: https://twitch.tv/canadian_gamer23
📺 YouTube: https://youtube.com/@CanadianGamer23/streams
"""

# Post to Twitter
def post_to_twitter():
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
    client = Client()
    client.login(os.getenv("BLUESKY_HANDLE"), os.getenv("BLUESKY_PASSWORD"))
    client.send_post(text=message)
    print("✅ Posted to Bluesky")

if __name__ == "__main__":
    post_to_twitter()
    post_to_bluesky()
