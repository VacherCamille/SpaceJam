import pygame

from pygame.locals import *

pygame.init()

pygame.display.set_caption("Le jeux vidéale")

fenetre = pygame.display.set_mode((1024,768),RESIZABLE)
fond = pygame.image.load("fond.png").convert()
perso = pygame.image.load("perso.png")

clock = pygame.time.Clock()

x = 0
y = 200
vel = 5
width = 1024
height = 768

class Joueur(object):
    def __init__(self,x,y,width,height,vel):
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
        # self.vaisseau = Vaisseau()
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

def redraw():
    fenetre.blit(fond, (0,0))
    hero.draw(fenetre)
    for bullet in bullets:
        bullet.draw(fenetre)
    pygame.display.update()

hero = Joueur(100,400,30,68,5)
bullets =[]

run = True
while run:
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

    if keys[pygame.K_LEFT] and hero.posx > 0:
        hero.posx -= hero.vel
    if keys[pygame.K_RIGHT] and hero.posx < 1024-30:
        hero.posx += hero.vel
    if keys[pygame.K_DOWN]:
        hero.posy += hero.vel
    if keys[pygame.K_UP]:
        if len(bullets) < 5:
            bullets.append(Projectil(round(hero.posx + hero.width + 20 //2), round(hero.posy + hero.height//2), 6, (120,154,66),10))
            hero.posx -= 10

    redraw()
pygame.quit()

# perso = pygame.image.load("perso.png").convert_alpha()
# perso_x = 0
# perso_y = 0
# fenetre.blit(perso, (perso_x, perso_y))
#
# pygame.display.flip()
# pygame.key.set_repeat(400,30)

# continuer = 1
# while continuer:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#              continuer = 0
#         # if event.type == KEYDOWN:
#         #     if event.key == K_DOWN:
#         #         position_perso = position_perso.move(0,5)
#         #     if event.key == K_RIGHT:
#         #         position_perso = position_perso.move(5,0)
#         #     if event.key == K_LEFT:
#         #         position_perso = position_perso.move(-5,0)
#         #     if event.key == K_UP:
#         #         position_perso = position_perso.move(0,-5)
#         # if event.type == MOUSEBUTTONDOWN:
#         #     if event.button == 1:
#         #         perso_x = event.pos[0]
#         #         perso_y = event.pos[1]
#         if event.type == MOUSEMOTION:
#             perso_x = event.pos[0]
#             perso_y = event.pos[1]
#
#     fenetre.blit(fond, (0,0))
#     fenetre.blit(perso, (perso_x, perso_y))
#     pygame.display.flip()


