import pygame
from pygame import *
from math import *

class Vaisseau:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.cobalt = 0

    def depotItem(self, nomPiece):
        self.items.pop(nomPiece)

    def depotCobalt(self, nbCobalt):
        self.cobalt += nbCobalt


class Joueur(object):
    def __init__(self, x, y, width, height, vel, map, vaisseau):
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
        self.vitessex =0
        self.vitessey =0
        # self.arme = Arme()
        self.map = map
        self.points = 0
        self.hitbox = (self.posx -15, self.posy, 30, 75)
        self.perso = pygame.image.load("perso.png")
        self.unePiece = None  # il ne peut transporter qu'une pièce
        self.cobalt = 0 # est une quantité donc un nombre
        self.vaisseau = vaisseau

    def draw(self, fenetre):

        fenetre.blit(self.perso, (self.posx-15, self.posy))
        self.hitbox = (self.posx, self.posy, 30, 75)
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

        elif dir == "up-right":
            self.posy += 10
            self.posx -= 10

        elif dir == "up-left":
            self.posy += 10
            self.posx += 10

        elif dir == "down-left":
            self.posy -= 10
            self.posx += 10

        elif dir == "down-right":
            self.posy -= 10
            self.posx -= 10

    def depot(self):
        if self.map == 0:
            if self.unePiece != None:
                self.vaisseau.depotItem(self.unePiece)
            if self.cobalt > 0:
                self.vaisseau.depotCobalt(self.cobalt)

    def colision (self):
        varx = self.posx//20
        vary = self.posy//20
        varx2 = ceil((self.posx+self.width)/20)
        vary2 = ceil((self.posy + self.height) / 20)
        coli = False

        if varx2>(len(self.map.grille[0])-1):
            varx2 = (len(self.map.grille[0])-1)
        if vary2>(len(self.map.grille)-1):
            vary2 = (len(self.map.grille)-1)

        for i in range(vary,vary2) :
            for j in range (varx, varx2):
                if self.map.grille[i][j] == 1 :
                    coli = True

        #print (coli)
        return coli

    def mouvement_horizontal(self, vel) :
        if self.vitessex != 0 :
            vel = vel//2
        if not(self.colision()):
            self.posx+=vel


    def mouvement_vertical(self, vel):
        #print("mouv")
        if self.vitessey != 0 :
            vel = vel//2
        if not(self.colision()):
            self.posy+=vel


    def applique_mouvements(self):
        self.posx += self.vitessex
        self.posy += self.vitessey

        if self.vitessex>0 :
            self.vitessex -= 1
        elif self.vitessex<0:
            self.vitessex += 1
        if self.vitessey>0 :
            self.vitessey -= 1
        elif self.vitessey<0:
            self.vitessey += 1


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


    def colision (self, grille):
        varx = self.posx//20
        vary = self.posy//20

        if varx>(len(grille[0])-1):
            varx = (len(grille[0])-1)
        if vary>(len(grille)-1):
            vary = (len(grille)-1)

        if grille[vary][varx] == 1 :
            return True
        else :
            return False


class Monstre(object):
    def __init__(self, map):
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
        self.skin = pygame.image.load("perso.png")
        self.map = map


    def draw(self, fenetre):
        fenetre.blit(self.skin, (self.x, self.y))
        self.hitbox = (self.x, self.y, 50, 75)
        pygame.draw.rect(fenetre, (255, 0, 0), self.hitbox, 2)

    #def attack(self):


class Map(object):
    def __init__(self, num, bg, asteroides, piece, ressource):
        self.num = num
        self.bordure = pygame.image.load(bg)
        self.fond = pygame.image.load("images/fond.png")
        self.asteroides = asteroides
        self.grille = 38 * [0]
        for i in range(len(self.grille)):
            self.grille[i] = 51 * [0]
        self.init_grille()
        self.pieces = piece
        self.ressources = ressource

    def draw(self, fenetre, bordure):
        fenetre.blit(self.fond, (0, 0))
        fenetre.blit(pygame.transform.scale(bordure,(1024,768)), (0,0))
        for aster in self.asteroides :
            aster.draw(fenetre)

        for piece in self.pieces:
            piece.draw(fenetre)

        for coba in self.ressources:
            coba.draw(fenetre)

    def init_grille(self):
        for aster in self.asteroides :
            varx = (aster.posx//20)
            vary = (aster.posy//20)
            for i in range(len(aster.grille)) :
                for j in range(len(aster.grille[0])):
                    self.grille[vary+i][varx+j] = aster.grille[i][j]
        print (self.grille)


class Asteroide ():
    def __init__(self, posx, posy, type):
        self.posx = posx
        self.posy = posy
        self.grille = 5 * [0]
        for i in range(len(self.grille)):
            self.grille[i] = 5 * [0]
        self.build_asteroide(type)
        self.type = type

    def draw(self, fenetre):
        if self.type == 1:
            fenetre.blit(pygame.image.load("images/type1.png"),(self.posx,self.posy))
        elif self.type == 2:
            fenetre.blit(pygame.image.load("images/type2.png"), (self.posx, self.posy))
        elif self.type == 3:
            fenetre.blit(pygame.image.load("images/type3.png"), (self.posx, self.posy))
        else:
            fenetre.blit(pygame.image.load("images/type4.png"), (self.posx, self.posy))

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

        elif type ==2 :
            self.grille[0][0] = 1
            self.grille[0][1] = 1
            self.grille[1][1] = 1
            self.grille[1][2] = 1
            self.grille[1][3] = 1
            self.grille[2][1] = 1
            self.grille[2][2] = 1
            self.grille[3][1] = 1

        elif type == 3 :
            self.grille[0][1] = 1
            self.grille[1][0] = 1
            self.grille[1][1] = 1
            self.grille[1][2] = 1
            self.grille[1][3] = 1

        elif type == 4 :
            self.grille[0][0] = 1
            self.grille[1][0] = 1
            self.grille[1][1] = 1
            self.grille[1][2] = 1
            self.grille[2][1] = 1
            self.grille[2][2] = 1

class Object:
    def __init__(self, nom, x, y, point):
        self.posx = x
        self.posy = y
        self.points = point
        self.nom = nom
        self.image = ''

    def draw(self, fenetre):
        fenetre.blit(pygame.image.load(self.image), (self.posx, self.posy))

class Ressource(Object):
    def __init__(self, x, y, quantite):
        super().__init__("cobalt", x, y, (quantite*1))
        self.quantite = quantite
        self.image = "images/cobalt.jpg"


class Piece(Object):
    def __init__(self, nom, x, y, point):
        super().__init__(nom, x, y, point)
        self.image = "images/boulon.jpg"
