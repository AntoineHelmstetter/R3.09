import sys
import time
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout,QPushButton, QLabel,QLineEdit,QMainWindow,QTimeEdit
from PyQt5.QtCore import QCoreApplication
import socket



class Interface (QMainWindow):
    def __init__(self):
        self.compteur = 0
        self.string_compteur =str(self.compteur)
        self.arret_thread =  False
        super().__init__()
        #Création application 
        root = QWidget()
        self.setCentralWidget(root)
        self.setWindowTitle("Chronomètre")

        #Création du Layout
        grid = QGridLayout()
        root.setLayout(grid)

        #Création des composants
        btn_con = QPushButton("Connexion")
        btn_quitter = QPushButton("Quitter")
        btn_start = QPushButton("Start")
        btn_reset = QPushButton("Reset")
        btn_stop = QPushButton("Stop")
        titre_compteur = QLabel("Compteur :")
        ligne_compteur = QLineEdit(self.string_compteur)

        #Fixation composants sur l'interface

        grid.addWidget(titre_compteur,0,0)
        grid.addWidget(ligne_compteur,1,0)
        grid.addWidget(btn_start,2,1)
        grid.addWidget(btn_reset,3,0)
        grid.addWidget(btn_stop,3,1)
        grid.addWidget(btn_con,4,0)
        grid.addWidget(btn_quitter,4,1)

        #Fonctions utilisées
        btn_quitter.clicked.connect(self.__quitter)
        btn_start.clicked.connect(self.start)
        btn_reset.clicked.connect(self.__reset)
        btn_stop.clicked.connect(self.__stop)
        btn_con.clicked.connect(self.__connect)

        #Création des fonctions
    def start(self):
        t1= threading.Thread(target=self.__start)
        t1.start()

    def __start(self):
        self.compteur=self.compteur+1
        self.string_compteur=self.compteur
        while self.arret_thread == False:
           self.compteur=self.compteur+1
        
            
    def __quitter(self):
        self.__stop()
        QCoreApplication.exit(0)

    def __reset(self):   
        self.compteur = 0

    def __stop(self):
        self.arret_thread = True

    def __connect(self):
        host = "localhost"
        port = 10000
        client_socket = socket.socket()
        client_socket.connect((host,port))

        client_socket.send("cliquer".encode())
 




if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Interface()
    window.show()
    
    app.exec()
    