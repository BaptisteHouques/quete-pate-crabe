from models.personnage import Personnage

class Bob(Personnage):
    def __init__(self):
        super().__init__("Bob l'éponge", vie=100, force=10)