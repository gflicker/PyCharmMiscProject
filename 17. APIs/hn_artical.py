# Making sure that data from the call which is more kind of text in a list is formatted
# into a dictionary by using json.dump()
import requests
import json

# Make an API call, and store the response
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Exploring the structure of the data.
response_dict = r.json() #Changing the format into a json file which is a dictionary

readable_file = 'data/readable_hn_data.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)

# Opening the file that has been saved and see how data has been formatted
filename = 'data/readable_hn_data.json'
with open(filename) as reading:
    review = reading.read()
    print(review)

