# extract-download-url-from-text
It is a simple script that picks a big text message with urls in it and extract it, saves a TXT file and also downloads the files to a folder.


## USAGE
1. You need to have a file on the script directory with some message and some url in it. When running the script will ask you to input the filename.
2. It will generate a file **"links-tratados.txt"** on the directory (if you run multiple times with different messages, the script will append to this file).
3. After that it will run wget and download files to a new paste named **"wgetfiles"** on its directory.


## FUTURE GOALS

- [ ] Translate to English.  
- [ ] Make wget use multiple processing.  
- [ ] Use as set to save the urls to text file so it doesnt append duplicate urls.  
- [ ] Clean the terminal messages shown.  

