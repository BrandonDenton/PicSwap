#!/usr/bin/env python
import requests
import requests.auth
import json
import threading
import sys
import pymongo

def scrapeViews(gameName):
	client = pymongo.MongoClient (host='da1.eecs.utk.edu')
	db = client ['D2Discovery']
	
	view = db.twitchstreams.find({"streams": {"channel": {"game": gameName}}}, "viewers")
	return(view)
	
def queryGames():
	## Open the config file and build game queries from its contents. ##
    viewsOfGames = []
	gamefile = open("gamelist.txt", 'r')
	graphfile = open("graphfile.txt", 'wb')
	
	for i in gamefile:
		viewsOfGames[i] = scrapeViews(i)
		
	return(viewsOfGames)
	
if __name__ == '__main__':
    queryGames()
