from models import Character

class Bob(Character):
    def __init__(self):
        super().__init__("Bob l'éponge", hp=100, str=10)