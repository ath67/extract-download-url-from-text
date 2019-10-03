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
a = open(arquivo, 'r') #reading file with original text
text = a.read()
a.close()
print(text)                 #print original text
a1=text.replace("\n", " ")  #puts everything in only one line (deletes any '\n')
a1=a1.replace("http", " http")  #creates a space between any frase that have "XXX:http" so split() consider the http a separete word
a11=a1.split()              #creates a list that every text in the a1 is an item
print(a1)                   #prints the text before splitting
print("splits=", str(a11))  #prints the split() list

print(type(a11))            #print a check to make sure a11 is a list


y=1
linksVAR=[]
for string in a11:          #loop that will filter every list item that has "http"
    if 'http' in string:
        linksVAR.append(string)
        print(linksVAR)
        print(string)        #prints the item with "http"
        print("Link number:", y)  #Prints an couter of processed urls
        textfinal = open('url-list.txt', 'a')  #appends links to an .txt file on script's root
        textfinal.write(string + '\n')
        textfinal.close()
        y=y+1                #sum to the couter



dirpath = os.getcwd()       #find script's root

mypath = dirpath + '\wgetfiles' #directory to save files
if not os.path.isdir(mypath):       #creates the directory/paste if it doesnt exist yet
    os.makedirs(mypath)


print(linksVAR)
for i in range(0, len(linksVAR)):       #loop that downloads every url in a 'clean file'
    linkbaixar= linksVAR[i]     #reads list itens
    print('There are ', len(linksVAR), ' items to download.') #prints list length (number of itens to download)
    print('__________downloading item nº', i+1, ':', linksVAR[i]) #prints current item wich is being downloaded
    wget.download(linkbaixar, out=mypath)           #wget's the item/url

print("Finished downloading! This message will stay on scree for 1 minute")
time.sleep(60)
