from instagrapi import Client

USERNAME = "bot_god_hu"
PASSWORD = "nobihuyaar@11"  # Replace with your actual password

cl = Client()
cl.login(USERNAME, PASSWORD)
cl.dump_settings("session.json")
print("✅ Session saved to session.json")
