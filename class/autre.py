import random


class Object:
    def __init__(self, nom):
        self.posx = random.randint(1,100)
        self.posy = random.randint(1,100)
        self.points = 10
        self.nom = nom


class Asteroid:
    def __init__(self):
        self.posx = random.randint(1, 100)
        self.posy = random.randint(1, 100)
