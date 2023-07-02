import unittest
from app import action_adversaire
from data import adversaires, characters


class TestActionAdversaire(unittest.TestCase):
    def test_action_adversaire(self):
        adversaire = 'Sally'
        personnage = 'boxeur'

        # Exécution de la fonction à tester
        resultat = action_adversaire(adversaire, personnage)

        # Vérification des résultats attendus
        if resultat.startswith(f"{adversaire} vous a attaqué"):
            # Vérification si l'attaque a été infligée
            self.assertLess(characters[personnage]['vie'], 100)
        elif resultat.startswith(f"{adversaire} a esquivé"):
            # Vérification si l'attaque a été esquivée
            self.assertEqual(characters[personnage]['vie'], 100)

if __name__ == '__main__':
    unittest.main()