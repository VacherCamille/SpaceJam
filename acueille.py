import pygame

pygame.init()
fenetre = pygame.display.set_mode((1024,768))

#coordonées start
x_start = 300;
y_start = 200;

#coordonées crédits
x_c = 30;
y_c = 600;

pygame.display.set_caption('Menu Start')

#affichage du bouton start
start = pygame.image.load("rectangle.png").convert()
fenetre.blit(start ,  ( x_start,y_start))

#affichage du bouton crédits
credits = pygame.image.load("rectangle.png").convert()
fenetre.blit(credits ,  ( x_c,y_c))

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

            if credits.get_rect(topleft=(30,600)).collidepoint(x, y):
                print('crédits')
                print(x, y)

#loop over, quite pygame
pygame.quit()