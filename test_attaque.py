import unittest
from app import FncAttack
from data import ennemies, characters

class TestAttacking(unittest.TestCase):
    def test_attaquer(self):
        ennemie = 'Sally'
        character = 'Boxer'

        # Exécution de la fonction à tester
        resultat = FncAttack(ennemie, character)

        # Vérification des résultats attendus
        self.assertTrue(resultat.startswith("Vous avez infligé 30 points de dégâts à Sally."))

        # Vérification des modifications dans les données d'adversaires
        self.assertEqual(ennemies[ennemie]['hp'], 70)

if __name__ == '__main__':
    unittest.main()