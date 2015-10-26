#!usr/bin/env python
##################################################################
# Working Directory Builder for PicSwap Client
# AUTHOR: Brandon Denton
#
# THE FOLLOWING SCRIPT SERVES THE PURPOSE DESCRIBED BELOW. ITS 
# AUTHOR MAKES NO GUARANTEES OF ITS FITNESS FOR ANY OTHER PURPOSE. 
#
# This module is intended to create necessary directories for the
# proper runtime functions of PicSwap, a simple file sharing
# client written in Python. The client needs to store the public
# encryption keys for a user's friends as well as temporary files
# sent to the user via my server that hosts and distributes files
# sent through the users' PicSwap clients on multiple OS's. 
##################################################################

import os    # directory navigation
import getpass    # We want to suppress user input, if they need to set their password.

def makeWindirs():
    '''builds PicSwap client's file structure on a Windows platform'''
    try:    # try to find it first
        os.chdir("C:/picSwap_data")
    except OSError:    # If client's main directory is not here, make it.
        os.mkdir("C:/picSwap_data")

    ## If any of the client's subdirectories are not here, make them. ##
    try:
        os.chdir("C:/picSwap_data/account")    # user info and friends' public keys
    except OSError:
        os.mkdir("C:/picSwap_data/account")
    try:    
        os.chdir("C:/picSwap_data/account/keys")
    except OSError:
        os.mkdir("C:/picSwap_data/account/keys")
    os.chdir("C:\picSwap_data")
    try:
        os.chdir("C:/picSwap_data/temp")    # temporary files (simulates Snapchat's policy
    except OSError:
        os.mkdir("C:/picSwap_data/temp")    
        
    # Check for the user's account info and activity log.
    os.chdir("C:/picSwap_data/account")
    try:
        usr = open("usr.INFO", 'r')
    except FileNotFoundError:
        name = input('Please choose a username: ')
        pwd = getpass.getpass('Please choose a password: ')
        usr = open("usr.INFO", 'w')
        usr.write(name + "\n" + pwd)
        usr.close()
        ## Encrypt this with a private key generated for the user. ##    
    try:
        act = open("activity.LOG", 'r')
    except FileNotFoundError:
        act = open("activity.LOG", 'w')
        act.write(name + "\n\n------ ACCOUNT ACTIVITY ------\n")
        act.close()
    
def makeGNUdirs():
    '''builds PicSwap client's file structure on a Linux platform'''
    try:    # try to find it first
        os.chdir("~/picSwap_data")
    except OSError:    # If client's main directory is not here, make it.
        os.mkdir("~/picSwap_data")

    ## If any of the client's subdirectories are not here, make them. ##
    try:
        os.chdir("~/picSwap_data/account")    # user info and friends' public keys
    except OSError:
        os.mkdir("~/picSwap_data/account")
    try:    
        os.chdir("~/picSwap_data/account/keys")
    except OSError:
        os.mkdir("~/picSwap_data/account/keys")
    try:
        os.chdir("~/picSwap_data/temp")    # temporary files (simulates Snapchat's policy
    except OSError:
        os.mkdir("~/picSwap_data/temp")            
        
    # Check for the user's account info and activity log.
    os.chdir("~/picSwap_data/account")
    try:
        usr = open("usr.INFO", 'r')
    except FileNotFoundError:
        name = input('Please choose a username: ')
        pwd = getpass.getpass('Please choose a password: ')
        usr = open("usr.INFO", 'w')
        usr.write(name + "\n" + pwd)
        usr.close()
        ## Encrypt this with a private key generated for the user. ##    
    try:
        act = open("activity.LOG", 'r')
    except FileNotFoundError:
        act = open("activity.LOG", 'w')
        act.write(name + "\n\n------ ACCOUNT ACTIVITY ------\n")
        act.close()     
