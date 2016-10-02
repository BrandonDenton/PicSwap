#!/usr/bin/env python
import json
import requests
from requests.auth import HTTPBasicAuth
import twitchingpython
#import pymongo

# define list of indexed game queries
gamelist = []
gamefile = open("gamelist.txt", 'r')
for line in gamefile:
    gamelist.append(line.replace(" ", "%20"))
        
for i in gamelist:
    query = "https://api.twitch.tv/kraken/streams/?game=" + i
    print(query)
    #try:
    streamsByGame = requests.get(query)
    streamData = streamsByGame.json()

    print(json.dumps(streamData, indent=2, sort_keys=True))
    #gamelist[i].replace("%20", " ")     # strip query junk out to get game readable game name
    #gameViews = {}
    #gameViews[gamelist[i]] = viewcount
print(json.dumps(streamData, indent=2, sort_keys=True))