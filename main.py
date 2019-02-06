import pygame
from pygame import *

from def_class import *

pygame.init()

pygame.display.set_caption("Le jeux vidéale")

fenetre = pygame.display.set_mode((1024,768),RESIZABLE)
fond = pygame.image.load("fond.png").convert()

clock = pygame.time.Clock()

map0 = "fond.png"
map1 = "fond.png"
map2 = "fond.png"
map3 = "fond.png"
map4 = "fond.png"
map5 = "fond.png"
map6 = "fond.png"

# ici était les classes

def redraw():
    fenetre.blit(fond, (0,0))
    hero.draw(fenetre)
    fenetre.blit(text,(100,100))
    for bullet in bullets:
        bullet.draw(fenetre)
    pygame.display.update()

def deplacement(hero):
    keys = pygame.key.get_pressed()

     # definition des changement de maps
    if keys[pygame.K_LEFT] and hero.posx > 0:
        hero.posx -= hero.vel
        lastKey = "left"
    elif keys[pygame.K_LEFT]:
        lastKey = "left"
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
        lastKey="right"
    elif keys[pygame.K_RIGHT]:
        lastkey="right"
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

    if keys[pygame.K_DOWN] and hero.posy < 768-  hero.height:
        hero.posy += hero.vel
        lastKey = "down"
    elif keys[pygame.K_DOWN]:
        lastKey = "down"
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
        lastKey="up"
    elif keys[pygame.K_UP]:
        lastKey="up"
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
            bullets.append(Projectil(round(hero.posx + hero.width + 20 //2), round(hero.posy + hero.height//2), 6, (120,154,66),45 , lastKey)) #vitesse 50
            hero.recul(lastKey)
            #hero.posx -= 10

hero = Joueur(100,400,30,68,30,1)
maps = [Map(0,map0),Map(1,map1),Map(2,map2),Map(3,map3),Map(4,map4),Map(5,map5),Map(6,map6)]
bullets =[]
lastKey="right"

run = True
while run:
    font = pygame.font.Font('American_Captain.ttf', 100)
    text = font.render(str(hero.map),True,(255,0,0))

    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

    for bullet in bullets:
        if bullet.dir=="up" and bullet.posy < 768 and bullet.posy > 0 :
            bullet.posy -= bullet.vel

        elif bullet.dir=="down" and bullet.posy < 768 and bullet.posy > 0 :
            bullet.posy += bullet.vel

        elif bullet.dir=="right" and bullet.posx < 1024 and bullet.posx > 0:
            bullet.posx += bullet.vel

        elif bullet.dir=="left" and bullet.posx < 1024 and bullet.posx > 0:
            bullet.posx -= bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    deplacement(hero)

    # if keys[pygame.K_SPACE] and keys[pygame.K_UP]:
    #     if len(bullets) < 25:
    #         bullets.append(Projectil(round(hero.posx + hero.width + 20 //2), round(hero.posy + hero.height//2), 6, (120,154,66),45,"up")) #vitesse 50
    #         hero.posy -= 10

    redraw()
pygame.quit()


