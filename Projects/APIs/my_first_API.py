import requests

# Making a GET request to an API
response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")

# Checking if the request was a success
status_for_request = response.status_code
if status_for_request == 200:
    print("Pokemon found, your request was successful")
    print(f'Status Code: {response.status_code}')
else:
    print("Request failed")
    print(f'Status Code: {status_for_request}')

# Converting the response into a python dictionary
data = response.json() #this code converts the response into a dictionary

# Extract some of the information that might be useful for one's request
print("Name:", data["name"])
print("Height:", data["height"])
print("Weight:", data["weight"])
print("Base experience:", data["base_experience"])

print(f'{type(data)} this is they type of data')
print(f'{type(response.text)} this is they type of response')

# Trying to see what is contained in data
print(data)
