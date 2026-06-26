"""Loading username already captured or dumped in a json file"""
import json
filename = 'username.json'

with open(filename) as f:
    username = json.load(f)
    print(f'Welcome back, {username}!')