import pygame
from pygame import *


class Joueur(object):
    def __init__(self, x, y, width, height, vel, map):
        # # Sprites du personnage
        # self.droite = pygame.image.load(droite).convert_alpha()
        # self.gauche = pygame.image.load(gauche).convert_alpha()
        # self.haut = pygame.image.load(haut).convert_alpha()
        # self.bas = pygame.image.load(bas).convert_alpha()
        self.posx = x
        self.posy = y
        self.width = width
        self.height = height
        self.vel = vel
        # self.arme = Arme()
        self.map = map
        self.points = 0
        self.hitbox = (self.posx, self.posy, 50, 75)
        self.perso = pygame.image.load("perso.png")

    def draw(self, fenetre):

        fenetre.blit(self.perso, (self.posx, self.posy))
        self.hitbox = (self.posx, self.posy, 50, 75)
        pygame.draw.rect(fenetre, (255, 0, 0), self.hitbox, 2)

    def recul(self, dir):
        if dir == "right":
            self.posx -= 10

        elif dir == "down":
            self.posy -= 10

        elif dir == "left":
            self.posx += 10

        elif dir == "up":
            self.posy += 10


class Projectil(object):
    def __init__(self, x, y, radius, color, vel, dir):
        self.posx = x
        self.posy = y
        self.vel = vel
        self.radius = radius
        self.color = color
        self.dir = dir

    def draw(self, fenetre):
        pygame.draw.circle(fenetre, self.color, (self.posx, self.posy), self.radius)


class Monstreb:
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
        self.hitbox = (self.posx, self.posy, 50, 75)

    def draw(self, fenetre):
        fenetre.blit(perso, (self.x, self.y))
        self.hitbox = (self.x, self.y, 50, 75)
        pygame.draw.rect(fenetre, (255, 0, 0), self.hitbox, 2)


class Map(object):
    def __init__(self, num, bg):
        self.num = num
        self.fond = pygame.image.load(bg)
        self.asteroides = []

    def draw(self, fenetre):
        fenetre.blit(self.fond, (0, 0))
        for aster in asteroides :
            aster.draw()



class Asteroide ():
    def __init__(self, posx, posy, type):
        self.posx = posx
        self.posy = posy

        self.grille = 5 * [0]
        for i in range(len(self.grille)):
            self.grille[i] = 5 * [0]
        self.build_asteroide(type)

    def draw(self):
        pass

    def build_asteroide(self, type):
        if type==1 :
            self.grille[0][2] = 1
            self.grille[1][0] = 1
            self.grille[1][1] = 1
            self.grille[1][2] = 1
            self.grille[2][1] = 1
            self.grille[2][2] = 1
            self.grille[2][3] = 1
            self.grille[3][2] = 1
            self.grille[3][2] = 1
            self.grille[4][2] = 1

            print(self.grille)

        elif type ==2 :
            self.grille[0][0] = 1
            self.grille[0][1] = 1
            self.grille[1][1] = 1
            self.grille[1][2] = 1
            self.grille[1][3] = 1
            self.grille[2][1] = 1
            self.grille[2][2] = 1
            self.grille[3][1] = 1

            print(self.grille)

        elif type == 3 :
            self.grille[0][1] = 1
            self.grille[1][0] = 1
            self.grille[1][1] = 1
            self.grille[1][2] = 1
            self.grille[1][3] = 1

            print(self.grille)

        elif type == 4 :
            self.grille[0][0] = 1
            self.grille[1][0] = 1
            self.grille[1][1] = 1
            self.grille[1][2] = 1
            self.grille[2][1] = 1
            self.grille[2][2] = 1
