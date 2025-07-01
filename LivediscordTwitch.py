import os
import requests
# from dotenv import load_dotenv
# load_dotenv()  


def create_message():
    title = os.getenv("TITLE")
    message = f"""<@&824043811718168576> 🎮 Canadian Gamer is LIVE! Playing {title}

    📺 Twitch: https://twitch.tv/canadian_gamer23

    """

    return message
# Post to Discord
def post_to_discord():
    message = create_message()
    webhook_url = os.getenv("LIVE_DISCORD_WEBHOOK_URL")
    response = requests.post(webhook_url, json={"content": message})
    response.raise_for_status()
    print("✅ Posted to Discord")




if __name__ == "__main__":
    post_to_discord()

