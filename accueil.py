import pygame
from pygame import *

from main import *

import operator
from operator import itemgetter

pygame.init()
fenetre = pygame.display.set_mode((1024,768))

input_text = 'entrer votre nom'

def redraw():
    global input_text, nameTxt, start, credits, hscores, quiter, font, sortir

    #image de fond
    fond = pygame.image.load("images/fond.png").convert()
    fenetre.blit(fond, (0,0))

    pygame.display.set_caption('Space Walker : High')

    if score != None:
        font = pygame.font.Font('American_Captain.ttf', 20)
        fenetre.blit(font.render(input_text + ",", True, (250, 128, 114)), (10, 300))
        fenetre.blit(font.render("votre dernier score est : ", True, (250, 128, 114)), (10, 320))
        fenetre.blit(font.render(str(score), True, (250, 128, 114)), (50, 350))

    font = pygame.font.Font('American_Captain.ttf', 40)
    #affichage zone de text
    nameTxt = pygame.draw.rect(fenetre, (115, 194, 251), (387, 150, 250, 35))
    fenetre.blit(font.render(input_text, True, (0, 0, 0)), (390, 152))

    #affichage du bouton start
    start = pygame.image.load("bouton.png").convert()
    fenetre.blit(start ,  ( 390,200))
    fenetre.blit(font.render("start", True, (250, 128, 114)), (480, 235))

    #affichage du bouton crédits
    credits = pygame.image.load("bouton.png").convert()
    fenetre.blit(credits , ( 390,350))
    fenetre.blit(font.render("credits", True, (250, 128, 114)), (460, 385))

    #affichage du bouton highscore
    hscores = pygame.image.load("bouton.png").convert()
    fenetre.blit(hscores ,  (390, 500))
    fenetre.blit(font.render(" highscore", True, (250, 128, 114)), (440, 535))

    #affichage du bouton quiter
    sortir = pygame.image.load("bouton2.png").convert()
    quiter = pygame.image.load("bouton2.png").convert()
    fenetre.blit(quiter ,  (825, 650))
    fenetre.blit(font.render("quitter", True, (0, 0, 0)), (860, 670))

    pygame.display.flip()

def drawHScore():
    global sortir
    # image de fond
    fond = pygame.image.load("images/fond.png").convert()
    fenetre.blit(fond, (0, 0))

    pygame.display.set_caption('Menu Start : Highscore')

    # affichage du bouton quiter
    sortir = pygame.image.load("bouton2.png").convert()
    fenetre.blit(sortir, (825, 650))
    fenetre.blit(font.render("sortir", True, (0, 0, 0)), (860, 670))

    fichier_score = open("score.txt", "r")
    n = 0
    for line in fichier_score:
        n += 1
        line_split = line.split("|")
        lineToScreen = line_split[0]+" : "+line_split[1]
        fenetre.blit(font.render(str(n), True, (250, 128, 114)), (200, 20 + (60*n)))
        fenetre.blit(font.render("|", True, (250, 128, 114)), (230, 20 + (60 * n)))
        fenetre.blit(font.render(lineToScreen, True, (250, 128, 114)), (250, 20 + (60*n)))
    pygame.display.flip()


#fin D'UNE partie du jeux
def gameover():
    fichier_score = open("score.txt", "r")
    n = 0
    tab_score = []
    for line in fichier_score:
        n += 1
        line_split = line.split("|")
        line_split[1] = int(line_split[1].split("\n")[0])
        tab_score.append(line_split)

    tab_score = sorted(tab_score, key=itemgetter(1), reverse=True)
    for val in tab_score:
        if val[1]<score:
            tab_score.insert(tab_score.index(val), [input_text,score])
            break

    if len(tab_score) >10:
        tab_score.pop()

    fichier_score = open("score.txt", "w")
    for val in tab_score:
        fichier_score.write(val[0]+"|"+str(val[1])+"\n")

    fichier_score.close()
    fenetre = pygame.display.set_mode((1024, 768))
    redraw()

score = None
redraw()
running = True
accueil = True
clickEnterName = False
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if start.get_rect(topleft=(390, 200)).collidepoint(x, y):
                print('start')
                score = game()
                #####pour tout fermer à la fin du jeux
                # running = False
                # break
                #####
                gameover()
                break
            if credits.get_rect(topleft=(390,350)).collidepoint(x, y):
                print('crédits')

            if hscores.get_rect(topleft=(390,500)).collidepoint(x, y):
                accueil = False
                drawHScore()

            if sortir.get_rect(topleft=(825,650)).collidepoint(x, y) and not accueil:
                redraw()
                accueil = True
            elif quiter.get_rect(topleft=(825,650)).collidepoint(x, y) and accueil:
                running = False

            if nameTxt.collidepoint(x, y):
                clickEnterName = True
                input_text = ''
                redraw()
                nbChar = 0

        if event.type == pygame.KEYDOWN and clickEnterName and len(input_text)<10:
            input_text = input_text + str(event.unicode)
            redraw()

#loop over, quite pygame
pygame.quit()