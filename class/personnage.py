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
        self.posx = x
        self.posy = y
        self.speedx = 0
        self.speedy = 0
        self.arme = Arme()
        self.vaisseau = Vaisseau()
