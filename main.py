import pygame

from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((640,480),RESIZABLE)
fond = pygame.image.load("background.jpg")


continuer = 1

while continuer:
    continuer = int(input())



