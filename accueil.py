import pygame
from pygame import *

from main import *

import operator
from operator import itemgetter

pygame.init()
fenetre = pygame.display.set_mode((1024,768))

input_text = 'entrer votre nom'

def redraw(img1="bouton.png", img2="bouton.png", img3="bouton.png", img4='bouton2.png' , img5='bouton2.png' , img6='bouton2.png' ):
    global input_text, nameTxt, start, histoire, hscores, quiter, font, sortir, aide

    #image de fond
    fond = pygame.image.load("images/fond.png").convert()
    fenetre.blit(fond, (0,0))

    # titre
    pygame.display.set_caption('Space Walker : High')

    titre = pygame.image.load("images/titre.png")
    titre = pygame.transform.scale(titre, (800, 200))
    fenetre.blit(titre, (140, -10))

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
    start = pygame.image.load(img1).convert() # start bouton img1
    fenetre.blit(start ,  ( 390,200))
    fenetre.blit(font.render("start", True, (250, 128, 114)), (480, 235))

    #affichage du bouton highscore
    hscores = pygame.image.load(img2).convert() # hscores bouton img2
    fenetre.blit(hscores ,  (390, 350))
    fenetre.blit(font.render(" highscore", True, (250, 128, 114)), (445, 385))

    # affichage du bouton histoire
    histoire = pygame.image.load(img3).convert() # histoire bouton img3
    fenetre.blit(histoire, (390, 500))
    fenetre.blit(font.render("histoire", True, (250, 128, 114)), (460, 535))

    # affichage du bouton quitter
    sortir = pygame.image.load(img4).convert()# a ne pas afficher : fait expres
    quiter = pygame.image.load(img5).convert()# quiter bouton2 img5
    fenetre.blit(quiter ,  (825, 650))
    fenetre.blit(font.render("quitter", True, (0, 0, 0)), (856, 670))

    # affichage du bouton aide
    aide = pygame.image.load(img6).convert()# aide bouton2 img6
    fenetre.blit(aide, (20, 650))
    fenetre.blit(font.render("aide", True, (0, 0, 0)), (70, 670))

    # son menu start
    s_start = pygame.mixer.Sound("start.wav")
    s_start.play()

    pygame.display.flip()

def drawHScore(img1="bouton2.png"):
    global sortir
    # image de fond
    fond = pygame.image.load("images/fond.png").convert()
    fenetre.blit(fond, (0, 0))

    pygame.display.set_caption('Menu Start : Highscore')

    # affichage du bouton sortir
    sortir = pygame.image.load(img1).convert()
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

def drawStory(img1="bouton2.png"):
    fond = pygame.image.load("images/fond.png").convert()
    fenetre.blit(fond, (0, 0))
    pygame.display.set_caption('Menu Start : aide')

    sortir = pygame.image.load(img1).convert()
    fenetre.blit(sortir, (825, 650))
    fenetre.blit(font.render("sortir", True, (0, 0, 0)), (860, 670))

    fichier_credit = open("histoire.txt", "r")
    n = 0
    for line in fichier_credit:
        n += 1
        # 39 charactère peuvent être mis dans une ligne
        fenetre.blit(font.render(line, True, (250, 128, 114)), (20, 20 + (n * 30)))

    pygame.display.flip()

def drawHelp(img1="bouton2.png"):
    fond = pygame.image.load("images/fond.png").convert()
    fenetre.blit(fond, (0, 0))
    pygame.display.set_caption('Menu Start : crédits')

    sortir = pygame.image.load(img1).convert()
    fenetre.blit(sortir, (825, 650))
    fenetre.blit(font.render("sortir", True, (0, 0, 0)), (860, 670))

    fichier_credit = open("help.txt", "r")
    n = 0
    for line in fichier_credit:
        n += 1
        #39 charactère peuvent être mis dans une ligne
        fenetre.blit(font.render(line, True, (250, 128, 114)), (20, 20 + (n*40)))

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

#son bouton
ss = pygame.mixer.Sound("clic.wav")
shs = pygame.mixer.Sound("bg.wav")
shsT = pygame.mixer.Sound("hs.wav")
sq = pygame.mixer.Sound("quit.wav")

while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if start.get_rect(topleft=(390, 200)).collidepoint(x, y):
                ss.play()
                redraw(img1="boutonINV.png")
                pygame.time.delay(500)
                print('start')
                score = game()
                #####pour tout fermer à la fin du jeux
                # running = False
                # break
                #####
                gameover()
                break
            if histoire.get_rect(topleft=(390, 500)).collidepoint(x, y):
                ss.play()
                redraw(img3="boutonINV.png")
                pygame.time.delay(500)
                accueil = False
                drawStory()

            if hscores.get_rect(topleft=(390,350)).collidepoint(x, y):
                shs.play()
                redraw(img2="boutonINV.png")
                pygame.time.delay(500)
                pygame.mixer.stop()
                shsT.play()
                accueil = False
                drawHScore()

            if aide.get_rect(topleft=(20, 650)).collidepoint(x, y):
                ss.play()
                redraw(img6="bouton2INV.png")
                pygame.time.delay(500)
                accueil = False
                drawHelp()

            if sortir.get_rect(topleft=(825,650)).collidepoint(x, y) and not accueil:
                ss.play()
                pygame.time.delay(500)
                shsT.stop()
                redraw()
                accueil = True
            elif quiter.get_rect(topleft=(825,650)).collidepoint(x, y) and accueil:
                sq.play()
                redraw(img5="bouton2INV.png")
                pygame.time.delay(500)
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