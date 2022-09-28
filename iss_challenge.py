#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
import datetime
    
URL= "http://api.open-notify.org/iss-now.json"
def main():
    # This accesses the API
    resp= requests.get(URL).json()

    #This sets up the Lon/lat variables from the API
    lon= resp["iss_position"]["longitude"]
    lat= resp["iss_position"]["latitude"]

    ts = resp["timestamp"]
    ts = datetime.datetime.fromtimestamp(ts) 

    print(f"""
    Current Location of the ISS:
    Timestamp: {ts}
    lon: {lon}
    lat: {lat}
    """)

if __name__ == "__main__":
    main()
