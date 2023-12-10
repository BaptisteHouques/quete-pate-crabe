import unittest
from app import FncDodge

class TestDodging(unittest.TestCase):
    def test_esquiver(self):
        # Exécution de la fonction à tester
        resultat = FncDodge()

        # Vérification des résultats attendus
        self.assertTrue(resultat in [True, False])

if __name__ == '__main__':
    unittest.main()