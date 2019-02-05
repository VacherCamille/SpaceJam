import pygame
from personnage import *

from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((1024,768))
fond = pygame.image.load("fond.png").convert()
perso_img = pygame.image.load("perso.png").convert()
#p_img = perso_img.get_rect()
fenetre.blit(fond, (0,0))

# perso = pygame.image.load("perso.png").convert_alpha()
# position_perso = pygame.transform.scale(perso, (70,90))
# perso_x = 0
# perso_y = 0
#
# position_perso = perso.get_rect()
perso = Joueur(30,30, perso_img, perso_img, perso_img, perso_img)

fenetre.blit(perso.direction, (perso.posx, perso.posy))
# fenetre.blit(perso, (perso_x, perso_y))

pygame.display.flip()


def gerer_main_events():
    global continuer
    for event in pygame.event.get():
        if event.type == QUIT:
             continuer = 0

def gerer_joueur_events():
    ## Pour le clavier (keyboard)
    clavier = pygame.key.get_pressed()
    if clavier[pygame.K_UP]:
        perso.deplacement('haut')
        print("haut")
    if clavier[pygame.K_DOWN]:
        perso.deplacement('bas')
        print("bas")

    # ## Pour la souris (mouse)
    # if pygame.mouse.get_focused():
    #     souris = pygame.mouse.get_pressed()
    #     position = pygame.mouse.get_pos()
    #     if souris[0]: # Gauche
    #         position_perso = position_perso.move(100,0)
    #     if souris[1]: # Milieu
    #         print('clique de milieu', position)
    #     if souris[2]: # Droite
    #         print('clique de droite', position)

continuer = 1
while continuer:
    gerer_main_events()
    gerer_joueur_events()
    pygame.display.flip()
    # fenetre.blit(fond, (0,0))
    fenetre.blit(perso.direction, (perso.posx, perso.posy))

pygame.quit()
