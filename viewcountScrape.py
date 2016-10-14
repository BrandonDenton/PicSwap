#!/usr/bin/env python
import requests
import requests.auth
import json
import threading
import sys
import pymongo

def connectAndScrape(name):
    ## Connection stuff
    client = pymongo.MongoClient (host='da1.eecs.utk.edu')
    db = client['D2Discovery']

    print(db.twitchstreams.find({"streams": {"game": gameName}})

def genQueries():
    gamefile = open("gamefile.txt", "r")
    for name in gamefile:
        connectAndScrape(name)
    gamefile.close()

if __name__ == '__main__':
    genQueries()
