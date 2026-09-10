from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
port = os.getenv("PORT")
url = os.getenv("DATABASE_URL")

print(api_key)
print(port)
print(url)