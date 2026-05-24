import requests
import os
from dotenv import load_dotenv

load_dotenv()
COINGECKOAPIKEY = os.getenv("COINGECKOAPIKEY")

url = "https://api.coingecko.com/api/v3/simple/price"
headers = {"x-cg-demo-api-key": COINGECKOAPIKEY}
params = {"ids": "bitcoin-cash", "vs_currencies": "usd"}

response = requests.get(url, headers = headers, params = params)
data = response.json()
print(data)