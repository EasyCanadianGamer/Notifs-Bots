import os
import requests
import tweepy
from atproto import Client
# from dotenv import load_dotenv
# load_dotenv()  



def create_tweet_message():
    game = os.getenv("GAME")
    time = os.getenv("TIME")

    message = f"""🎮 YOOOO WASSUP!!! I AM GOING TO PLAY {game} live on Twitch at {time}!!!!!

    📺 Twitch: https://twitch.tv/canadian_gamer23
    #gaming #livestream #Twitch  #CG23
    """

    return message


def create_message():
    game = os.getenv("GAME")
    time = os.getenv("TIME")
    message = f"""🎮 YOOOO WASSUP!!! I AM GOING TO PLAY {game} live on Twitch at {time}!!!!!

    📺 Twitch: https://twitch.tv/canadian_gamer23
    #gaming #livestream #Twitch  #CG_BLUSKY
    """

    return message

# Post to Twitter
def post_to_twitter():
    message = create_tweet_message()

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
