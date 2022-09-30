#!/usr/bin/env python3

# This is used to get requests and send information in json per requirement 1
import requests
import json

# This allows us to use pretty printer
from pprint import pprint

# This is the "user ip default from example wasnt sure if I should change it"
URL = "http://127.0.0.1:2224/"

#adds a new information after the radiants
shardbearer = {
           "type": "Shardbearer",
           "first": "While not the first, Adolin Kohnlin is one of the best",
           "spren": "Mayalaran, dead spren Shardblade",
           "abilities": [
                "Summon shardblade",
                "Enhanced strength",
                "Self-adjusting plate armor"
                ]
          }

# json.dumps takes a python object and returns it as a JSON string
shardbearer = json.dumps(shardbearer)

# this is sending a post request and converting to a json
resp = requests.post(URL, json=shardbearer)

# pretty-print the response back from our POST request
pprint(resp.json())

