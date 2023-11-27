from random import randrange
from abc import ABC, abstractmethod
import numpy as np

#from Carte1 import Creation_carte, Carte
#from Partie1 import Partie

class Joueur:
    def __init__(self, nom):
        self.nom          = nom   # nom du joueur
        self.nb_carte     = []    # cartes du joueur 
        self.actif        = True  # booléen indiquant si le joueur peut joueur ou pas  
        self.termine      = True  # booléen indiquant si le joueur a terminé ses cartes ou pas
        self.carte_bloque = []    # on stocke les cartes outils brisées qui ont bloqué le joueur 
        self.role         = None  # role du joueur     

    def affiche(self):
        "on affiche les cartes de chaque joueur"
        n = len(self.nb_carte[0][1])
        p = int(n / 3)
        a = 0

        for j in range(0, n, p + 1):
            a += 1
            for i in range(len(self.nb_carte)):

                if (a == 2):

                    print(str(i) + ": ", end="")
                    print(self.nb_carte[i][1][j:j + p], ",", end=" ")
                else:
                    print("  ", self.nb_carte[i][1][j:j + p], " ", end=" ")

                if (i == len(self.nb_carte) - 1 and a == 2):
                    print(str(i + 1), ":", "Jeter une carte", end="")
            print("")
        

    def piocher(self,carte): 
        "le pioche une carte"
        self.nb_carte.append(carte.tirer_carte())

    def __str__(self):
        s = ''
        s += self.nom
        s += '\n'
        return s