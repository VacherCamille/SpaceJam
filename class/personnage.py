# fichier de classes relatives à tout ce que possède un personnage

class Vaisseau:
    def __init__(self):
        self.obItem = ["moteur", "aiguille de direction", "propulseur"]
        self.takenItem = []


class Arme:
    def __init__(self):
        self.degat = 50
        self.recul = 10


class Joueur:
    def __init__(self,x,y):
        # # Sprites du personnage
        # self.droite = pygame.image.load(droite).convert_alpha()
        # self.gauche = pygame.image.load(gauche).convert_alpha()
        # self.haut = pygame.image.load(haut).convert_alpha()
        # self.bas = pygame.image.load(bas).convert_alpha()
        self.posx = x
        self.posy = y
        self.speedx = 0
        self.speedy = 0
        self.arme = Arme()
        self.vaisseau = Vaisseau()
        self.points = 0
        # self.direction = self.droite

    def perdPoints(self, degat):
        self.points = self.points-degat

    def gagnePoints(self, gain):
        self.points = self.point+gain

    def deplacement(self, d):
        if d == gauche :
            self.posx = self.posx-1

        else if d == droite :
            self.posx = self.posx+1

        else if d == haut :
            self.posy = self.posy+1

        else
            self.posy = self.posy-1

    def reculer(self, d):
        self.posx = self.posx-d