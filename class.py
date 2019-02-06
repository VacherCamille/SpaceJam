#  classes relatives à tout ce que possède un personnage

class Vaisseau:
    def __init__(self):
        self.obItem = ["moteur", "aiguille de direction", "propulseur"]
        self.takenItem = []


class Arme:
    def __init__(self):
        self.degat = 50
        self.recul = 10


class Joueur:
    def __init__(self, x, y, gauche, droite, haut, bas):
        # Sprites du personnage
        self.droite = pygame.image.load(droite).convert_alpha()
        self.gauche = pygame.image.load(gauche).convert_alpha()
        self.haut = pygame.image.load(haut).convert_alpha()
        self.bas = pygame.image.load(bas).convert_alpha()
        self.posx = x
        self.posy = y
        self.speedx = 0
        self.speedy = 0
        self.arme = Arme()
        self.vaisseau = Vaisseau()
        self.points = 0
        self.direction = self.droite

    def perdPoints(self, degat):
        self.points = self.points-degat

    def gagnePoints(self, gain):
        self.points = self.point+gain

    def deplacement(self, d):
        if d == 'gauche' :
            self.posx = self.posx-50
            print(self.posx)
        elif d == 'droite' :
            self.posx = self.posx+50
            print(self.posx)
        elif d == 'haut' :
            self.posy = self.posy+50
            print(self.posy)
        else :
            self.posy = self.posy-50
            print(self.posy)
    def reculer(self, d):
        self.posx = self.posx-d


# classes monstres
class Monstre:

    def __init__(self):
        # # Sprites du monstre
        # self.droite = pygame.image.load(droite).convert_alpha()
        # self.gauche = pygame.image.load(gauche).convert_alpha()
        # self.haut = pygame.image.load(haut).convert_alpha()
        # self.bas = pygame.image.load(bas).convert_alpha()
        self.pv = 100
        self.speed = 10
        self.degat = 1  # nombre de point qu'enlève le monstre au score du joueur
        self.distance = 10
        self.x = 0
        self.y = 0


    def attaque(self, perso):
        perso.perdPoints(self.degat)
        perso.reculer(self.distance)

    def deplacement(self, d):
        if d == 'gauche' :
            self.x = self.x-1

        else if d == 'droite':
            self.x = self.x+1

        else if d == 'haut':
            self.y = self.y+1

        else
            self.y = self.y-1


class Pieuvre(Monstre):

    def __init__(self):
        Monstre.__init__(self)


class Tireur(Monstre):

    def __init__(self):
        Monstre.__init__(self)


class Coureur(Monstre):

    def __init__(self):
        Monstre.__init__(self)


# autre classes
class Object:
    def __init__(self, nom):
        self.posx = random.randint(1, 100)
        self.posy = random.randint(1, 100)
        self.points = 10
        self.nom = nom


class Asteroid:
    def __init__(self):
        self.posx = random.randint(1, 100)
        self.posy = random.randint(1, 100)


class Projectil:
    def __init__(self,x,y,radius):
        self.posx = x
        self.posy = y
        self.radius = radius
