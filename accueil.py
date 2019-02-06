import pygame
from pygame import *

pygame.init()
fenetre = pygame.display.set_mode((1024,768))

#image de fond
fond = pygame.image.load("fond.png").convert()
fenetre.blit(fond, (0,0))

pygame.display.set_caption('Menu Start')

#affichage zone de text
nameTxt = pygame.draw.rect(fenetre, (115, 194, 251), (387, 150, 250, 35))

#affichage du bouton start
start = pygame.image.load("bouton.png").convert()
fenetre.blit(start ,  ( 390,200))

#affichage du bouton crédits
credits = pygame.image.load("bouton.png").convert()
fenetre.blit(credits , ( 390,350))

#affichage du bouton highscore
hscores = pygame.image.load("bouton.png").convert()
fenetre.blit(hscores ,  (390, 500))

#affichage du bouton quiter
quiter = pygame.image.load("bouton2.png").convert()
fenetre.blit(quiter ,  (825, 650))

pygame.display.flip()

running = True
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if start.get_rect(topleft=(300, 200)).collidepoint(x, y):
                print('start')
                print(x, y)

            if credits.get_rect(topleft=(300,350)).collidepoint(x, y):
                print('crédits')
                print(x, y)

            if hscores.get_rect(topleft=(300,500)).collidepoint(x, y):
                print('hscores')
                print(x, y)

            if quiter.get_rect(topleft=(900,700)).collidepoint(x, y):
                print('quitter')
                running = False

            if nameTxt.collidepoint(x, y):
                nbChar = 0
                print("zone de text")

#loop over, quite pygame
pygame.quit()
