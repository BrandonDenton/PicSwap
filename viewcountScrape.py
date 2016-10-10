#!/usr/bin/env python
import requests
import requests.auth
import json
import threading
import sys
import pymongo

def connectAndScrape():
    ## Connection stuff
    client = pymongo.MongoClient (host='da1.eecs.utk.edu')
    db = client['D2Discovery']
    twitchcoll = db.twitchstreams

    print(twitchstreams.find_one({"streams": ["game": "League of Legends"]})


if __name__ == '__main__':
    connectAndScrape()
