# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 20:28:46 2023

@author: YOUNES
"""
from random import randrange
from abc import ABC, abstractmethod
import numpy as np
 
class Partie:
    def __init__(self, joueur, plateau, nom_carte, chemins):

        self.tour            = 1
        self.joueur          = joueur        # joueur est un objet de type Joueur deja crée
        self.joueurs_termine = 0             # nombre de joueurs qui ont terminé leurs cartes
        self.c               = ["lrud0"]       
        self.plateau         = plateau        # plateau contenant les cartes jouées 
        self.nom_carte       = nom_carte      # même construction que le plateau mais avec les noms des cartes
        self.chemins         = [[(2, 0, 0)]]  # cette matrice contient tous les chemins qui méne de la carte de depart
                                              # on stocke d'abord la carte de depart
    def distribuer_roles(self, nbr_j):
        
        " on distribue les roles selon le nombre de joueurs"
        if nbr_j < 3: print("Le jeu se joue à au moins 3 joueurs !")

        if nbr_j == 3:  # si le nombre de joueur est de 3
            roles = ['saboteur', 'chercheur', 'chercheur', 'chercheur']
            for i in range(nbr_j):
                self.joueur[i].role = roles.pop(randrange(0, len(roles)))
        if nbr_j == 4:  # si le nombre de joueurs est de 4
            roles = [
                'saboteur', 'chercheur', 'chercheur', 'chercheur', "chercheur"
            ]
            for i in range(nbr_j):
                self.joueur[i].role = roles.pop(randrange(0, len(roles)))
        if nbr_j == 5:  # si le nombre de joueurs est de 5
            roles = [
                'saboteur', 'saboteur', 'chercheur', 'chercheur', 'chercheur',
                "chercheur"
            ]
            for i in range(nbr_j):
                self.joueur[i].role = roles.pop(randrange(0, len(roles)))

        if nbr_j == 6:  # si le nombre de joueurs est de 6
            roles = [
                'saboteur', 'saboteur', 'chercheur', 'chercheur', 'chercheur',
                'chercheur', "chercheur"
            ]
            for i in range(nbr_j):
                self.joueur[i].role = roles.pop(randrange(0, len(roles)))
        if nbr_j == 7:  # si le nombre de joueurs est de 7
            roles = [
                'saboteur', 'saboteur', 'saboteur', 'chercheur', 'chercheur',
                'chercheur', 'chercheur', "chercheur"
            ]
            for i in range(nbr_j):
                self.joueur[i].role = roles.pop(randrange(0, len(roles)))
        if nbr_j == 8:  # si le nombre de joueurs est de 4
            roles = [
                'saboteur', 'saboteur', 'saboteur', 'chercheur', 'chercheur',
                'chercheur', 'chercheur', "chercheur",'chercheur'
            ]
            for i in range(nbr_j):
                self.joueur[i].role = roles.pop(randrange(0, len(roles)))
        if nbr_j == 9:  # si le nombre de joueurs est de 4
            roles = [
                'saboteur', 'saboteur', 'saboteur', 'chercheur', 'chercheur',
                'chercheur', 'chercheur', "chercheur",'chercheur','chercheur'
            ]
            for i in range(nbr_j):
                self.joueur[i].role = roles.pop(randrange(0, len(roles)))
        if nbr_j == 10:  # si le nombre de joueurs est de 4
            roles = [
                'saboteur','saboteur', 'saboteur', 'saboteur', 'chercheur', 'chercheur',
                'chercheur', 'chercheur', "chercheur",'chercheur','chercheur'
            ]
            for i in range(nbr_j):
                self.joueur[i].role = roles.pop(randrange(0, len(roles)))
        "completer avec la méme procedure pour nbr_j = 5 , 6 ...ect"

    def distribuer_cartes(self, carte, nbr_cartes, nbr_j):
        "on distribue les cartes pour chaque joueur"
        for j in range(nbr_j):
            for i in range(nbr_cartes):  #nbr_cartes est le nombre de cartes distribuées par joueur
                self.joueur[j].nb_carte.append(carte.ajout_carte())

    def controle_saisie(self, a, i):  
        "cette methode controle la saisie de l'utilisateur"
        "a est l'indice de la carte à jouer et i est l'indice du joueur "
        while a >= len(self.joueur[i].nb_carte):
            print("saisie erronée !")
            print("jouer une carte ")
            a = int(input())
            self.joueur[i].affiche()

        return a

    def controle_cord(self, c, x, y):
        "on vérifie si les coordonnées de la carte respectent bien la taille du plateau"
        if x < -1 or x > len(self.nom_carte): return False

        if x != -1:
            if y < -1 or y > len(self.nom_carte[x]): return False

        if x == -1 or y == -1:
            "on vérifie la connexion des cartes entre elles "
            "particuliérment quand x=-1 ou y=-1 car on sait d'avance ce qu'on doit tester "
            if x == -1:
                if 'u' in self.nom_carte[0][y] and 'd' in c:
                    return True
                else:
                    return False
            if y == -1:
                if 'l' in self.nom_carte[x][0] and 'r' in c:
                    return True
                else:
                    return False
        test = False
        "on vérifie que la case à jouer ne contient pas déja une carte"
        
        if self.nom_carte[x][y] == 'vide' or self.nom_carte[x][y] == "eboulement":
            sx = [x - 1, x + 1]
            sy = [y - 1, y + 1]

            test2 = False
            nl = len(self.nom_carte)
            nc = len(self.nom_carte[x])
            "la on vérifie qu'autour de la case à jouer il y'a bien au moins une carte adjacente"
            for s in sx:  # on vérifie que les cases adjacentes ne sont pas toutes vides
                if s < nl-1 and s >= 0 and len(self.nom_carte[x]) != 0:
                    if not '-' in self.nom_carte[s][y] and self.nom_carte[s][y] != 'vide':
                        test2 = True

            for s in sy:
                if s < nc and s >= 0:
                    if not '-' in self.nom_carte[x][s] and self.nom_carte[x][s] != 'vide':
                        test2 = True

            if test2 == True:
                test = True
                "dans le cas où il y a au moins une carte chemin"
                "adjacente qui soit pas un cul-de-sac on doit verifier qu'il y a connexion entre"
                "la carte à jouer et les cartes voisines"

                if sx[0] < nl-1 and sx[0] >= 0 and len(self.nom_carte[x]) != 0:
                    if self.nom_carte[sx[0]][y] != "vide" and self.nom_carte[
                            sx[0]][y] != 'eboulement' and self.nom_carte[sx[0]][
                                y] != "or" and not "pierre" in self.nom_carte[
                                    sx[0]][y]:

                        if ("d" in self.nom_carte[sx[0]][y] and not 'u' in c) or ('u' in c
                                  and not "d" in self.nom_carte[sx[0]][y]):
                            test = False
                    # else :
                if sx[1] < nl-1 and sx[1] >= 0 and len(self.nom_carte[x]) != 0:
                    if self.nom_carte[sx[1]][y] != "vide" and self.nom_carte[ sx[1]][y] != 'eboulement' and self.nom_carte[sx[1]][y] != "or" and not "pierre" in self.nom_carte[sx[1]][y]:
                        if ("u" in self.nom_carte[sx[1]][y] and not 'd' in c ) or ('d' in c and not "u" in self.nom_carte[sx[1]][y]):
                            test = False
                if sy[0] < nc and sy[0] >= 0:
                    if self.nom_carte[x][sy[0]] != "vide" and self.nom_carte[x][sy[0]] != 'eboulement' and self.nom_carte[x][sy[0]] != "or" and not "pierre" in self.nom_carte[x][sy[0]]:
                        if ('r' in self.nom_carte[x][sy[0]] and not 'l' in c) or ('l' in c and not "r" in self.nom_carte[x][sy[0]]):
                             test = False
                if sy[1] < nc and sy[1] >= 0:
                    if self.nom_carte[x][sy[1]] != "vide" and self.nom_carte[x][sy[1]] != 'eboulement' and self.nom_carte[x][sy[1]] != "or" and not "pierre" in self.nom_carte[x][sy[1]]:
                        if ('l' in self.nom_carte[x][sy[1]] and not 'r' in c ) or ('r' in c and not "l" in self.nom_carte[x][sy[1]]):
                            test = False
            else:
                test = False

        return test

    def detruire_carte(self, x, y):
        test = False
        nl = len(self.nom_carte)
        nc = len(self.nom_carte[x])
        " on vérifie d'abord les coordonnees de la carte à détruire et l'existence de cette carte"
        " et puis on vérifie aussi si cette carte ne s'agit pas d'une carte arrivé ou bien d'une carte de départ"
        print(nl, nc)
        if x >= 0 and x < nl and y >= 0 and y < nc:
            if self.nom_carte[x][y] != "vide" and self.nom_carte[x][
                    y] != "eboulement":
                if self.nom_carte[x][y] != "lrud0" and self.nom_carte[x][
                        y] != "or" and self.nom_carte[x][y] != "pierre":
                    test = True

        return test

    def test_chemin(self, n, x, y, z, x1, y1):
        indx = [-1]
        test = False
        
        for i in range(n):

            if (x1, y1, z) in self.chemins[i]:
                "on vérifie qu'il y a continuité des coordonnées"
                if self.chemins[i][-1] == (x1, y1, z):
                    "on vérifie s'il y a continuité avec les coordonnées de la derniére carte"
                     
                    test2 = True
                    for s in self.chemins[i]: 
                        "s'il y a une carte eboulement sur le chemin alors on peut pas ajouter "
                        "les coordonnées de la carte au chemin"
                        if s[2] == -1: test2 = False
                    if test2 == True:
                        "si le chemin est continu alors on y'a moyen d'ajouter les coordonnées de la carte à jouer au chemin"
                        self.chemins[i].append((x, y, z))
                        test = True

                else:

                    j = self.chemins[i].index((x1, y1, z))
                    
                    if indx[-1] != j:
                        indx.append(j)

                        test2 = True
                        "s'il y a une carte eboulement sur le chemin alors on peut pas ajouter "
                        "les coordonnées de la carte au chemin"
                        for s in self.chemins[i][0:j + 1]:
                            if s[2] == -1: test2 = False
                        "s'il y a continuité avec les coordonnées d'une carte d'un chemin "
                        " alors on peut créer un autre chemin"
                        if test2 == True:
                            test = True
                            nc = self.chemins[i][0:j + 1]
                            nc.append((x, y, z))

                            # on crée un nouveau chemin 
                            self.chemins.append(nc)

        return test

    def creer_chemin(self, x, y, z): # x et y sont les coordonnées de la case 
                                     # z est un indicateur de la carte -1 si éboulement 0 sinon
        n    = len(self.chemins)
        test = False # booléen indiquant si la case à jouer est possible ou pas 
                     # pour cela on vérifie si le chemin est continu ou pas  
        for i in range(len(self.chemins)):
            if z == -1: # si on joue une carte éboulement
                if (x, y, 0) in self.chemins[i]:
                    j = self.chemins[i].index((x, y, 0))
                    self.chemins[i][j] = (x, y, z) # on redéfinit l'indicateur de la carte 
                                                    # en le mettant à -1
                    return True

            if (x, y, -1) in self.chemins[i]:
                j = self.chemins[i].index((x, y, -1))
                self.chemins[i][j] = (x, y, z)
                return True

        if x == -1:
            x1, y1 = x + 1, y 
            test   = self.test_chemin(n, x, y, z, x1, y1)
            if test == True:
                for i in range(len(self.chemins)):
                    for j in range(len(self.chemins[i])):

                        x1 = self.chemins[i][j][0]
                        y1 = self.chemins[i][j][1]
                        z1 = self.chemins[i][j][2]
                        "on décale toutes les cases de 1 sur x pour recentrer" 
                        "toujours les cordonnées à 0"
                        self.chemins[i][j] = (x1 + 1, y1, z1)
        if y == -1:
            y1, x1 = y + 1, x

            test = self.test_chemin(n, x, y, z, x1, y1)

            if test == True:
                for i in range(len(self.chemins)):
                    for j in range(len(self.chemins[i])):

                        x1 = self.chemins[i][j][0]
                        y1 = self.chemins[i][j][1]
                        z1 = self.chemins[i][j][2]
                        "on décale toutes les cases de 1 sur y pour recentrer" 
                        "toujours les cordonnées à 0"
                        self.chemins[i][j] = (x1, y1 + 1, z1)

        if x != -1 and y != -1:

            x1 = [x - 1, x + 1]
            y1 = [y - 1, y + 1]

            t = []
            for s in x1:
                t.append(self.test_chemin(n, x, y, z, s, y))
            for s in y1:
                t.append(self.test_chemin(n, x, y, z, x, s))

            if True in t: test = True
            else: test = False

        return test

    def get_carte_arrivee(self, x, y):
        pierre = ["(  |  ) (--N--) (  |  )"]
        gold = ["(  |  ) (--G--) (  |  )", "(  |  ) (-2G--) (  |  )"]
        if self.nom_carte[x][y] == 'or':
            return gold[randrange(len(gold))]
        if self.nom_carte[x][y] == 'pierre':
            return pierre[randrange(len(pierre))]

    def test_arrive(self, c, x, y):
        sx = [x - 1, x + 1]
        sy = [y - 1, y + 1]

        test = False
        x1, y1 = x, y
        ind = -1
        nl = len(self.nom_carte)
        nc = len(self.nom_carte[x])
        "on vérifie que la carte posée méne bien à une carte d'arrivé "
        if sx[0] < nl-1 and sx[0] >= 0 and len(self.nom_carte[x]) != 0:

            if self.nom_carte[sx[0]][y] == 'or' and not '-' in c and 'u' in c:
                test, ind = True, 1
                x1, y1 = sx[0], y
                self.plateau[x1][y1] = self.get_carte_arrivee(x1, y1)
                "dés qu'on trouve une carte or on s'arréte"
                return test, x1, y1, ind
            if self.nom_carte[
                    sx[0]][y] == 'pierre' and not '-' in c and 'u' in c:
                test, ind = True, 0
                x1, y1 = sx[0], y
                "si on arrive à une carte pierre on la tourne"
                self.plateau[x1][y1] = self.get_carte_arrivee(x1, y1)
        if sx[1] < nl-1 and sx[1] >= 0 and len(self.nom_carte[x]) != 0:

            if self.nom_carte[sx[1]][y] == 'or' and not '-' in c and 'd' in c:
                test, ind = True, 1
                x1, y1 = sx[1], y
                self.plateau[x1][y1] = self.get_carte_arrivee(x1, y1)
                return test, x1, y1, ind
            if self.nom_carte[
                    sx[1]][y] == 'pierre' and not '-' in c and 'd' in c:
                test, ind = True, 0
                x1, y1 = sx[1], y
                self.plateau[x1][y1] = self.get_carte_arrivee(x1, y1)
        if sy[0] < nc and sy[0] >= 0 and len(self.nom_carte[x]) != 0:

            if self.nom_carte[x][sy[0]] == 'or' and not '-' in c and 'l' in c:
                test, ind = True, 1
                x1, y1 = x, sy[0]
                self.plateau[x1][y1] = self.get_carte_arrivee(x1, y1)
                return test, x1, y1, ind
            if self.nom_carte[x][
                    sy[0]] == 'pierre' and not '-' in c and 'l' in c:
                test, ind = True, 0
                x1, y1 = x, y[0]
                self.plateau[x1][y1] = self.get_carte_arrivee(x1, y1)
        if sy[1] < nc and sy[1] >= 0 and len(self.nom_carte[x]) != 0:

            if self.nom_carte[x][sy[1]] == 'or' and not '-' in c and 'r' in c:
                test, ind = True, 1
                x1, y1 = x, sy[1]
                self.plateau[x1][y1] = self.get_carte_arrivee(x1, y1)
                return test, x1, y1, ind
            if self.nom_carte[x][
                    sy[1]] == 'pierre' and not '-' in c and 'r' in c:
                test, ind = True, 0
                x1, y1 = x, sy[1]
                self.plateau[x1][y1] = self.get_carte_arrivee(x1, y1)

        return test, x1, y1, ind

    def bloque_joueur(self, idx_j, c):
        test = False
        print("quel joueur voulez-vous bloquer")
        for i in range(len(self.joueur)):
            if i != idx_j: print("{}\ {}".format(i, self.joueur[i].nom))
        j = int(input())
        "on vérifie que la carte outil brisé n'a deja étè jouée contre le même joueur"
        if not c in self.joueur[j].carte_bloque:
            self.joueur[j].actif = False # on bloque le joueur
            self.joueur[j].carte_bloque.append(c) # on stocke la carte par laquelle 
                                                  # on a bloqué le joueur 
            test = True
        else:
            print("Ce joueur est déja bloqué par cette carte")

        return test

    def debloque_joueur(self, idx_j, c):
        test = False
        print("quel joueur voulez-vous débloquer")
        for i in range(len(self.joueur)):
            print("{}\ {}".format(i, self.joueur[i].nom))
        j = int(input())
        c = c + '-' # on contruit la carte outil brisé  à partir de la carte
                    # reparer outil afin de vérifier si on peut débloquer le joueur
                    # à l'aide de cette carte

         
        if self.joueur[j].actif == False:
            
            if c in self.joueur[j].carte_bloque:
                test = True
                self.joueur[j].carte_bloque.remove(c)
                if len(self.joueur[j].carte_bloque) == 0:
                    self.joueur[j].actif = True
            else:
                test = False
                print("vous ne pouvez pas debloquer ce joueur avec cet outil")

                print("recommencer !!")
        else:
            print("ce joueur est déja actif")
        return test

    def tourne_carte_arrivee(self, m):
        s = 0

        for i in range(len(self.nom_carte)):
            for j in range(len(self.nom_carte[i])):
                if self.nom_carte[i][j] == "or" or self.nom_carte[i][j] == "pierre":
                    s += 1
                    if s == m:
                        carte = self.plateau[i][j]
                        if self.nom_carte[i][j] == "or":
                              
                            self.plateau[i][j] = self.get_carte_arrivee(i, j)
                            self.Affiche_plateau()
                            self.plateau[i][j] = carte
                        else:

                            self.plateau[i][j] = self.get_carte_arrivee(i, j)
                            self.Affiche_plateau()
                            self.plateau[i][j] = carte

                        

    # def jouer_IA (self,carte,ia) :
    #     if ia.role == 'saboteur' :

    #         for crd in range (ia.nb_carte):
    #             if crd == 'eboulement' :
    #               ind=-1   # indicateur de la carte (-1 si carte eboulement 0 sinon)
    #               test1= False
    #               case=[]
    #               for i in range(len(self.plateau)):
    #                   for j in range(len(self.plateau[0])):
    #                           test1=self.detruire_carte(i,j)
    #                           if test1==True :
    #                                case.append((i,j))
    #                   # if "or"in self.nom_carte[i]: xs=self.nom_carte[i].index("")
    #               if len(case) !=0 :
    #                   for s in case :

    def jouer(self, carte):

        for i in range(len(self.joueur)):

            indic = -1  # ça indique si on a trouvé l'or ou pas (0 si oui -1 sinon)
            if self.joueur[i].termine != False:
                crd = []
                print("c'est le tour de {} ".format(self.joueur[i].nom))
                print()
                #print(self.joueur[i].nb_carte)
                # if self.joueur[i].nom == 'ia' :
                # self.joueur_IA (carte,self.joueur[i])
                test = False
                while test == False:
                    self.Affiche_plateau()
                    print("quelle carte voulez-vous jouer")
                    self.joueur[i].affiche()
                    a = int(input())
                    if a == len(self.joueur[i].nb_carte
                                ):  # on choisit de jeter une carte
                        print("quelle carte voulez-vous jeter")
                        a = int(input())
                        a = self.controle_saisie(a, i)  # on controle la saisie
                        test = True
                        s = self.joueur[i].nb_carte.pop(a)

                        if carte.cartes_restantes() > 0:
                            self.joueur[i].piocher(carte)

                    else:
                        "on choisit de jouer une carte chemin ou bien une carte action"
                        a = self.controle_saisie(a, i)
                        crd.append(self.joueur[i].nb_carte[a]
                                   [0])  # on stocke le nom de la carte choisie

                        "si le joueur est déja bloqué, il peut joueur "
                        "seulement une carte action ou jeter une carte"
                        if crd[-1] == 'L' or crd[-1] == 'P' or crd[-1] == 'W':
                            test = self.debloque_joueur(i, crd[-1])
                            if test == True:
                                self.joueur[i].nb_carte.pop(a)
                                if carte.cartes_restantes(
                                ) > 0:  # on pioche tant qu'il reste des cartes dans la pioche
                                    self.joueur[i].piocher(carte)
                                break
                        else:
                            if crd[-1] == 'map':
                                print("quelle carte voulez-vous tourner")
                                print("taper 1 ou 2 ou 3")
                                m = int(input())
                                self.tourne_carte_arrivee(m)
                                break
                            elif crd[-1] == 'L-' or crd[-1] == 'P-' or crd[-1] == 'W-':
                                "si le joueur decide de jouer une carte outil brisé"
                                test = self.bloque_joueur(i, crd[-1])
                                if test == True:
                                    self.joueur[i].nb_carte.pop(a)
                                    if carte.cartes_restantes(
                                    ) > 0:  # on pioche tant qu'il reste des cartes dans la pioche
                                        self.joueur[i].piocher(carte)
                                    break

                            elif crd[-1] == 'L' or crd[-1] == 'P' or crd[
                                    -1] == 'W':
                                test = self.debloque_joueur(i, crd[-1])
                                if test == True:
                                    self.joueur[i].nb_carte.pop(a)
                                    if carte.cartes_restantes(
                                    ) > 0:  # on pioche tant qu'il reste des cartes dans la pioche
                                        self.joueur[i].piocher(carte)
                                    break

                            elif crd[-1] == "eboulement":
                                ind = -1  # indicateur de la carte (-1 si carte eboulement 0 sinon)
                                test1 = False
                                while test1 == False:
                                    print(
                                        "entrer les coordonnées de la carte (x,y) de la carte à détruire"
                                    )
                                    x = int(input())
                                    y = int(input())
                                    test1 = self.detruire_carte(x, y)
                                    if test1 == False:
                                        print("Saisie érronée !!!")
                                        print("")
                                        print(
                                            "Rappel : il est impossible de détruire une carte d'arrivée ou une carte de départ"
                                        )
                                        print('')
                                        print(
                                            "si vous voulez jouer une autre carte tapez 'y' sinon 'n'"
                                        )
                                        b = input()
                                        if b == 'y':
                                            "dans le cas où le joueur décide de rechoisir une autre carte"
                                            test1 = True
                                            test = False
                                            crd.remove(crd[-1])
                                        else:

                                            test1 = False
                                    else:
                                        test = True
                                        self.creer_chemin(x, y, ind)
                                        s = self.joueur[i].nb_carte.pop(
                                            a
                                        )  # on supprime la carte jouée et on la stocke dans s
                                        self.construction_plateau(
                                            x, y, s[1], s[0])
                                        self.c.append(s[0])
                                        if carte.cartes_restantes(
                                        ) > 0:  # on pioche tant qu'il reste des cartes dans la pioche
                                            self.joueur[i].piocher(carte)

                            else:
                                if self.joueur[i].actif != False:

                                    ind = 0
                                    print(
                                        "entrer les coordonnées de la carte (x,y)"
                                    )
                                    x = int(input())
                                    y = int(input())

                                    test = self.controle_cord(crd[-1], x, y)

                                    if test == True:

                                        test2 = self.creer_chemin(
                                            x, y, ind
                                        )  # on teste si le chemin est continu depuis la carte de départ

                                        if test2 == True:

                                            s = self.joueur[i].nb_carte.pop(
                                                a
                                            )  # on supprime la carte jouée et on la stocke dans c
                                            arrive, x1, y1, indic = self.test_arrive(
                                                crd[-1], x, y)

                                            if arrive == True:

                                                if indic == 1:

                                                    self.construction_plateau(
                                                        x, y, s[1], s[0])

                                                    break
                                                else:
                                                    "si la carte d'arrivée s'agit d'une carte pierre alors on marque cette carte par X"

                                                    self.nom_carte[x1][
                                                        y1] = 'Xpierre'
                                                    self.construction_plateau(
                                                        x, y, s[1], s[0])
                                                    self.c.append(s[0])
                                                    self.creer_chemin(
                                                        x1, y1, 0)
                                                    if carte.cartes_restantes(
                                                    ) > 0:  # on pioche tant qu'il reste des cartes dans la pioche
                                                        self.joueur[i].piocher(carte
                                                        )

                                            else:

                                                self.construction_plateau(
                                                    x, y, s[1], s[0])
                                                self.c.append(s[0])
                                                if carte.cartes_restantes(
                                                ) > 0:  # on pioche tant qu'il reste des cartes dans la pioche
                                                    self.joueur[i].piocher(carte)
                                        else:
                                            test = False
                                            print(
                                                "vous devez d'abord réparer la galerie avant de poursuivre ce chemin"
                                            )

                                    else:
                                        print(
                                            "Vous ne pouvez pas jouer cette case !"
                                        )
                                        print("recommencer !")
                                else:
                                    print(
                                        "vous ne pouvez pas jouer de carte chemin car vous étes bloqué"
                                    )
                                    test = False
                if len(self.joueur[i].nb_carte) == 0:
                    self.joueurs_termine += 1  # on stocke le nombre de joueurs qui n'ont plus de cartes

                    self.joueur[i].termine = False  # si le joueur n'a plus de cartes

                if indic == 1: break

        return self.joueur[i].role, self.joueurs_termine, indic

    def init_plateau(self):
        esp = ""
        c0 = "(  |  ) (--S--) (  |  )"

        for _ in range(len(c0)):
            esp += " "
        g = "(  e  ) (  n  ) (  d  )"

        indx_or = randrange(0, 3)
        s = -1
        for j in range(5):
            for i in range(6):
                self.plateau[j].insert(i, esp)
                self.nom_carte[j].insert(i, 'vide')
            if j % 2 == 0:
                s += 1
                if s == indx_or: 
                    "on insére la carte or au hasard"
                    self.plateau[j][i] = g
                    self.nom_carte[j][i] = "or"
                else:
                    self.plateau[j][i] = g
                    self.nom_carte[j][i] = "pierre"

            self.plateau.insert(j + 1, [])
            self.nom_carte.insert(j + 1, [])
        self.plateau[0].insert(0, esp)
        self.nom_carte[0].insert(0, "vide")
        self.plateau[2].insert(0, c0)
        self.nom_carte[2].insert(0, "lrud0")

        self.plateau[1].insert(0, esp)
        self.nom_carte[1].insert(0, "vide")

        self.plateau[3].insert(0, esp)
        self.nom_carte[3].insert(0, "vide")
        self.plateau[4].insert(0, esp)
        self.nom_carte[4].insert(0, "vide")

    def affiche_contour(self, nc):

        print("       ", end="")
        for i in np.arange(-1, nc + 1):
            print(" ", str(i), "   ", end="")
        print()
        print("-------" * (nc + 3))
        print("     ", "|")
        print("  ", " -1" + "|")
        print("     ", "|")

    def Affiche_plateau(self):

        nb = "                       "
        n = len(self.plateau[0][0])
        p = int(n / 3)
        s = -1
        nc = len(self.plateau[0])
        self.affiche_contour(nc)
        for i in range(len(self.plateau) - 1):
            s += 1
            for j in range(0, n, p + 1):

                cont = "      |      " + str(s) + "|       |      "
                print(cont[j:j + p], end="")
                print(nb[j:j + p], end="")

                for k in range(len(self.plateau[i])):

                    #print(cont[j:j + p],end="")
                    print(self.plateau[i][k][j:j + p], end="")

                print(' ')
        print("                   ")
        print("********************************")

    def construction_plateau(self, x, y, c, c_n):
        "contruction d'un plateau dynamique"

        if c_n == "eboulement":
            "on detruit la carte en l'echangeant par la carte éboulement "
            self.nom_carte[x][y] = c_n
            self.plateau[x][y] = c
            self.Affiche_plateau()
            return 0

        esp = ""
        for _ in range(len(c)):
            esp += " "
        if x == len(self.plateau)-2 :
            "dés qu'on s'appproche du bord du plateau on remplit la derniére ligne par des cartes vides "
            " et on rajoute une ligne vide pour que la taille du plateau reste toujours dynamique"
            n = len(self.plateau)
            
            for j in range(len(self.nom_carte[0])):
                self.plateau[n-1].insert(j, esp) 
                self.nom_carte[n-1].insert(j, "vide")
            self.plateau.insert(n, [])
            self.nom_carte.insert(n, [])
        if x >= 0 and len(self.plateau[x]) == 0:
            
            self.plateau.insert(x, [])
            self.nom_carte.insert(x, [])

        if x < 0:
            x = 0
            n = len(self.plateau[0])
            "on rajoute une ligne vide devant la ligne 0"
            self.plateau.insert(0, [])
            self.nom_carte.insert(0, [])
            for _ in range(n):
                "on remplit par des cartes vides la ligne qu'on vient d'ajouter "
                self.plateau[0].insert(y, esp)
                self.nom_carte[0].insert(y, "vide")
            "on insére la carte dans la case voulue"
            self.plateau[x][y] = c     # on insére la carte dans le plateau
            self.nom_carte[x][y] = c_n # on insére le nom de la carte 

        if y >= 0:
            
            if len(self.plateau[x]) == 0:
                "si la ligne est vide (aucune carte)"
                "alors on remplit par des cartes vides tant qu'on est pas arrivé "
                "à la case voulue et puis on insére la carte"
                s = 0

                while s < y:
                     
                    self.plateau[x].insert(s, esp)
                    self.nom_carte[x].insert(s, "vide")
                    s += 1

                self.plateau[x].insert(y, c)     # on insére la carte dans le plateau
                self.nom_carte[x].insert(y, c_n) # on insére le nom de la carte 
            else:
                if len(self.plateau[x]) > y:
                    "si la ligne n'est pas vide et que le nombre de colonnes est"
                    "supérieur à y alors on insére directement la carte dans la case voulue"
                    self.plateau[x][y] = c
                    self.nom_carte[x][y] = c_n
                else:
                    s = len(self.plateau[x])
                    "si la ligne n'est pas vide et que le nombre de colonnes est"
                    " inférieur à y alors on remplit par des carte vide jusqu'à arriver à la case voulu"
                    " et on insére à la carte"
                    while s < y:

                        self.plateau[x].insert(s, esp)
                        self.nom_carte[x].insert(s, "vide")
                        s += 1

                    self.plateau[x].insert(y, c)     # on insére la carte dans le plateau
                    self.nom_carte[x].insert(y, c_n) # on insére le nom de la carte 

        else:
            "si y est négatif"
            y = 0
            "on remplit par des carte vide jusqu'à arriver à la case voulu"
            " et puis on insére à la carte"
            for i in range(len(self.plateau)):
                self.plateau[i].insert(y, esp)
                self.nom_carte[i].insert(y, "vide")

            self.plateau[x][y] = c     # on insére la carte dans le plateau
            self.nom_carte[x][y] = c_n # on insére le nom de la carte 

        self.Affiche_plateau() # on affiche le plateau 


 
