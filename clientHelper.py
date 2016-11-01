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
from Crypto.Cipher import AES    # clientHelper is the only module that actually does encryption
## The following modules help us generate PSEUDORANDOM alphanumeric AES keys. ##
import string
import random
import struct
from sys import platform as Platform
#from msvcrt import getch    # Press any key to exit.

def generateKey(size=32, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    '''This function generates a pseudorandom AES key each time the client
    runs. This key is applied to each file in its session with the server
    until the user closes the client.'''
    return ''.join(random.choice(chars) for _ in range(size))

def serverConnect():
    ''' This function creates a socket for the client on a  
    user's machine to communicate with the PicSwap server.
    If we can't see the server on the specified port, the 
    user is asked to exit the program. Otherwise, the 
    function returns the socket object for the connection. '''
    print("Connecting to server...")
    host = "succ"    # Just host it on Hydra because your router hates every port you want to use.
    port = 42069    # This, like my server hostname, should never change.
    sendSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sendSock.connect((host, port))
        return sendSock
    except:
        print("Unable to connect to server. Sorry for the inconvenience!")
        return -1
            
def send(sendSock, key):
    ''' This function sends a specified file via the socket already
    opened to my server on port 42069. Don't make the server handle 
    files larger than 5 GB.'''

    fname = raw_input('What file would you like me to send? ')
    a = 0    # flag for checking to see if the file the user wants to encrypt is in picSwap's directory
    while(fname != 'none'):
        sendSock.send("1")
        print os.getcwd()
        try:
            ftest = open(fname, "rb")
            ftest.close()
        except:
            print("That file doesn't exist. Please select a different file.")  
            a = -1
            fname = "none"
        
        if(a != -1):
            sendSock.send(key)    # Send the AES key for this session's files to the server.
            IV = 16 * '\x00'           # Initialization vector
            mode = AES.MODE_CBC        # cipher block chaining
            encryptor = AES.new(key, mode, IV=IV)    # Crypto does the heavy lifting!
            outName = "ENC_" + fname    # name of file to send
            fsize = os.path.getsize(fname)    # for encrypted file to send
            
            with open(fname, "rb") as f:
                with open(outName, 'wb') as out:
                    # finfo = os.stat(fname)              # Put a cap on filesize so the server 
                    #if(finfo.st_size > (1024^4)*5):      # doesn't fill quickly/get congested.
                    #    print("File " + fname + " is too big. Please send something 5 GB or smaller.\n")
                    #    break
                    ## header for encrypted file ##
                    out.write(IV)
                    out.write("\n")
                    
                    while True:
                        chunk = f.read(1024)    # buffer out 1024 bytes to write to out
                        if(len(chunk) == 0):
                            break
                        elif(len(chunk) % 16 != 0):
                            chunk += ' ' * (16 - len(chunk) % 16)
                        
                        ## Now write the buffered contents of the file to out. ##
                        out.write(encryptor.encrypt(chunk))
                outf = open(outName, 'rb')
                outData = outf.read()
                outf.close()
                sendSock.send(outData)              
            print(fname + " sent!")
        fname = raw_input('What file would you like me to send? ')    # Ask for another file to send.
    sendSock.send("0")    # We're done sending files. 
