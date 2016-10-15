#!/usr/bin/env python
import requests
import requests.auth
import json
from bson.json_util import dumps as darkdump    # ばかな！
import threading
import sys
import pymongo
import csv

'''This function flattens the multi-tiered JSON
   objects returned from Twitch's API into a 
   single-layered object that's fit for a CSV
   file.'''
def flatten4csv(input):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(input)
    return out

def connectAndScrape(gameName):
    try:
        client = pymongo.MongoClient (host='da1.eecs.utk.edu', port=9109)
        db = client['D2Discovery']
        twitchstreams = db.twitchstreams
    except pymongo.errors.ServerSelectionTimeoutError:
        print("Error: Unable to connect to da1")
        twitchstreams = None
    
    if twitchstreams is not None:
        objflat = twitchstreams.find_one()
        #objflat = flatten4csv(db.twitchstreams.find({"streams": {"game": gameName}}))
        return(objflat)
    
def queryGames():
    ## Open the config file and build game queries from its contents. ##
    viewsOfGames = []
    gamefile = open("gamelist.txt", 'r')
    graphfile = open("graphfile.txt", 'wb')

    #for name in gamefile:
    #   print(connectAndScrape(name))
    connectAndScrape(viewsOfGames)
     
if __name__ == '__main__':
    queryGames()
