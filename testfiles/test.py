#!/usr/bin/env python3
"""This is Project 3 for Alta3, program to demonstrate the use of flask -Blake Ellsworth"""

#These are import features of flask. Flask is a class of flask.
from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify

import json

# This makes it so we can just type app to call the program
app= Flask(__name__)

# This is a dictionary / list with information to be called upon
windrunner = [{
    "type": "Wind Runner",
    "first": "Kaladin \"Stormblessed\"",
    "spren": "honorspren",
    "abilities": [
        "Basic lashings",
        "Full lashings",
        "Reverse Lashings",
              ]
              }]
skybreaker = [{
    "type": "Skybreaker",
    "first": "Nalan\'Elin",
    "spren": "Highspren",
    "abilities": [
        "Gravitation",
        "Division",
              ]
              }]
dustbringer = [{
    "type": "Dustbringer",
    "first": "Malata",
    "spren": "Ashspren",
    "abilities": [
        "Division",
        "Abrasion",
              ]
              }]
edgedancer = [{
    "type": "Edgedancer",
    "first": "Lift",
    "spren": "cultivationspren",
    "abilities": [
        "Abrasion",
        "Progression",
              ] 
              }]
truthwatcher = [{
    "type": "Truthwatcher",
    "first": "Renarin",
    "spren": "Mistspren, or voidspren",
    "abilities": [
        "Progression",
        "Illumination",
              ]
                }]
lightweaver = [{
    "type": "Lightweaver",
    "first": "Shallan",
    "spren": "Cryptic spren",
    "abilities": [
        "Illumination",
        "Transformation",
              ]
                }]
elsecaller = [{
    "type": "Elsecaller",
    "first": "Jasnah",
    "spren": "Inkspren",
    "abilities": [
        "Transformation",
        "Transportation",
              ]
                }]
willshaper = [{
    "type": "Willshaper",
    "first": "Venli",
    "spren": "Lightspren",
    "abilities": [
        "Transportation",
        "Cohesion",
              ]
                }]
stoneward = [{
    "type": "Stoneward",
    "first": "Talatin",
    "spren": "Unknown",
    "abilities": [
        "Cohesion",
        "Tension",
              ]
                }]
bondsmith = [{
    "type": "Bondsmith",
    "first": "Dalinar",
    "spren": "Splinter of the Almighty",
    "abilities": [
        "Tension",
        "Adhesion",
              ]
             }]

# This is the information that is posted upon the post request
@app.route("/", methods=["GET","POST"])
def index():

    if request.method == 'POST':
        data = request.json
        if data:
           data= json.loads(data)

           # These are setting up variables to call upon the dictionary / list above
           # These do not post in the order writting on here if you run program and check link. No idea why
           type = data["type"]
           first = data["first"]
           spren = data["spren"]
           abilities = data["abilities"]
        
           # How information should be shared when posted
           windrunner.append({"Type of Radiant ":type,"The first radiant of this type ":first,"This radiant uses a ":spren,"These radients use ":abilities})
           skybreaker.append({"Type of Radiant ":type,"The first radiant of this type ":first,"This radiant uses a ":spren,"These radients use ":abilities})
           dustbringer.append({"Type of Radiant ":type,"The first radiant of this type ":first,"This radiant uses a ":spren,"These radients use ":abilities})
           edgedancer.append({"Type of Radiant ":type,"The first radiant of this type ":first,"This radiant uses a ":spren,"These radients use ":abilities})
           truthwatcher.append({"Type of Radiant ":type,"The first radiant of this type ":first,"This radiant uses a ":spren,"These radients use ":abilities})
           lightweaver.append({"Type of Radiant ":type,"The first radiant of this type ":first,"This radiant uses a ":spren,"These radients use ":abilities})
           elsecaller.append({"Type of Radiant ":type,"The first radiant of this type ":first,"This radiant uses a ":spren,"These radients use ":abilities})
           willshaper.append({"Type of Radiant ":type,"The first radiant of this type ":first,"This radiant uses a ":spren,"These radients use ":abilities})
           stoneward.append({"Type of Radiant ":type,"The first radiant of this type ":first,"This radiant uses a ":spren,"These radients use ":abilities})
           bondsmith.append({"Type of Radiant ":type,"The first radiant of this type ":first,"This radiant uses a ":spren,"These radients use ":abilities})
    
    # I should probably write this a better way, but stuff wasnt working... and this did.
    return jsonify(windrunner, skybreaker, dustbringer, edgedancer, truthwatcher, lightweaver, elsecaller, willshaper, stoneward, bondsmith)

# I dont know what this does, but its said its best practice to use
if __name__ == "__main__":
    
    # This is the main method of the program. When someone sends request to this IP/port
    app.run(host="0.0.0.0", port=2224)

