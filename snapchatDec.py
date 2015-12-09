#!/usr/bin/env python
# Snapchat Media Decryption and Renaming
from Crypto import Cipher as c
import os       # need target file's stat struct

oldname = input('Please specify a .noMedia file in this directory: ')
encfile = open(oldname, 'r')
stats = os.stat(oldname)        # generate stat struct for target file's size
oldsize = stats.st_size
iv = oldsize        # need to read up on generating this for encrypted files

# may need to change key/cipher mode of operation with future Snapchat patches
crackit = c.AES.new('M02cnQ51Ji97vwT4', c.AES.MODE_ECB, iv)    # key in EVERY pre-2014 build!!!   

newname = oldname.replace(".nomedia", "")
decfile = open('new' + oldname + ext, 'w+')
while True:
    chunk = encfile.read(24*1024)
    if len(chunk) == 0:     # end of file, we're done
        break
    decfile.write(crackit.decrypt(chunk))   
    
decfile.truncate(oldsize)       # chop off byte padding from writing 24*1024 chunks
