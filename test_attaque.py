import unittest
from app import attaquer
from data import adversaires, characters

class TestAttaquer(unittest.TestCase):
    def test_attaquer(self):
        adversaire = 'Sally'
        personnage = 'boxeur'

        # Exécution de la fonction à tester
        resultat = attaquer(adversaire, personnage)

        # Vérification des résultats attendus
        self.assertTrue(resultat.startswith("Vous avez infligé 30 points de dégâts à Sally."))

        # Vérification des modifications dans les données d'adversaires
        self.assertEqual(adversaires[adversaire]['vie'], 70)

if __name__ == '__main__':
    unittest.main()