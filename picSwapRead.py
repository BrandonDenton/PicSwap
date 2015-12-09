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
import time
from Crypto.Cipher import AES    # decryption

def decrypt(in_file, out_file, password, iv, key_length=32):
    bs = AES.block_size
    cipher = AES.new(key, AES.MODE_CBC, iv)
    next_chunk = ''
    finished = False
    while not finished:
        chunk, next_chunk = next_chunk, cipher.decrypt(in_file.read(1024 * bs))
        if len(next_chunk) == 0:
            padding_length = ord(chunk[-1])
            chunk = chunk[:-padding_length]
            finished = True
        out_file.write(chunk)
        
fname = raw_input("What file would you like to decrypt? ")
while(fname != "none"):
    i = 0
    with open(fname, "rb") as encf:
        for line in encf:
            if i == 0:
            iv = encf.read()
            i == 1
    
    decname = "DEC_" + fname
    decf = open(decname, "wb")
    encf2 = open(fname, "rb")
    keyf = open("aeskey", "rb")
    key = keyf.read()
    keyf.close()
    
    decrypt(encf2, decf, key)
    encf2.close()
    decf.close()
    
print("Goodbye!")
time.sleep(3)
os.system('cls')
exit(0)
