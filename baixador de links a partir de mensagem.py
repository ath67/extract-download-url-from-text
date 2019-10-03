import time
try:
   import wget
   print("Modulo wget encontrado!")
except ImportError:
   print ("Modulo wget não foi encontrado, tente instala-lo antes de executar o script. Pesquise por 'pip intall' na internet. Esse aviso ficará na tela por 1:30 minuto")
   time.sleep(90)

import wget, os

a= 's'
arquivo = input("Digite o nome do arquivo com extensão e que esteja no root desse script")
a = open(arquivo, 'r') #leitura do arquivo com o texto original
text = a.read()
a.close()
print(text)                 #printa o texto original
a1=text.replace("\n", " ")  #coloca tudo em uma só linha (apaga os \n)
a1=a1.replace("http", " http")  #cria um espaço entre qualquer frase que tenha "XXX:http" para o split() considerar o http uma palavra separada
a11=a1.split()              #cria uma lista em q cada palavra do texto é um item
print(a1)                   #printa o texto "tratado" para o split
print("splits=", str(a11))  #printa a lista

print(type(a11))            #printa uma checagem para saber se a11 é lista


y=1
linksVAR=[]
for string in a11:          #loop que separa cada item da lista que contenha "http"
    if 'http' in string:
        linksVAR.append(string)
        print(linksVAR)
        print(string)        #printa  o item com http
        print("Link numero:", y)  #Printa uma contagem de links salvos
        textfinal = open('links-tratados.txt', 'a')  #cria/dá append um arquivo para salvar os links
        textfinal.write(string + '\n')
        textfinal.close()
        y=y+1                #soma à contagem



dirpath = os.getcwd()       #descobrir o diretorio atual

mypath = dirpath + '\wgetfiles' #diretorio a ser criado/arquivos salvos
if not os.path.isdir(mypath):       #criação do diretorio caso n exista
    os.makedirs(mypath)


print(linksVAR)
for i in range(0, len(linksVAR)):       #loop para baixar cada link de um arquivo
    linkbaixar= linksVAR[i]     #ler itens da lista e igualar a uma variavel
    print('São ', len(linksVAR), ' itens para baixar.') #printa nº de itens
    print('__________baixando item nº', i+1, ':', linksVAR[i]) #printa item atual baixando
    wget.download(linkbaixar, out=mypath)           #wget no link

print("Download terminado! Essa mensagem ficará na tela por 1 minuto")
time.sleep(60)
