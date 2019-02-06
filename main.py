import pygame
from pygame import *
from def_class import *
pygame.init()

# Fonctions

def redraw():
    hero.map.draw(fenetre, imageVaisseau)
    hero.draw(fenetre)

    fenetre.blit(text,(700,10))
    fenetre.blit(timerTxt,(512,10))


    # affichage score
    font = pygame.font.Font('American_Captain.ttf', 30)
    scoreTxt = font.render("score : " + str(score), True, (250, 128, 114))
    fenetre.blit(scoreTxt, (10, 10))


    #affichage sac
    font = pygame.font.Font('American_Captain.ttf', 25)
    sacTxt = font.render("sac", True, (250, 128, 114))
    cobaltSacTxt = font.render("cobalt : " + str(hero.cobalt), True, (250, 128, 114))
    itemSacTxt = font.render("item : " + str(hero.unePiece), True, (250, 128, 114))

    pygame.draw.rect(fenetre, (115, 194, 251), (5, 45, 150, 75))
    fenetre.blit(sacTxt, (60, 50))
    fenetre.blit(itemSacTxt, (10, 75))
    fenetre.blit(cobaltSacTxt, (10, 95))


    #affichage du contenu du vaisseau quand il est dedans
    if hero.map.num == 0:
        font = pygame.font.Font('American_Captain.ttf', 25)
        vaisseauTxt = font.render("vaisseau", True, (250, 128, 114))
        itemVaisseauTxt = font.render("item : " + str(hero.vaisseau.items), True, (250, 128, 114))
        cobaltVaisseauTxt = font.render("cobalt : " + str(hero.vaisseau.cobalt), True, (250, 128, 114))

        pygame.draw.rect(fenetre, (115, 194, 251), (5, 125, 150, 75))
        fenetre.blit(vaisseauTxt, (60, 130))
        fenetre.blit(itemVaisseauTxt, (10, 155))
        fenetre.blit(cobaltVaisseauTxt, (10, 175))

    for bullet in bullets:
        bullet.draw(fenetre)
    pygame.display.update()


def initialisation_jeu():
    global hero, maps, lastKey, bullets, run, fenetre, fond, beginTime, timerTxt, imageVaisseau, score

    score = 0

    fenetre = pygame.display.set_mode((1024, 768))
    fond = pygame.image.load("map.png").convert()

    imageVaisseau = pygame.image.load("vaisseau.png")
    imageVaisseau = pygame.transform.scale(imageVaisseau, (300,200))

    asteroides_map1 = [Asteroide(10, 10, 2)]

    map0 = Map(0,"map.png",asteroides_map1)
    map1 = Map(1,"map.png",asteroides_map1)
    map2 = Map(2,"map.png",asteroides_map1)
    map3 = Map(3,"map.png",asteroides_map1)
    map4 = Map(4,"map.png",asteroides_map1)
    map5 = Map(5,"map.png",asteroides_map1)
    map6 = Map(6,"map.png",asteroides_map1)

    vassal = Vaisseau("Aurora")
    hero = Joueur(100, 400, 30, 68, 30, map1, vassal)
    beginTime = pygame.time.get_ticks()
    bullets = []
    lastKey = "right"
    run = True


def deplacement(hero):

    keys = pygame.key.get_pressed()

    # definition des changement de maps
    if keys[pygame.K_LEFT] and hero.posx > 0:
        hero.posx -= hero.vel
        lastKey = "left"
    elif keys[pygame.K_LEFT]:
        lastKey = "left"
        if hero.map.num == 1:
            hero.map.num = 0
            hero.posx = 1024
        elif hero.map.num == 3:
            hero.map.num = 2
            hero.posx = 1024
        elif hero.map.num == 4:
            hero.map.num = 1
            hero.posx = 1024
        elif hero.map.num == 5:
            hero.map.num = 6
            hero.posx = 1024

    if keys[pygame.K_RIGHT] and hero.posx < 1024-50:
        hero.posx += hero.vel
        lastKey="right"
    elif keys[pygame.K_RIGHT]:
        lastKey="right"
        if hero.map.num == 0:
            hero.map.num = 1
            hero.posx = 0
        elif hero.map.num == 1:
            hero.map.num = 4
            hero.posx = 0
        elif hero.map.num == 2:
            hero.map.num = 3
            hero.posx = 0
        elif hero.map.num == 6:
            hero.map.num = 5
            hero.posx = 0

    if keys[pygame.K_DOWN] and hero.posy < 768-  hero.height:
        hero.posy += hero.vel
        lastKey = "down"
    elif keys[pygame.K_DOWN]:
        lastKey = "down"
        if hero.map.num == 1:
            hero.map.num = 6
            hero.posy = 0
        elif hero.map.num == 2:
            hero.map.num = 1
            hero.posy = 0
        elif hero.map.num == 3:
            hero.map.num = 4
            hero.posy = 0
        elif hero.map.num == 4:
            hero.map.num = 5
            hero.posy = 0

    if keys[pygame.K_UP] and hero.posy > 0:
        hero.posy -= hero.vel
        lastKey="up"
    elif keys[pygame.K_UP]:
        lastKey="up"
        if hero.map.num == 1:
            hero.map.num = 2
            hero.posy = 768
        elif hero.map.num == 4:
            hero.map.num = 3
            hero.posy = 768
        elif hero.map.num == 6:
            hero.map.num = 1
            hero.posy = 768
        elif hero.map.num == 5:
            hero.map.num = 4
            hero.posy = 768

    if keys[pygame.K_SPACE]:
        if len(bullets) < 25:
            bullets.append(Projectil(round(hero.posx + hero.width + 20 //2), round(hero.posy + hero.height//2), 6, (120,154,66),45 , lastKey))
            hero.recul(lastKey)
            #hero.posx -= 10

def shoot(bullets):
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


################
# MAIN PROG JEUX
################

# Instanciations

initialisation_jeu()

# Boucle principale

while run:
    #chronomètre
    seconds = int(180 - (pygame.time.get_ticks() - beginTime)/1000)
    min = int(seconds/60)
    seconds = int(seconds % 60)
    if seconds == 0 and min == 0:
        run = False
    font = pygame.font.Font('American_Captain.ttf', 50)
    timerTxt = font.render(str(min)+":"+str(seconds), True, (250, 128, 114))

    # Indicateur (numéro de carte)
    font = pygame.font.Font('American_Captain.ttf', 50)
    text = font.render("Numero map:"+str(hero.map.num),True,(255,0,0))

    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

    shoot(bullets)
    deplacement(hero)

    redraw()
pygame.quit()


