import unittest
from app import FncActionEnnemie
from data import ennemies, characters


class TestActionEnnemie(unittest.TestCase):
    def test_action_adversaire(self):
        ennemie = 'Sally'
        character = 'Boxer'

        # Exécution de la fonction à tester
        result = FncActionEnnemie(ennemie, character)

        # Vérification des résultats attendus
        if result.startswith(f"{ennemie} vous a attaqué"):
            # Vérification si l'attaque a été infligée
            self.assertLess(characters[character]['hp'], 100)
        elif result.startswith(f"{ennemie} a esquivé"):
            # Vérification si l'attaque a été esquivée
            self.assertEqual(characters[character]['hp'], 100)

if __name__ == '__main__':
    unittest.main()