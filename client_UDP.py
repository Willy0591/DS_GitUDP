# -*- coding: utf-8 -*-

import socket#Importé la biblio socket
UDP_IP= "192.168.0.202" #Adresse IP du serveur 
UDPport= 5005 #Port utilisé pour la communication
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.settimeout(1.0)
sock.sendto("cinema",(UDP_IP,UDPport))#Envoi de la trame  

trameReponse, addr = sock.recvfrom(1024)#Récuperation de la trame

print "Réception de la trame de réponse", trameReponse.encode("hex")#Affichage de la trame

code1=int(ord(trameReponse[0])<<24)
code2=code1+(ord(trameReponse[1])<<16)
code3=code2+(ord(trameReponse[2])<<8)
code4=code3+(ord(trameReponce[3])

code = ord()#transformation de la trame en code 

print code #Affichage du code 

