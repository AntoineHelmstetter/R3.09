from threading import Thread
import socket
import os
#pip install psutil
#import psutil
import subprocess

def Send(client,recep):
    while True:
        msg = input()
        msg = rep.encode("utf-8")
        client.send(msg)
        
def Reception(client):
    while True:
        requete_client = client.recv(500)
        requete_client = requete_client.decode('utf-8')
        print(requete_client)
        if requete_client=="bye":
            client.close()
        elif requete_client =="exit":
            client.close()
            socket.close()
        

Host = "localhost"
Port = 6390

#Création du socket
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket.bind((Host,Port))
socket.listen(1)

#Le script s'arrête jusqu'a une connection
client, ip = socket.accept()
print("Le client d'ip",ip,"s'est connecté")

envoi = Thread(target=Send,args=[client])
recep = Thread(target=Reception,args=[client])

envoi.start()
recep.start()

recep.join()

client.close()
socket.close()

