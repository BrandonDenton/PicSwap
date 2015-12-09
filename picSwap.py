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
import time    # delay for exit
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
## Now that we've ensured we have a place to store needed   ##
## files for the client, it's time to set up a socket so    ##
## the client can receive files from my server. If          ##
## serverConnect() returns -1, this means that the client   ##
## could not connect to the server or otherwise create a    ##
## socket on port 42069.                                    ##
sendSock = ch.serverConnect()
    
if(sendSock == -1):    # could not create a socket to connect to the server
    while(sendSock == -1):    # try to connect as many times as the user wants
        tryAgain = raw_input("Would you like to try again? ")
        if(tryAgain == "yes" or tryAgain == "y" or tryAgain == "y" or tryAgain == "Y"):
            sendSock = ch.serverConnect()
        else:    # close the client
            print("Goodbye!")
            time.sleep(3)
            if(Platform == "win32"):
                os.system('cls')
            else:
                os.system('clear')
            exit(0)

print("-------------------------------\n----- Welcome to PicSwap! -----\n-------------------------------\n")    # MENU SCREEN HYPE
key = ch.generateKey()    ## Generate a pseudrandom AES key for this session. ##
while True:
    ch.send(sendSock, key)    # Apply the key above to each file sent IN THIS SESSION.

#    elif(option == 'Afghanistan'):
#        ch.send("A_weapon_to_surpass_Metal_Gear.txt")

    # Ask the user if they want to send another file. ##
    again = raw_input("Would you like to send another file? ")
    if(again == "yes" or again == "y" or again == "y" or again == "Y"):
        ch.send(sendSock, key)
    else:    # Wait 3 seconds, clear the console, and exit the client.
        print("Thank you for using PicSwap! Goodbye!")
        time.sleep(3)
        if(Platform == "win32"):
            os.system('cls')
        else:
            os.system('clear')
        exit(0)
