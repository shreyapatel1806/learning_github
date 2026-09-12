from dotenv import load_dotenv
import os

load_dotenv()

# api_key = os.getenv("API_KEY")
# port = os.getenv("PORT")
# url = os.getenv("DATABASE_URL")

# print(api_key)
# print(port)
# print(url)


import json

with open("config.json", "r") as file:
    config = json.load(file)

print(config["app"]["name"])
print(config["server"]["host"])
print(config["server"]["port"])