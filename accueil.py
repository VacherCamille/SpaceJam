import pygame
from pygame import *

from main import *

pygame.init()
fenetre = pygame.display.set_mode((1024,768))

input_text = 'entrer votre nom'

def redraw():
    global input_text, nameTxt, start, credits, hscores, quiter, font

    #image de fond
    fond = pygame.image.load("fond.png").convert()
    fenetre.blit(fond, (0,0))

    pygame.display.set_caption('Menu Start')

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
    fenetre.blit(font.render("hightscore", True, (250, 128, 114)), (440, 535))

    #affichage du bouton quiter
    quiter = pygame.image.load("bouton2.png").convert()
    fenetre.blit(quiter ,  (825, 650))
    fenetre.blit(font.render("quitter", True, (0, 0, 0)), (860, 670))

    pygame.display.flip()

redraw()
running = True
clickEnterName = False
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if start.get_rect(topleft=(390, 200)).collidepoint(x, y):
                print('start')
                game()
                running = False
                break

            if credits.get_rect(topleft=(390,350)).collidepoint(x, y):
                print('crédits')

            if hscores.get_rect(topleft=(390,500)).collidepoint(x, y):
                print('hscores')

            if quiter.get_rect(topleft=(825,650)).collidepoint(x, y):
                print('quitter')
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