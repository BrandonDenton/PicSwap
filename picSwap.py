#!usr/bin/env python
######################################################################
# "PicSwap" Encrypting File Sharing Client
# AUTHOR: Brandon Denton
#
# THE FOLLOWING SCRIPT SERVES THE PURPOSE DESCRIBED BELOW. ITS AUTHOR
# MAKES NO GUARANTEES OF ITS FITNESS FOR ANY OTHER PURPOSE. THE 
# AUTHOR IS ALSO NOT RESPONSIBLE FOR ANY DATA TRANSMITTED VIA THE
# SERVICE DESCRIBED BELOW. UTILIZE THE SERVICE AT YOUR OWN DISCRETION. 
#
# This script is the frontend for a general-purpose file sharing 
# service that applies encryption in CBC mode to files it sends. The
# script currently determines what files to send via user input to 
# the command line and allows a user to "add friends", a process 
# which queries the server for a desired username and distributes 
# the public key associated with that name to the user for later 
# decryption of files that desired user may send with their public 
# key.
######################################################################
import socket
import os
from sys import platform as Platform
import getpass    # We want to suppress user input of their password.
import buildDirs as bd    # helper module that build's client's directory system

def msgUpdate():
    ''' This function, which executes at least once at runtime and 
    also upon user request, queries the server for files that the 
    user's friends have delivered to the server to be sent to the 
    user. If any exist in the user's directory on the server, the 
    server sends each file there to the user via the open socket. '''
    while True:
        data = clients.recv(16)
        if data:
            print >>sys.stderr, 'sending data back to the client'
            clients.sendall(data)
        else:
            print("Done!\n\n")
            break
            
def send(fname=''):
    ''' This function sends a specified file via the socket already
    opened to my server in 2K chunks. Don't make the server handle 
    files larger than 5 GB.'''
    os.chdir("C:\picSwap_data")
    if(fname == ''):
        fname = raw_input('What file would you like me to send? ')
    while(fname != "none" or fname != "I'm done." or fname != "done"):
        with open(fname, "rb") as f:
            finfo = os.stat(fname)                # Put a cap on filesize so the server 
            #if(finfo.st_size > (1024^4)*5):      # doesn't fill quickly/get congested.
            #    print("File " + fname + " is too big. Please send something 5 GB or smaller.\n")
            #    break
            for line in f:
                clients.send(line)    # buffering out 1K at a time
            if not line: break
        fname = raw_input('What file would you like me to send? ')


## If the picSwap client doesn't have its own directory and ##
## subdirectories for the user's friends' public keys and   ##
## temporary files, make them. This functionality must be   ##
## filesystem independent, hence the need for sys.platform. ##
if(Platform == "win32"):
    bd.makeWindirs()
elif(Platform == "linux" or Platform == "darwin"):
    bd.makeGNUdirs()

## Now we must query the user for their username and password. ##
name = raw_input('username: ')
pwd = getpass.getpass('password: ')
## THIS IS JUST A PLACEHOLDER. Have the client query the       ##
## server for this verification after you get sockets working. ##
if(Platform == "win32"):
    os.chdir("C:/picSwap_data/")
#    usr = open()
    
## Now that we've ensured we have a place to store needed   ##
## files for the client, it's time to start allowing the    ##
## user to send files to his or her friends. SOCKET TIME!!! ##
host = '50.142.36.252'    # need my broadcasting address here
port = 80    # This, like my server hostname, should hopefully never change.
clients = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clients.connect((host, port))

msgUpdate()    # Always check for new files from friends at least once each time we run the client.

print("---------------------\n----- Main Menu -----\n---------------------\n")
print("Type the following commands:\n  * send (Send a file.)\n  * update (Get files other users sent to you.)\n  * quit (Exit the program.)\n\n")
while True:
    option = raw_input('What would you like to do? ')
    if(option == 'send'):
        send()
    elif(option == 'update'):
        msgUpdate()
    elif(option == 'quit'):
        option = raw_input('Are you sure? y/n ')
        if(option == 'y' or option == 'yes'):
            break    # The user is done. Close the client application.
    # Easter eggs lol #
    elif(option == 'Afghanistan'):
        send("C:\picSwap_data\account\A_weapon_to_surpass_Metal_Gear.txt")
    else:
        print("I don't understand. Please pick something else.")
