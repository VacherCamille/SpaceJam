class Monstre:

    def __init__(self):
        self.pv = 100
        self.speed = 10
        self.degat = 1  # nombre de point qu'enlève le monstre au score du joueur
        self.distance = 10


class Pieuvre(Monstre):

    def __init__(self):
        Monstre.__init__(self)


class Tireur(Monstre):

    def __init__(self):
        Monstre.__init__(self)


class Coureur(Monstre):

    def __init__(self):
        Monstre.__init__(self)