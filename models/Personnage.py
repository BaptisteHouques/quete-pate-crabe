class Personnage:
    def __init__(self, nom, humidite, force, vitesse, status=None):
        self.nom = nom
        self.humidite = humidite
        self.force = force
        self.vitesse = vitesse
        self.status = status or []
        
    def __str__(self):
        return f"{self.nom} : Humidité {self.humidite}, Force {self.force}, Vitesse {self.vitesse}, Status {self.status}"