import os
import requests
from dotenv import load_dotenv
load_dotenv()  


message = """<@&824043811718168576> 🎮 Canadian Gamer is LIVE!

📺 Twitch: https://twitch.tv/canadian_gamer23
📺 YouTube: https://youtube.com/@CanadianGamer23/streams
"""

# Post to Discord
def post_to_discord():
    webhook_url = os.getenv("LIVE_DISCORD_WEBHOOK_URL")
    response = requests.post(webhook_url, json={"content": message})
    response.raise_for_status()
    print("✅ Posted to Discord")




if __name__ == "__main__":
    post_to_discord()

