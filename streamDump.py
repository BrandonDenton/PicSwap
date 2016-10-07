#!/usr/bin/env python
import requests
import requests.auth
import json
import threading
import sys
import pymongo

clientid = "lje4lkmnfa7m2h2t0w3118sabdtcec5"
clients = "28cj2hjncgfk7lfchxo8lfahq3wy4cm"
twitchreq = "https://api.twitch.tv/kraken/streams/?game"
authstuff = "response_type=token&client_id=" + clientid + "&redirect_uri=http://localhost:65011"

def connectAndRecord():
   client = pymongo.MongoClient (host='da1.eecs.utk.edu')
   db = client ['D2Discovery']
   runOnInterval(db)

def runOnInterval(db):
    threading.Timer(1800.0, runOnInterval).start ()
    grabStreamInfo(db)

def grabStreamInfo(db):
    ## Open the config file and build game queries from its contents. ##
    gamelist = []   
    gamefile = open("gamelist.txt", 'r')
    for line in gamefile:
        gamelist.append(line.replace(" ", "%20"))

    recfile = open("recfile.txt", 'w')
    ## Build request queries and grab the data for each game tag. ##
    for i in gamelist:
        query = twitchreq + authstuff
        print(query)
    
        gameReq = requests.get(query)    # actually make the API request
        print(gameReq.status_code)
    
        json.dump(gameReq.json(), recfile)
        recfile.write("\n\n")
        
        db.twitchstreams.insert_one(gameReq.json())
        
if __name__ == '__main__':
    connectAndRecord()
