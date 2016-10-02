#!/usr/bin/env python
import urllib, json
from requests_oauthlib import oAuth2Session
import twitchingpython
#import pymongo

app = Flask(__name__)

clientid = "lje4lkmnfa7m2h2t0w3118sabdtcec5"
clients = "28cj2hjncgfk7lfchxo8lfahq3wy4cm"
authrequest = "https://api.twitch.tv/kraken/oauth2/authorize"
tokrequest = "https://api.twitch.tv/kraken/oauth2/token"
gamerequest = "https://api.twitch.tv/kraken/streams/?game="

# define list of indexed game queries
gamelist = []
gamefile = open("gamelist.txt", 'r')
for line in gamefile:
    gamelist.append(line.replace(" ", "%20"))

#twitchconn = Oauth2Session(clientid)
#authurl, state = twitchconn.authorization_url(authrequest)
#session['oauth_state'] = state
        
for i in gamelist:
    query = gamerequest + i
    print(query)
    
    twitch = OAuth2Session(clientid, token=session['oauth_token'])
    
    gameQuery = urllib.urlopen(query)
    streamData = json.loads(gameQuery.read())

    print(json.dumps(streamData, indent=2, sort_keys=True))
    #gamelist[i].replace("%20", " ")     # strip query junk out to get game readable game name
    #gameViews = {}
    #gameViews[gamelist[i]] = viewcount
print(json.dumps(streamData, indent=2, sort_keys=True))
