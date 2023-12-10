class Character:
    def __init__(self, name, hp, str):
        self.name = name
        self.hp = hp
        self.str = str

    def __str__(self):
        return f"{self.name} : Vie {self.hp}, Force {self.str}"