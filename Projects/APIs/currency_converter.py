import requests

import requests

API_KEY = "cbbacc55c18493943292705d"  # paste your actual key here

url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"

response = requests.get(url)
data = response.json()

print("Status:", data["result"])
print("Base currency:", data["base_code"])
print("ZMW rate:", data["conversion_rates"]["ZMW"])