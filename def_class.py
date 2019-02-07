import pygame
from pygame import *
from math import *

class Vaisseau:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.cobalt = 0

    def depotItem(self, nomPiece):
        self.items.append(nomPiece)

    def depotCobalt(self, nbCobalt):
        self.cobalt += nbCobalt


class Joueur(object):
    def __init__(self, x, y, width, height, vel, map, vaisseau, skin):
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
        self.perso = skin
        self.unePiece = None  # il ne peut transporter qu'une pièce
        self.cobalt = 0 # est une quantité donc un nombre
        self.vaisseau = vaisseau

    def draw(self, fenetre):

        fenetre.blit(self.perso, (self.posx-15, self.posy))
        self.hitbox = (self.posx, self.posy, 30, 75)
        #pygame.draw.rect(fenetre, (255, 0, 0), self.hitbox, 2)

    def recul(self, dir):
        if dir == "right":
            self.mouvement_horizontal(-8)

        elif dir == "down":
            self.mouvement_vertical(-8)

        elif dir == "left":
            self.mouvement_horizontal(8)

        elif dir == "up":
            self.mouvement_vertical(8)

        elif dir == "up-right":
            self.mouvement_vertical(6)
            self.mouvement_horizontal(-6)

        elif dir == "up-left":
            self.mouvement_vertical(6)
            self.mouvement_horizontal(6)

        elif dir == "down-left":
            self.mouvement_vertical(-6)
            self.mouvement_horizontal(6)

        elif dir == "down-right":
            self.mouvement_vertical(-6)
            self.mouvement_horizontal(-6)

    def recuperer(self, objet, numItem):
        class_split1 = str(type(objet)).split("'")[1]
        class_split = class_split1.split(".")[1]
        if class_split=="Ressource":
            print("l'objet est une ressource")
            self.cobalt = self.cobalt + objet.quantite
            self.map.item_a_ramasser.pop(numItem)
        elif class_split=="Piece":
            print("l'objet est une piece")
            if self.unePiece == None:
                self.unePiece = objet
                self.map.item_a_ramasser.pop(numItem)

    def depot(self):
        if self.map.num == 0:
            if self.unePiece != None:
                self.vaisseau.depotItem(self.unePiece)
                self.unePiece = None
            if self.cobalt > 0:
                self.vaisseau.depotCobalt(self.cobalt)
                self.cobalt = 0

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
    def __init__(self, x, y):
        # # Sprites du monstre
        # self.droite = pygame.image.load(droite).convert_alpha()
        # self.gauche = pygame.image.load(gauche).convert_alpha()
        # self.haut = pygame.image.load(haut).convert_alpha()
        # self.bas = pygame.image.load(bas).convert_alpha()
        self.pv = 1000
        self.speed = 3
        self.degat = 100  # nombre de point qu'enlève le monstre au score du joueur
        self.distance = 150
        self.x = x
        self.y = y
        self.hitbox = (self.x, self.y, 50, 75)
        self.skin = pygame.image.load("images/gros2.png")
        self.dirx ="plus"
        self.diry ="plus"
        self.skin = pygame.image.load("images/gros.png")
        self.couldown = 0
        self.timeCouldown = 0



    def draw(self, fenetre):
        fenetre.blit(self.skin, (self.x, self.y))
        self.hitbox = (self.x, self.y, 50, 75)
        #pygame.draw.rect(fenetre, (255, 0, 0), self.hitbox, 2)



class MonstreTireur(Monstre):
     def __init__(self, x, y):
         super().__init__(x, y)
         self.pv = 200
         self.speed = 2
         self.degat = 20
         self.skin = pygame.image.load("images/tireur2.png")

class MonstreCoureur(Monstre):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.pv = 500
        self.speed = 5
        self.degat = 10
        self.skin = pygame.image.load("images/coureur2.png")
        self.distance = 50

class Map(object):
    def __init__(self, num, bg, asteroides, pieces, ressources, aliens):
        self.num = num
        self.bordure = pygame.image.load(bg)
        self.fond = pygame.image.load("images/fond.png")
        self.asteroides = asteroides
        self.grille = 39 * [0]
        self.aliens = aliens

        for i in range(len(self.grille)):
            self.grille[i] = 51 * [0]
        self.init_grille()
        self.item_a_ramasser = pieces + ressources

    def draw(self, fenetre, bordure):
        fenetre.blit(self.fond, (0, 0))
        fenetre.blit(pygame.transform.scale(bordure,(1024,768)), (0,0))
        for aster in self.asteroides :
            aster.draw(fenetre)

        for item in self.item_a_ramasser:
            item.draw(fenetre)

        for alien in self.aliens :
            alien.draw(fenetre)



    def init_grille(self):
        for aster in self.asteroides :
            varx = (aster.posx//20)
            vary = (aster.posy//20)
            for i in range(len(aster.grille)) :
                for j in range(len(aster.grille[0])):
                    self.grille[vary+i][varx+j] = aster.grille[i][j]


    def init_bordures(self):
        if self.num == 1 :
            for i in range(0,len(self.grille)-1):
                for j in range (0,2):
                    self.grille[i][j] = 1
            for i in range(12,23):
                for j in range (2,9):
                    self.grille[i][j] = 1
            for i in range(6,11):
                for j in range (2,4):
                    self.grille[i][j] = 1
            for i in range(24,28):
                for j in range (2,6):
                    self.grille[i][j] = 1
        if self.num == 2:
            for i in range(0,3):
                for j in range (0,len(self.grille[0])-1):
                    self.grille[i][j] = 1
            for i in range(0,17):
                for j in range (0,2):
                    self.grille[i][j] = 1
            for i in range(17,len(self.grille)-1):
                for j in range (0,3):
                    self.grille[i][j] = 1
            for i in range(3,4):
                for j in range (6,26):
                    self.grille[i][j] = 1
            for i in range(4,7):
                for j in range (6,10):
                    self.grille[i][j] = 1
        if self.num == 3:
            for i in range(0,3):
                for j in range (0,len(self.grille[0])-1):
                    self.grille[i][j] = 1
            for i in range(3,4):
                for j in range (26,45):
                    self.grille[i][j] = 1
            for i in range(5,7):
                for j in range (39,45):
                    self.grille[i][j] = 1
            for i in range(0,18):
                for j in range (49,len(self.grille[0])-1):
                    self.grille[i][j] = 1
            for i in range(19,len(self.grille)-1):
                for j in range (48,len(self.grille[0])-1):
                    self.grille[i][j] = 1
        if self.num == 4:
            for i in range(0,len(self.grille)-1):
                for j in range (49,len(self.grille[0])-1):
                    self.grille[i][j] = 1
            for i in range(7,20):
                for j in range (47,len(self.grille[0])-1):
                    self.grille[i][j] = 1
        if self.num == 5:
            for i in range(0,len(self.grille)-1):
                for j in range (49,len(self.grille[0])-1):
                    self.grille[i][j] = 1
            for i in range(29,len(self.grille)-1):
                for j in range (45,len(self.grille[0])-1):
                    self.grille[i][j] = 1
            for i in range(35,len(self.grille)-1):
                for j in range (8,len(self.grille[0])-1):
                    self.grille[i][j] = 1
            for i in range(37,len(self.grille)-1):
                for j in range (0,7):
                    self.grille[i][j] = 1
        if self.num == 6:
            for i in range(0,len(self.grille)-1):
                for j in range (0,2):
                    self.grille[i][j] = 1
            for i in range(29,len(self.grille)-1):
                for j in range (0,6):
                    self.grille[i][j] = 1
            for i in range(35,len(self.grille)-1):
                for j in range (0,43):
                    self.grille[i][j] = 1
            for i in range(37,len(self.grille)-1):
                for j in range (44,51):
                    self.grille[i][j] = 1


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
    def __init__(self, nom, x, y):
        self.posx = x
        self.posy = y
        self.nom = nom
        self.image = ''

    def draw(self, fenetre):
        fenetre.blit(pygame.image.load(self.image), (self.posx, self.posy))

class Ressource(Object):
    def __init__(self, x, y, quantite):
        super().__init__("cobalt", x, y)
        self.quantite = quantite
        self.image = "images/cobalt.jpg"


class Piece(Object):
    def __init__(self, nom, x, y, point):
        super().__init__(nom, x, y)
        self.image = "images/"+self.nom+".png"
        self.point = point
