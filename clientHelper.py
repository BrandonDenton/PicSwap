#!usr/bin/env python
#######################################################################
# PicSwap Communication Helper
# AUTHOR: Brandon Denton
#
# THE FOLLOWING SCRIPT SERVES THE PURPOSE DESCRIBED BELOW. ITS AUTHOR
# MAKES NO GUARANTEES OF ITS FITNESS FOR ANY OTHER PURPOSE. THE 
# AUTHOR IS ALSO NOT RESPONSIBLE FOR ANY DATA TRANSMITTED VIA THE
# SERVICE DESCRIBED BELOW. UTILIZE THE SERVICE AT YOUR OWN DISCRETION. 
#
# This module is intended to facilitate sending and receiving files by
# the client "picSwap.py". msgUpdate() checks for new files intended 
# for receiving by the client, and send() sends files from the client
# to the server, such that the server can send the file to the proper
# user once he or she runs the client or calls msgUpdate().
#######################################################################
import os
import socket
from sys import platform as Platform
#from msvcrt import getch    # Press any key to exit.

def serverConnect():
    ''' This function creates a socket for the client on a  
    user's machine to communicate with the PicSwap server.
    If we can't see the server on the specified port, the 
    user is asked to exit the program. Otherwise, the 
    function returns the socket object for the connection. '''
    print("Connecting to server...")
    host = "50.142.36.252"    # Just host it on Hydra because your router hates every port you want to use.
    port = 24601    # This, like my server hostname, should never change.
    clientr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        clientr.connect((host, port))
    except:
        print("Unable to connect to server. Sorry for the inconvenience!\nPress any key to exit.\n")
        #exout = getch()
        exit(1)

def msgUpdate():
    ''' This function, which executes at least once at runtime and 
    also upon user request, queries the server for files that the 
    user's friends have delivered to the server to be sent to the 
    user. If any exist in the user's directory on the server, the 
    server sends each file there to the user via the open socket. '''
    host = "50.142.36.252"    # Just host it on Hydra because your router hates every port you want to use.
    print("Looking for new messages...")
    port = 24602    # This, like my server hostname, should never change.
    try:
        clientu = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientu.connect((host, port))
    except:    # No new messages or server timeout
        print("You're up to date!\n")
    print("Done!\n\n")
            
def send(fname=''):
    ''' This function sends a specified file via the socket already
    opened to my server in 2K chunks. Don't make the server handle 
    files larger than 5 GB.'''
    host = "50.142.36.252"
    port = 42069    # This, like my server hostname, should never change.
    clients = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        clients.connect((host, port))
        return clientr    # client app will need this connection for file transfer
    except:
        print("Unable to connect to server")
    if(fname == ''):
        fname = raw_input('What file would you like me to send? ')
    while(fname != 'none'):
        print os.getcwd()
        try:
            with open(fname, "rb") as f:
                # finfo = os.stat(fname)                # Put a cap on filesize so the server 
                #if(finfo.st_size > (1024^4)*5):      # doesn't fill quickly/get congested.
                #    print("File " + fname + " is too big. Please send something 5 GB or smaller.\n")
                #    break
                for line in f:
                    clients.send(line)    # buffering out 1K at a time
                    if not line: break
            print(fname + " sent!")
        except:
            print("That file doesn't exist. Please select a different file.")
        fname = raw_input('What file would you like me to send? ')
