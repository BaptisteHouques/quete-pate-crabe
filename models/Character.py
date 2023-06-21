class Character:
    def __init__(self, nom, force):
        self.nom = nom
        self.vie = vie
        self.force = force

    def __str__(self):
        return f"{self.nom} : Vie {self.vie}, Force {self.force}"