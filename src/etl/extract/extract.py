import os
import base64
import requests
from dotenv import load_dotenv

# Load values from .env into environment variables
load_dotenv()

client_id = os.getenv("client_id_prd")
client_secret = os.getenv("client_secret_prd")
oauth_url = os.getenv("oauth_url_prod")
api_base = os.getenv("api_base_url_prod")
scope = os.getenv("oauth_scope")

# ---- Get OAuth token ----
credentials = f"{client_id}:{client_secret}"
encoded_credentials = base64.b64encode(credentials.encode()).decode()

headers = {
    "Authorization": f"Basic {encoded_credentials}",
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "grant_type": "client_credentials",
    "scope": scope
}

token_response = requests.post(oauth_url, headers=headers, data=data)
token_response.raise_for_status()

access_token = token_response.json()["access_token"]

# ---- Call Browse API ----
search_url = f"{api_base}/buy/browse/v1/item_summary/search"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

params = {
    "q": "taylormade-sim-2",
    "limit": 1
}

response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()

print(response.json())