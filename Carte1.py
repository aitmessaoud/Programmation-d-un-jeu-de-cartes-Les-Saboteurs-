# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 20:26:19 2023

@author: YOUNES
"""

from random import randrange
from abc import ABC, abstractmethod
import numpy as np

#from Joueur1 import Joueur
#from Partie1 import Partie



class Carte(ABC):
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def ajout_carte(self):
        pass

    @abstractmethod
    def cartes_restantes(self):
        pass


class Creation_carte(Carte):
    def __init__(self, liste_cartes):

        self.liste_cartes = liste_cartes

    @classmethod
    def creer_carte(cls):
        " on crée ici toutes les cartes du jeu"

        #a = "(  |  ) (--+--) (  |  )"
        #b = "( Att ) (  W  ) (     )"
        #c = "( Def ) (  W  ) (     )"
        #d = "(  |  ) (--+--) (  |  )"
        #e = "(  |  ) (--+--) (  |  )"

        "cartes positives"
        a = "(  |  ) (--+--) (  |  )"
        b = "(  |  ) (  +--) (  |  )"
        # carte UDL à rajouter c = "(  |  ) (--+  ) (  |  )"
        c = "(  |  ) (--+--) (     )"
        d = "(  |  ) (  +--) (     )"
        e = "(  |  ) (--+  ) (     )"
        f = "(  |  ) (  +  ) (  |  )"
        g = "(     ) (--+--) (     )"
        h = "(  |  ) (  +  ) (     )"
        i = "(     ) (  +--) (     )"
        j = "( Def ) (  L  ) (     )"
        k = "( Def ) (  P  ) (     )"
        l = "( Def ) (  W  ) (     )"
        p = "(  M  ) ( MAP ) (  P  )"
        q = "(  R  ) ( RoF ) (  F  )"

        "cartes negatives"
        a_ = "(  |  ) (--X--) (  |  )"
        b_ = "(  |  ) (  X--) (  |  )"
        c_ = "(  |  ) (--X  ) (  |  )"
        d_ = "(  |  ) (  X--) (     )"
        e_ = "(  |  ) (--X  ) (     )"
        f_ = "(  |  ) (  X  ) (  |  )"
        g_ = "(     ) (--X--) (     )"
        j_ = "( Att ) (  L  ) (     )"
        k_ = "( Att ) (  P  ) (     )"
        l_ = "( Att ) (  W  ) (     )"
     

        URDL = [('ludr', a)] * 5
        URDL_ = [('ludr-', a_)]
        URD = [('urd', b)] * 5
        URD_ = [('urd-', b_)]
        URL = [('url', c)] * 5
        URL_ = [('url-', c_)]
        UR = [('ur', d)] * 5
        UR_ = [('ur-', d_)]
        UL = [('ul', e)] * 4
        UL_ = [('ul-', e_)]
        UD = [('ud', f)] * 4
        UD_ = [('ud-', f_)]
        RL = [('rl', g)] * 3
        RL_ = [('rl-', g_)]
        U = [('u', h)]
        R = [('r', i)]

        L = [('L', j)] * 2
        L_ = [('L-', j_)] * 3
        P = [('P', k)] * 2
        P_ = [('P-', k_)] * 3
        W = [('W', l)] * 2
        W_ = [('W-', l_)] * 3
        MAP = [('map', p)] * 6
        ROF = [('eboulement', q)] * 3
        #eboulement à definir

        liste_cartes = URDL + URD + URL + UR + UL + UD + RL + U + R + L + P + W + MAP + ROF + URDL_ + URD_ + URL_ + UR_ + UL_ + UD_ + RL_ + L_ + P_ + W_
        #liste_cartes = [('ludr', a), ('W-', b), ('W', c), ('ludr', d),
        #('ludr', e)]

        return cls(liste_cartes)

    def affiche(self):
        for i in range(len(self.liste_cartes)):
            print(self.liste_cartes[i][1])

    def tirer_carte(self):
        "pour piocher on tire toujours la derniére carte"
        if len(self.liste_cartes) != 0:
            card = self.liste_cartes[-1]
            self.liste_cartes.remove(card)
        else:
            card = []

        return card

    def ajout_carte(self):
        "on tire une carte au hasard parmi la liste des cartes"
        if len(self.liste_cartes) != 0:
            card = self.liste_cartes.pop(randrange(0, len(self.liste_cartes)))
        else:

            card = []
        return card

    def cartes_restantes(self):  # ça renvoie le nombre de cartes restantes
        return len(self.liste_cartes)

    def __str__(self):

        s = ''
        n = len(self.liste_cartes[0][1])
        p = int(n / 3)
        for i in range(len(self.liste_cartes)):
            for j in range(0, n):
                s += str(self.liste_cartes[i][1][j])
                if (j + 1) % (p + 1) == 0: s += '\n'
            s += '\n'
            s += '\n'
        return s