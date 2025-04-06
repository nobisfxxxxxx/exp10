from instagrapi import Client
import json

cl = Client()
cl.load_settings("session.json")
cl.login("bot_god_hu", "nobihuyaar@11")  # Replace with your actual password

# Your bot logic here
print("Bot is running...")
