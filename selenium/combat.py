import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class TestCombat(unittest.TestCase):
    def setUp(self):
        # Options pour exécuter Chrome en mode headless (sans ouvrir une fenêtre de navigateur)
        options = ChromeOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)

    def tearDown(self):
        self.driver.quit()

    def test_redirect_to_combat(self):
        # Va sur la page d'accueil
        self.driver.get("http://localhost:5000")

        # Sélectionne le premier personnage dans la liste déroulante
        select_personnage = Select(self.driver.find_element(By.ID, "personnage"))
        select_personnage.select_by_index(0)

        # Clique sur le bouton "Commencer le combat"
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        submit_button.click()

        # Vérifie si on est bien redirigé vers la page de combat
        self.assertIn("/combat", self.driver.current_url)

    def test_attack(self):
        # Va sur la page d'accueil
        self.driver.get("http://localhost:5000")

        # Sélectionne le premier personnage dans la liste déroulante
        select_personnage = Select(self.driver.find_element(By.ID, "personnage"))
        select_personnage.select_by_index(0)

        # Clique sur le bouton "Commencer le combat"
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        submit_button.click()

        # Clique sur le bouton "Attaquer"
        attack_button = self.driver.find_element(By.CSS_SELECTOR, "input[value='Attaquer']")
        attack_button.click()

        # Vérifie si le message d'attaque s'affiche bien
        message = self.driver.find_element(By.CSS_SELECTOR, "p").text
        self.assertIn("Vous avez infligé", message)

    def test_dodge(self):
        # Va sur la page d'accueil
        self.driver.get("http://localhost:5000")

        # Sélectionne le premier personnage dans la liste déroulante
        select_personnage = Select(self.driver.find_element(By.ID, "personnage"))
        select_personnage.select_by_index(0)

        # Clique sur le bouton "Commencer le combat"
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        submit_button.click()

        # Clique sur le bouton "Esquiver"
        dodge_button = self.driver.find_element(By.CSS_SELECTOR, "input[value='Esquiver']")
        dodge_button.click()

        # Vérifie si le message d'esquive contient la bonne phrase
        message = self.driver.find_element(By.CSS_SELECTOR, "#message").text
        self.assertIn("a esquivé votre attaque", message)



if __name__ == "__main__":
    unittest.main()
