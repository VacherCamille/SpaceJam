import pygame
from pygame import *
from def_class import *
from random import *

# Fonctions
pygame.init()

def redraw():
    #print(hero.posx, hero.posy)
    print(hero.map.num, hero.posx, hero.posy)
    hero.map.draw(fenetre, hero.map.bordure)
    hero.draw(fenetre)
    if not (hero.colision()):
        hero.applique_mouvements()
    fenetre.blit(text,(700,10))
    fenetre.blit(timerTxt,(512,10))
    pygame.display.set_caption('Space Walker')

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
        fenetre.blit(vaisseauTxt, (40, 130))
        fenetre.blit(itemVaisseauTxt, (10, 155))
        fenetre.blit(cobaltVaisseauTxt, (10, 175))

    for bullet in bullets:
        if (bullet.colision(hero.map.grille)):
            bullets.pop(bullets.index(bullet))
        bullet.draw(fenetre)
    pygame.display.update()


def initialisation_jeu():
    global hero, maps, lastKey, bullets, run, fenetre, fond, beginTime, timerTxt, imageVaisseau, score
    global map0, map1, map2, map3, map4, map5, map6

    score = 0

    fenetre = pygame.display.set_mode((1024, 768))
    fond = pygame.image.load("images/fond.png").convert()

    imageVaisseau = pygame.image.load("images/vaisseau.png")
    imageVaisseau = pygame.transform.scale(imageVaisseau, (768,768))

    asteroides_map1 = [Asteroide(550, 500, 1), Asteroide(650, 150, 2), Asteroide(150, 550, 3), Asteroide(850, 50, 4), Asteroide(900, 650, 1),Asteroide(100, 100, 2)]
    asteroides_map2 = [Asteroide(220, 668, 1), Asteroide(900, 150, 2), Asteroide(100, 400, 3), Asteroide(500, 300, 4), Asteroide(800, 600, 1),Asteroide(200, 200, 2)]
    asteroides_map3 = [Asteroide(400, 200, 1), Asteroide(650, 500, 2), Asteroide(600, 50, 3), Asteroide(80, 668, 4), Asteroide(400, 400, 1),Asteroide(300, 250, 2)]
    asteroides_map4 = [Asteroide(550, 500, 1), Asteroide(650, 150, 2), Asteroide(150, 550, 3), Asteroide(00, 450, 4), Asteroide(900, 650, 1),Asteroide(100, 100, 2)]
    asteroides_map5 = [Asteroide(550, 500, 1), Asteroide(650, 150, 2), Asteroide(150, 550, 3), Asteroide(850, 50, 4), Asteroide(900, 650, 1),Asteroide(100, 100, 2)]
    asteroides_map6 = [Asteroide(550, 500, 1), Asteroide(650, 150, 2), Asteroide(150, 550, 3), Asteroide(850, 50, 4), Asteroide(900, 650, 1),Asteroide(100, 100, 2)]

## aliens
    alien_map1 = []
    alien_map2 = []
    alien_map3 = []
    alien_map4 = []
    alien_map5 = []
    alien_map6 = []

    nbAliens = randint(2,5)
    xAliens = sample(range(10, 990), nbAliens)
    yAliens = sample(range(10,620), nbAliens)
    for i in range(0,nbAliens):
        typeAlien = randint(1,3)
        if typeAlien == 1:
            alien_map1.append(Monstre(xAliens[i], yAliens[i]))

        elif typeAlien == 2:
            alien_map1.append(MonstreCoureur(xAliens[i], yAliens[i]))

        elif typeAlien == 3:
            alien_map1.append(MonstreTireur(xAliens[i], yAliens[i]))

    nbAliens = randint(2,5)
    xAliens = sample(range(10, 990), nbAliens)
    yAliens = sample(range(10,620), nbAliens)
    for i in range(0,nbAliens):
        typeAlien = randint(1,3)
        if typeAlien == 1:
            alien_map2.append(Monstre(xAliens[i], yAliens[i]))

        elif typeAlien == 2:
            alien_map2.append(MonstreCoureur(xAliens[i], yAliens[i]))

        elif typeAlien == 3:
            alien_map2.append(MonstreTireur(xAliens[i], yAliens[i]))

    nbAliens = randint(2,5)
    xAliens = sample(range(10, 990), nbAliens)
    yAliens = sample(range(10,620), nbAliens)
    for i in range(0,nbAliens):
        typeAlien = randint(1,3)
        if typeAlien == 1:
            alien_map3.append(Monstre(xAliens[i], yAliens[i]))

        elif typeAlien == 2:
            alien_map3.append(MonstreCoureur(xAliens[i], yAliens[i]))

        elif typeAlien == 3:
            alien_map3.append(MonstreTireur(xAliens[i], yAliens[i]))

    nbAliens = randint(2,5)
    xAliens = sample(range(10, 990), nbAliens)
    yAliens = sample(range(10,620), nbAliens)
    for i in range(0,nbAliens):
        typeAlien = randint(1,3)
        if typeAlien == 1:
            alien_map4.append(Monstre(xAliens[i], yAliens[i]))

        elif typeAlien == 2:
            alien_map4.append(MonstreCoureur(xAliens[i], yAliens[i]))

        elif typeAlien == 3:
            alien_map4.append(MonstreTireur(xAliens[i], yAliens[i]))

    nbAliens = randint(2,5)
    xAliens = sample(range(10, 990), nbAliens)
    yAliens = sample(range(10,620), nbAliens)
    for i in range(0,nbAliens):
        typeAlien = randint(1,3)
        if typeAlien == 1:
            alien_map5.append(Monstre(xAliens[i], yAliens[i]))

        elif typeAlien == 2:
            alien_map5.append(MonstreCoureur(xAliens[i], yAliens[i]))

        elif typeAlien == 3:
            alien_map5.append(MonstreTireur(xAliens[i], yAliens[i]))

    nbAliens = randint(2,5)
    xAliens = sample(range(10, 990), nbAliens)
    yAliens = sample(range(10,620), nbAliens)
    for i in range(0,nbAliens):
        typeAlien = randint(1,3)
        if typeAlien == 1:
            alien_map6.append(Monstre(xAliens[i], yAliens[i]))
        elif typeAlien == 2:
            alien_map6.append(MonstreCoureur(xAliens[i], yAliens[i]))

        elif typeAlien == 3:
            alien_map6.append(MonstreTireur(xAliens[i], yAliens[i]))

    cobalt_map1 = [Ressource(600, 500, 13), Ressource(500, 650, 13)]
    cobalt_map2 = [Ressource(600, 500, 13), Ressource(500, 650, 13)]
    cobalt_map3 = [Ressource(600, 500, 13), Ressource(500, 650, 13)]
    cobalt_map4 = [Ressource(600, 500, 13), Ressource(500, 650, 13)]
    cobalt_map5 = [Ressource(600, 500, 13), Ressource(500, 650, 13)]
    cobalt_map6 = [Ressource(600, 500, 13), Ressource(500, 650, 13)]

    piece_map1 = [Piece("filtre à air", 500, 500, 30)]
    piece_map2 = [Piece("durite moteur", 500, 500, 30)]
    piece_map3 = [Piece("generateur hydrogene", 500, 500, 30)]
    piece_map4 = [Piece("filtre à eau", 500, 500, 30)]
    piece_map5 = [Piece("tube incubation", 500, 500, 30)]
    piece_map6 = [Piece("reserve helium", 500, 500, 30)]

    map0 = Map(0, "images/vaisseau.png", [], [], [], [])
    map1 = Map(1, "images/vaisseau.png", asteroides_map1, cobalt_map1, piece_map1, alien_map1)
    map2 = Map(2, "images/map2.png", asteroides_map2, cobalt_map2, piece_map2, alien_map2)
    map3 = Map(3, "images/map3.png", asteroides_map3, cobalt_map3, piece_map3, alien_map3)
    map4 = Map(4, "images/map4.png", asteroides_map4, cobalt_map4, piece_map4, alien_map4)
    map5 = Map(5, "images/map5.png", asteroides_map5, cobalt_map5, piece_map5, alien_map5)
    map6 = Map(6, "images/map6.png", asteroides_map6, cobalt_map6, piece_map6, alien_map6)



    vassal = Vaisseau("Aurora")
    hero = Joueur(100, 400, 30, 68, 10, map1, vassal)
    beginTime = pygame.time.get_ticks()
    bullets = []
    lastKey = "right"
    run = True

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

        elif bullet.dir == "up-right" and bullet.posx < 1024 and bullet.posx > 0 and bullet.posy < 768 and bullet.posy > 0:
            bullet.posy -= bullet.vel
            bullet.posx += bullet.vel

        elif bullet.dir == "up-left" and bullet.posx < 1024 and bullet.posx > 0 and bullet.posy < 768 and bullet.posy > 0:
            bullet.posy -= bullet.vel
            bullet.posx -= bullet.vel

        elif bullet.dir == "down-right" and bullet.posx < 1024 and bullet.posx > 0 and bullet.posy < 768 and bullet.posy > 0:
            bullet.posy += bullet.vel
            bullet.posx += bullet.vel

        elif bullet.dir == "down-left" and bullet.posx < 1024 and bullet.posx > 0 and bullet.posy < 768 and bullet.posy > 0:
            bullet.posy += bullet.vel
            bullet.posx -= bullet.vel

        else:
            bullets.pop(bullets.index(bullet))



def rebond_ressort(keys):
    if hero.colision() and keys[pygame.K_w] and keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
        print ("saut haut droite")
        hero.vitessex = 17
        hero.vitessey = -17
        hero.applique_mouvements()
    elif hero.colision() and keys[pygame.K_w] and keys[pygame.K_UP] and keys[pygame.K_LEFT]:
        print ("saut haut gauche")
        hero.vitessex = -17
        hero.vitessey = -17
        hero.applique_mouvements()
    elif hero.colision() and keys[pygame.K_w] and keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
        print ("saut bas droite")
        hero.vitessex = 17
        hero.vitessey = 17
        hero.applique_mouvements()
    elif hero.colision() and keys[pygame.K_w] and keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
        print ("saut bas gauche")
        hero.vitessex = -17
        hero.vitessey = 17
        hero.applique_mouvements()
    elif hero.colision() and keys[pygame.K_w] and keys[pygame.K_DOWN] :
        print ("saut bas")
        hero.vitessey = 25
        hero.applique_mouvements()
    elif hero.colision() and keys[pygame.K_w] and keys[pygame.K_UP] :
        print ("saut haut")
        hero.vitessey = -25
        hero.applique_mouvements()
    elif hero.colision() and keys[pygame.K_w] and keys[pygame.K_RIGHT] :
        print ("saut droite")
        hero.vitessex = 25
        hero.applique_mouvements()
    elif hero.colision() and keys[pygame.K_w] and keys[pygame.K_LEFT]:
        print ("saut gauche")
        hero.vitessex = -25
        hero.applique_mouvements()


# def controlMap(map):
#     if map == 0:
#         if hero.posx > 1024:
#             hero.map = map1
#             hero.posx = 310
#     elif map == 1:
#         if hero.posx >= 280 and hero.posx <= 340 and hero.posy <= 340 and hero.posy >= 310:
#             hero.map = map0
#             hero.posx = 0
#         elif hero.posx > 1024:
#             hero.map = map4
#             hero.posx = 0
#         elif hero.posy < 0:
#             hero.map = map2
#             hero.posy = 728
#         elif hero.posy > 728:
#             hero.map = map6
#             hero.posy = 0
#     elif map == 2:
#         if hero.posx > 1024:
#             hero.map = map3
#             hero.posx = 0
#         elif hero.posy > 768:
#             hero.map = map4
#             hero.posy = 0
#     elif map == 3:
#         if hero.posx < 0:
#             hero.map = map2
#             hero.posx = 1024
#         elif hero.posy > 768:
#             hero.map = map4
#             hero.posy = 0
#     elif map == 4:
#         if hero.posx < 0:
#             hero.map = map1
#             hero.posx = 1024
#         elif hero.posy > 768:
#             hero.map = map5
#             hero.posy = 0
#         elif hero.posy < 0:
#             hero.map = map3
#             hero.posy = 768
#     elif map == 5:
#         if hero.posx < 0:
#             hero.map = map6
#             hero.posx = 1024
#         elif hero.posy < 0:
#             hero.map = map4
#             hero.posy = 768
#     else:
#         if hero.posx > 1024:
#             hero.map = map5
#             hero.posx = 0
#         elif hero.posy < 0:
#             hero.map = map1
#             hero.posy = 768
#
#     redraw()

################
# MAIN PROG JEUX
################


def game():
    pygame.mixer.stop()
    # son jeu
    son = pygame.mixer.Sound("jeu2.wav")
    son.play(1000)

    global run, text, score, timerTxt
    initialisation_jeu()
    lastKey = "right"
    # Boucle principale

    while run:
        score += 1 # à enlever quand systeme de point mis en place
        #chronomètre
        seconds = int(180 - (pygame.time.get_ticks() - beginTime)/1000)
        min = int(seconds/60)
        seconds = int(seconds % 60)
        if seconds == 0 and min == 0:
            run = False
        font = pygame.font.Font('American_Captain.ttf', 50)

        if seconds<10:
            timerTxt = font.render(str(min) + ":0" + str(seconds), True, (250, 128, 114))
        else:
            timerTxt = font.render(str(min)+":"+str(seconds), True, (250, 128, 114))

        # Indicateur (numéro de carte)
        font = pygame.font.Font('American_Captain.ttf', 50)
        text = font.render("Numero map:"+str(hero.map.num),True,(255,0,0))

        pygame.time.delay(15)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.mixer.stop()
                run = False


        shoot(bullets)
        keys = pygame.key.get_pressed()
        # definition des changement de maps

        # Code pour fonction controlMap -> marche pas
        # if keys[pygame.K_LEFT]:
        #     hero.mouvement_horizontal(-hero.vel)
        #     lastKey = "left"
        #     controlMap(hero.map)
        #
        # if keys[pygame.K_RIGHT]:
        #     hero.mouvement_horizontal(+hero.vel)
        #     lastKey = "right"
        #     controlMap(hero.map)
        #
        # if keys[pygame.K_UP]:
        #     hero.mouvement_vertical(-hero.vel)
        #     lastKey = "up"
        #     controlMap(hero.map)
        #
        # if keys[pygame.K_DOWN]:
        #     hero.mouvement_vertical(+hero.vel)
        #     lastKey = "down"
        #     controlMap(hero.map)

        if keys[pygame.K_LEFT] and hero.map.num == 1:
            if hero.posx >= 280 and hero.posx <= 340 and hero.posy <= 340 and hero.posy >= 310:
                hero.map = map0
                hero.posx = 1024
            elif hero.posx > 0:
                hero.mouvement_horizontal(-hero.vel)
                lastKey = "left"
        elif keys[pygame.K_LEFT] and hero.posx > 0:
            hero.posx -= hero.vel
            lastKey = "left"
        elif keys[pygame.K_LEFT]:
            lastKey = "left"
            if hero.map.num == 3:
                hero.map = map2
                hero.posx = 1024
            elif hero.map.num == 4:
                hero.map = map1
                hero.posx = 1024
            elif hero.map.num == 5:
                hero.map= map6
                hero.posx = 1024


        if keys[pygame.K_RIGHT] and hero.posx < 1024-50:
            hero.mouvement_horizontal(hero.vel)
            lastKey="right"
        elif keys[pygame.K_RIGHT]:
            lastKey="right"
            if hero.map.num == 0:
                hero.map = map1
                hero.posx = 0
            elif hero.map.num == 1:
                hero.map = map4
                hero.posx = 0
            elif hero.map.num == 2:
                hero.map = map3
                hero.posx = 0
            elif hero.map.num == 6:
                hero.map = map5
                hero.posx = 0

        if keys[pygame.K_DOWN] and hero.posy < 768-  hero.height:
            hero.mouvement_vertical(hero.vel)
            lastKey = "down"
        elif keys[pygame.K_DOWN]:
            lastKey = "down"
            if hero.map.num == 1:
                hero.map = map6
                hero.posy = 0
            elif hero.map.num == 2:
                hero.map = map1
                hero.posy = 0
            elif hero.map.num == 3:
                hero.map = map4
                hero.posy = 0
            elif hero.map.num == 4:
                hero.map = map5
                hero.posy = 0

        if keys[pygame.K_UP] and hero.posy > 0:
            hero.mouvement_vertical(-hero.vel)
            lastKey="up"
        elif keys[pygame.K_UP]:
            lastKey="up"
            if hero.map.num == 1:
                hero.map = map2
                hero.posy = 768
            elif hero.map.num == 4:
                hero.map = map3
                hero.posy = 768
            elif hero.map.num == 6:
                hero.map = map1
                hero.posy = 768
            elif hero.map.num == 5:
                hero.map = map4
                hero.posy = 768


        if keys[pygame.K_LCTRL] and not ( keys[pygame.K_UP] and keys[pygame.K_RIGHT]) and not (keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]) and not (keys[pygame.K_LEFT] and keys[pygame.K_UP]) and not (keys[pygame.K_LEFT] and keys[pygame.K_DOWN]):
            #print(lastKey)
            if len(bullets) < 25:
                bullets.append(Projectil(round(hero.posx + hero.width + 20 // 2), round(hero.posy + hero.height // 2), 6,
                                         (120, 154, 66), 45, lastKey))
                hero.recul(lastKey)
        if keys[pygame.K_LCTRL] and keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
            print("up-right")
            if len(bullets) < 25:
                bullets.append(Projectil(round(hero.posx + hero.width + 20 //2), round(hero.posy + hero.height//2), 6, (120,154,66),45 , "up-right")) #vitesse 45
                hero.recul("up-right")

        if keys[pygame.K_LCTRL] and keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
            print("down right")
            if len(bullets) < 25:
                bullets.append(Projectil(round(hero.posx + hero.width + 20 //2), round(hero.posy + hero.height//2), 6, (120,154,66),45 , "down-right")) #vitesse 45
                hero.recul("down-right")

        if keys[pygame.K_LCTRL] and keys[pygame.K_UP] and keys[pygame.K_LEFT]:
            print("up-left")
            if len(bullets) < 25:
                bullets.append(Projectil(round(hero.posx + hero.width + 20 // 2), round(hero.posy + hero.height // 2), 6, (120, 154, 66), 45, "up-left"))  # vitesse 45
                hero.recul("up-left")

        if keys[pygame.K_LCTRL] and keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
            print("down-left")
            if len(bullets) < 25:
                bullets.append(Projectil(round(hero.posx + hero.width + 20 // 2), round(hero.posy + hero.height // 2), 6, (120, 154, 66), 45, "down-left"))  # vitesse 45
                hero.recul("down-left")

        rebond_ressort(keys)

        redraw()
    return score
