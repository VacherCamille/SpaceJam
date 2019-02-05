import pygame

from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((640,480),RESIZABLE)
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0,0))

perso = pygame.image.load("perso.png").convert_alpha()
perso_x = 0
perso_y = 0
fenetre.blit(perso, (perso_x, perso_y))

pygame.display.flip()
pygame.key.set_repeat(400,30)

continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
             continuer = 0
        # if event.type == KEYDOWN:
        #     if event.key == K_DOWN:
        #         position_perso = position_perso.move(0,5)
        #     if event.key == K_RIGHT:
        #         position_perso = position_perso.move(5,0)
        #     if event.key == K_LEFT:
        #         position_perso = position_perso.move(-5,0)
        #     if event.key == K_UP:
        #         position_perso = position_perso.move(0,-5)
        # if event.type == MOUSEBUTTONDOWN:
        #     if event.button == 1:
        #         perso_x = event.pos[0]
        #         perso_y = event.pos[1]
        if event.type == MOUSEMOTION:
            perso_x = event.pos[0]
            perso_y = event.pos[1]

    fenetre.blit(fond, (0,0))
    fenetre.blit(perso, (perso_x, perso_y))
    pygame.display.flip()


