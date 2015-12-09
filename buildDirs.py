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
    '''builds PicSwap client's directory on a Windows platform'''
    try:    # try to find it first
        os.chdir("C:/picSwap_data")
    except OSError:    # If client's main directory is not here, make it.
        os.mkdir("C:/picSwap_data")
        os.chdir("C:/picSwap_data")
    
def makeGNUdirs():
    '''builds PicSwap directory on a Linux platform'''
    try:    # try to find it first
        os.chdir("C:/picSwap_data")
    except OSError:    # If client's main directory is not here, make it.
        os.mkdir("C:/picSwap_data")
        os.chdir("C:/picSwap_data")
