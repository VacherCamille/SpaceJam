from "class\personnage" import *

class Monstre:

    def __init__(self):
        # # Sprites du monstre
        # self.droite = pygame.image.load(droite).convert_alpha()
        # self.gauche = pygame.image.load(gauche).convert_alpha()
        # self.haut = pygame.image.load(haut).convert_alpha()
        # self.bas = pygame.image.load(bas).convert_alpha()
        self.pv = 100
        self.speed = 10
        self.degat = 1  # nombre de point qu'enlève le monstre au score du joueur
        self.distance = 10
        self.x = 0
        self.y = 0
        # self.direction = self.droite

    def attaque(self, perso):
        perso.perdPoints(self.degat)
        perso.reculer(self.distance)

    def deplacement(self, d):
        if d == gauche :
            self.x = self.x-1

        else if d == droite :
            self.x = self.x+1

        else if d == haut :
            self.y = self.y+1

        else
            self.y = self.y-1





class Pieuvre(Monstre):

    def __init__(self):
        Monstre.__init__(self)


class Tireur(Monstre):

    def __init__(self):
        Monstre.__init__(self)


class Coureur(Monstre):

    def __init__(self):
        Monstre.__init__(self)