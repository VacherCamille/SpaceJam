import pygame
from pygame import *

pygame.init()

pygame.display.set_caption("Le jeux vidéale")

fenetre = pygame.display.set_mode((1024,768),RESIZABLE)
fond = pygame.image.load("fond.png").convert()
perso = pygame.image.load("perso.png")

clock = pygame.time.Clock()

map0 = "fond.png"
map1 = "fond.png"
map2 = "fond.png"
map3 = "fond.png"
map4 = "fond.png"
map5 = "fond.png"
map6 = "fond.png"

class Joueur(object):
    def __init__(self,x,y,width,height,vel,map):
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

    def draw(self,fenetre):
        fenetre.blit(perso, (self.posx, self.posy))
        self.hitbox = (self.posx, self.posy, 50, 75)
        pygame.draw.rect(fenetre, (255,0,0), self.hitbox,2)

class Projectil(object):
    def __init__(self,x,y,radius,color,vel):
        self.posx = x
        self.posy = y
        self.vel = vel
        self.radius = radius
        self.color = color

    def draw(self,fenetre):
        pygame.draw.circle(fenetre, self.color,(self.posx,self.posy), self.radius)

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
        self.hitbox = (self.posx, self.posy, 50, 75)

    def draw(self,fenetre):
        fenetre.blit(perso, (self.x, self.y))
        self.hitbox = (self.x, self.y, 50, 75)
        pygame.draw.rect(fenetre, (255,0,0), self.hitbox,2)

class Map(object):
    def __init__(self,num,bg):
        self.num = num
        self.fond = pygame.image.load(bg)
        self.meteor = []

    def draw(self,fenetre):
        fenetre.blit(self.fond, (0,0))

def redraw():
    fenetre.blit(fond, (0,0))
    hero.draw(fenetre)
    fenetre.blit(text,(100,100))
    for bullet in bullets:
        bullet.draw(fenetre)
    pygame.display.update()

hero = Joueur(100,400,30,68,30,1)
maps = [Map(0,map0),Map(1,map1),Map(2,map2),Map(3,map3),Map(4,map4),Map(5,map5),Map(6,map6)]
bullets =[]

run = True
while run:
    font = pygame.font.Font('American_Captain.ttf', 100)
    text = font.render(str(hero.map),True,(255,0,0))

    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

    for bullet in bullets:
        if bullet.posx < 1024 and bullet.posx > 0:
            bullet.posx += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

     # definition des changement de maps
    if keys[pygame.K_LEFT] and hero.posx > 0:
        hero.posx -= hero.vel
    elif keys[pygame.K_LEFT]:
        if hero.map == 1:
            hero.map = 0
            hero.posx = 1024
        elif hero.map == 3:
            hero.map = 2
            hero.posx = 1024
        elif hero.map == 4:
            hero.map = 1
            hero.posx = 1024
        elif hero.map == 5:
            hero.map = 6
            hero.posx = 1024

    if keys[pygame.K_RIGHT] and hero.posx < 1024-30:
        hero.posx += hero.vel
    elif keys[pygame.K_RIGHT]:
        if hero.map == 0:
            hero.map = 1
            hero.posx = 0
        elif hero.map == 1:
            hero.map = 4
            hero.posx = 0
        elif hero.map == 2:
            hero.map = 3
            hero.posx = 0
        elif hero.map == 6:
            hero.map = 5
            hero.posx = 0

    if keys[pygame.K_DOWN] and hero.posy < 768:
        hero.posy += hero.vel
    elif keys[pygame.K_DOWN]:
        if hero.map == 1:
            hero.map = 6
            hero.posy = 0
        elif hero.map == 2:
            hero.map = 1
            hero.posy = 0
        elif hero.map == 3:
            hero.map = 4
            hero.posy = 0
        elif hero.map == 4:
            hero.map = 5
            hero.posy = 0

    if keys[pygame.K_UP] and hero.posy > 0:
        hero.posy -= hero.vel
    elif keys[pygame.K_UP]:
        if hero.map == 1:
            hero.map = 2
            hero.posy = 768
        elif hero.map == 4:
            hero.map = 3
            hero.posy = 768
        elif hero.map == 6:
            hero.map = 1
            hero.posy = 768
        elif hero.map == 5:
            hero.map = 4
            hero.posy = 768

    if keys[pygame.K_SPACE]:
        if len(bullets) < 25:
            bullets.append(Projectil(round(hero.posx + hero.width + 20 //2), round(hero.posy + hero.height//2), 6, (120,154,66),10))
            hero.posx -= 10

    redraw()
pygame.quit()


