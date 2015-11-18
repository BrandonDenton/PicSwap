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
import clientHelper as ch

## If the picSwap client doesn't have its own directory and ##
## subdirectories for the user's friends' public keys and   ##
## temporary files, make them. This functionality must be   ##
## filesystem independent, hence the need for sys.platform. ##
if(Platform == "win32"):
    bd.makeWindirs()
elif(Platform == "linux" or Platform == "darwin"):
    bd.makeGNUdirs()

print("Welcome to PicSwap!")
if(Platform == "win32"):
    os.chdir("C:\picSwap_data")
print os.getcwd()
## Now we must query the user for their username and password. ##
name = raw_input('username: ')
pwd = getpass.getpass('password: ')
## THIS IS JUST A PLACEHOLDER. Have the client query the       ##
## server for this verification after you get sockets working. ##

## Navigate to the proper directory for pulling files to send. ##
print("Checking directories...")

## Now that we've ensured we have a place to store needed   ##
## files for the client, it's time to set up a socket so    ##
## the client can receive files from my server.             ##
ch.serverConnect()
    
## IMPLEMENTATION ISSUE WITH UPDATER, LOOK UP I/O REQUIREMENTS!!! ##
#ch.msgUpdate(clients)    # Always check for new files from friends at least once each time we run the client.

print("---------------------\n----- Main Menu -----\n---------------------\n")
print("Type the following commands:\n  * send (Send a file.)\n  * update (Get files other users sent to you.)\n  * quit (Exit the program.)\n\n")
while True:
    option = raw_input('What would you like to do? ')
    if(option == 'send'):
        ch.send()
    elif(option == 'update'):
        ch.msgUpdate()
    elif(option == 'quit'):
        option = raw_input('Are you sure? y/n ')
        if(option == 'y' or option == 'yes'):
            break    # The user is done. Close the client application.
    # Easter eggs lol #
    elif(option == 'Afghanistan'):
        ch.send("A_weapon_to_surpass_Metal_Gear.txt")
    else:
        print("I don't understand. Please pick something else.")
