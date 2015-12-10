#!usr/bin/env python
########################################################################
# Stripped-down Snapchat Clone Server
# AUTHOR: Brandon Denton
#
# This script is intended to connect to a companion client application
# "picSwap.py" via a socket it creates to the server machine and send a
# file intended for that client through that socket. Right now, the 
# user has to define the file sent from the server by user input, but 
# eventually I'll have "server.py" search a directory on the host 
# machine made especially for the user currently connecting to it and 
# send that client files stored there.
########################################################################
#import logging as logs
import socket as S
import os    # We need to make a directory to store user keys and files to be sent.

loginsock = S.socket(S.AF_INET, S.SOCK_STREAM)    # listen for login requests
updatesock = S.socket(S.AF_INET, S.SOCK_STREAM)    # listen for message update requests
sendsock = S.socket(S.AF_INET, S.SOCK_STREAM)    # listen for new files to send

## My scheme for the server requires it to listen for requests on three ports, ##
## one for each required service, listed below:                                ##
##                                                                             ##
##    port 24601 - login requests (At last, Valjean, we see each other plain!) ##
##    port 24602 - message update requests                                     ##
##    port 42069 - requests to send a file (listen 4 dank memes)               ##

host = S.gethostname()           # grab this machine's name
print host
sendsock.bind((host, 42069))     # bind host to socket to receive files from clients

sendsock.listen(5)
print('Listening for send requests...')

sendconn = -2    # flags for while loop below
while True:    # continuously listen on all three ports
    ## Receive a file a user wants to send. ##
    fin = open("rec.txt", "wb")    # file we will create

    while sendconn == -2:
        sendconn, clientaddr = sendsock.accept()    # Now prepare to write the contents of an encrypted file!
    
        
        print(clientaddr, ' wants to send a file!')
        flag, i = "1", 0
        flag = sendconn.recv()   # If this flag is ever set to zero, the client is done sending files. 
        key = sendconn.recv()    # get the AES key for the session
        keyfile = open("aeskey", "wb")
        keyfile.write(key)    # record the key for later use
        keyfile.close()
        
        ## Now record the encrypted file the client user has sent. ##
        while(flag == "1"):
            fileContents = sencconn.recv()
            name = str(i) + "_"
            f = open(name, "wb")
            f.write(fileContents)
            f.close()
            
            i += 1
            flag = sendconn.recv()    # will send "1" if more files, "0" if no more
        
        sendconn.close()
        sendconn = -2
    sendsock.listen(5)
    print('Listening for send requests...')
