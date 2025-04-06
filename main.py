from instagrapi import Client
import json

cl = Client()
cl.login("bot_god_hu", "nobihuyaar@11")  # Replace with your actual password

# Save session to file
cl.dump_settings("session.json")

print("✅ Session saved to session.json")
