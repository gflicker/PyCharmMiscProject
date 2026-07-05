# Nicely formatting the data that is in the response from an API request
import requests
import json

response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
data = response.json()

# Pretty print - much easier to read
print(json.dumps(data, indent=2))

