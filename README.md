# PicSwap Client and Supplementary Files
  This repo contains components of a final project for the Introduction to Computer Security course at the University of Tennessee, including a client for a simple filesharing service that will apply encryption in cipher-block chaining (CBC) mode with an AES-256 key to all files it sends. It also contains the server that receives and writes encrypted files to disk, along with the AES keys used for each client session. Finally, I have included a script that decrypts files sent to the server's host machine using the aforementioned AES-256 key called "picSwapRead.py".
  
# Dependencies
  Python 2.7 or later, pyCrypto2.6.1, picSwap.py, clientHelper.py, buildDirs.py
  
  NOTE: Currently file transfer only happens one way from client(s) to the server. You are welcome to test the software for            yourself, but keep this limitation in mind when doing so.
  
  Download all three files and save them to the same directory (regardless of where you save them, PicSwap will put its necessary client-side stuff in its own folder in your home directory). Feel free to email me at bdenton418@gmail.com and tell me how your client can/cannot connect to the server. Be sure to put files you want to send in the directory "C:/picSwap_data" if you are testing the client on a Windows platform or "~/picSwap_data" if testing it on a GNU/Linux platform; the client will create both these directories for you, if you don't already have them.

# Please read this! :)
  This is a student project meant to highlight the encryption implementation that ought to be employed by the client of the popular image and video sharing service Snapchat. As such, my development priority is ensuring security of the temporary files stored by the client that are sent to it by other users. While the file transfer service is functional from client to server, the service itself is not the focus of the project. Depending on your network limitations, the server may be slow to respond in some cases. Experiences with the service may vary. 
  Furthermore, by using this service, you agree to refrain from using it to transfer explicit content or content that facilitates academic dishonesty. Beyond that, maintain the same discretion that you would exhibit when using any social application; if you wouldn't staple it to a lamppost, don't send it via PicSwap. I am not responsible for any files successfully sent via the service. Keeping all that in mind, I welcome any students of the course listed above to test the client once the server is up and running!
