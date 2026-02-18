# Utilisation de Selenium Webdriver et d'un diver Brave

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Création du pilote WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://amazon.fr")

time.sleep(1)

# Accepter les cookies
driver.find_element(By.ID, "sp-cc-accept").click()

try:
    # Trouver la barre de recherche
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    # Effaccer ce qui est présent dans la barre de recherche
    search_box.clear()
    # Objet de notre recherche écriture dans la barre
    search_box.send_keys("Ordinateur fixe")
    # Effectue l'action de recherche
    search_box.send_keys(Keys.ENTER)

except Exception as e:
    assert False