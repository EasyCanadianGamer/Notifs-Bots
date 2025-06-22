import os
import requests
from dotenv import load_dotenv
load_dotenv()  



def create_message():
    yt_link = os.getenv("YOUTUBE_LINK")
    yt_title = os.getenv("YOUTUBE_TITLE")
    message = f" <@&1095573872578928641>🎮 Canadian Gamer is Just uploaded a new video: {yt_title}: {yt_link}"

    return message

# Post to Discord
def post_to_discord():
    message = create_message()
    webhook_url = os.getenv("VIDEO_DISCORD_WEBHOOK_URL")
    response = requests.post(webhook_url, json={"content": message})
    response.raise_for_status()
    print("✅ Posted to Discord")




if __name__ == "__main__":
    post_to_discord()

