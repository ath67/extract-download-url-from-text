import time
try:
   import wget
   print("WGET module found!")
except ImportError:
   print ("WGET module not found, try to install it before running the script. Search for 'pip intall'. This warning will be on screen for 1:30 minutes")
   time.sleep(90)

import wget, os

a= 's'
arquivo = input("Type the filename with the extension. The file should be on the script's root. FILENAME:   ")
a = open(arquivo, 'r', encoding="utf8") #reading file with original text
text = a.read()
a.close()
print ('-'*80) 
print("Text selected:")
print(text)                 #print original text
print ('-'*80)

#cleaning original text:
a1=text.replace("\n", " ")  #puts everything in only one line (deletes any '\n')
a1=a1.replace("http", " http")  #creates a space between any frase that have "XXX:http" so split() consider the http a separete word
a11=a1.split()              #creates a list that every text in the a1 is an item

if type(a11)!= list:    #print a check to make sure a11 is a list
   print ("Error with text list generated, please contact dev")
   time.sleep(60)
   exit()


y=1
linksVAR=set()
linksREAD=set()
print ('-'*80)
print ('-'*80) 
for string in a11:          #loop that will filter every list item that has "http"
    if 'http' in string:
        linksVAR.add(string) 
        opn=open('url-list.txt', 'a')  #creates file for output if already doesnt exists
        opn.close()
        textfinal = open('url-list.txt', 'r+')  #appends links to an .txt file on script's root
        reading = textfinal.read()
        if string in reading:             #ignores file already downloaded before (checks the output text file)
           linksVAR.remove(string)
           
        else:
           print("Link #", y,  "in text.", " URL:", string)  #Prints an couter of processed urls and it's URL/item with http
           linksREAD.add(string)
           time.sleep(0.3)
           textfinal.write(string + '\n')
           textfinal.close()
        y=y+1                #sum to the couter
print ('-'*80)
print ('-'*80) 
print("Waiting 15 sec for checking the URLs above. If there's none, you already run every link!")
time.sleep(15)
check=input("If everything is fine, type 'OK' (all caps), if not type anything different:  ")   #checks if user approves list of links
if check != "OK":
   print("Deleting links above from output file and closing scprit in 10 sec...")
   #Deleting the urls from 'url-list.txt' as request of user
   outputx= open('url-list.txt', 'r+')    #reads file with urls to be deleted
   outputxreading = outputx.read()
   out2=set()
   out1=outputxreading.replace("\n", " ")
   out2=out1.split() #transforms url-list into an list variable
   for string in out2:
      if string in linksREAD:             #removes all the urls that were added to the file in this run of the script (they were saved into the linksREAD variable
           out2.remove(string)
   tx=open("url-list.txt", "w+")          #overwrites the 'url-list.txt' file to do a new one without the wrong urls
   tx.close
   for string in out2:
      tx=open("url-list.txt", "a")
      tx.write(string + "\n")             #appends each url of the list to the file
      tx.close
   time.sleep(10)
   exit()                     #kills the script



dirpath = os.getcwd()       #find script's root

mypath = dirpath + '\wgetfiles' #directory to save files
if not os.path.isdir(mypath):       #creates the directory/paste if it doesnt exist yet
    os.makedirs(mypath)


s= len(linksVAR) - (len(linksVAR)-1)
print('There are ', len(linksVAR), ' items to download.') #prints list length (number of itens to download)
print ('-'*80)
print ('-'*80)
for i in linksVAR:       #loop that downloads every url in a 'clean file'
    linkbaixar= i     #reads list itens
    print('__________downloading item nº', s, ':', i) #prints current item wich is being downloaded
    wget.download(linkbaixar, out=mypath)           #wget's the item/url
    s += 1
print ('-'*80)
print ('-'*80)
print("Finished downloading! This message will stay on screen for 40 sec! Bye!!")
time.sleep(40)
