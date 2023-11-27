# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 20:28:47 2023

@author: YOUNES
"""

from random import randrange
from abc import ABC, abstractmethod
import numpy as np

from Carte1 import Creation_carte, Carte
from Joueur1 import Joueur
from Partie1 import Partie

print("+---------------------------------------+\n"
          "| Bienvenue dans le jeu des sabotteurs |\n"
          "+---------------------------------------+\n") 

print("Entrer le nombre de joueurs : ")
nbr_j = int(input())
liste_joueurs = []
joueur = []
for i in range(nbr_j):
    print("Entrer le nom du joueur {}".format(i + 1))
    nom = str(input())
    liste_joueurs.append(nom)
  
if nbr_j >= 3 and nbr_j <= 5:  
  nbr_cartes = 6  # le nombre de cartes à distribuer selon le nombre de joueurs
elif nbr_j >= 6 and nbr_j <= 7:
  nbr_cartes = 5 
elif nbr_j >= 8 and nbr_j <= 10:
  nbr_cartes = 4
    
for manche in range(2):

    for i in range(nbr_j):
        joueur.append(Joueur(liste_joueurs[i]))

    carte = Creation_carte.creer_carte()
    #print(carte)
    plateau = [[]]
    nom_carte = [[]]
    chemins = [[]]

    partie1 = Partie(joueur, plateau, nom_carte, chemins)
    partie1.init_plateau()
    partie1.distribuer_roles(nbr_j)
    partie1.distribuer_cartes(carte, nbr_cartes, nbr_j)

    for i in range(nbr_j):
        print("le role de {} est : {}".format(joueur[i].nom, joueur[i].role))

    print("******* La partie commence ********")
    print("******* manche {} ********".format(manche + 1))
    print("    ")
    test = True
    while test:
        "on lance la partie"
        winer, j_t, ind = partie1.jouer(carte)
        "on s'arrête quand les joueurs n'ont plus de cartes ou bien quand on a trouvé l'or"
        if j_t == nbr_j or ind == 1:
            test = False  # 3 est le nombre de joueur
    "si ind=1 ça veut dire que les miners ont trouvé l'or"
    if ind == 1:

        print("You found the gold, the miners win")

    else:
        print("The saboteurs win")
    joueur.clear()