# Importation des modules Selenium nécessaires
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from login import login
from const import g1,nomligne1
driver = webdriver.Chrome()
actions = ActionChains(driver)
#appeler fonction login
login(driver,"Farah@mail.com","Farah@@12345678")
#champ de produits
time.sleep(9)
# Accéder à la section Paramètre
xpath = "//div[contains(@id,'id-Paramètres') and contains(text(), 'Paramètre')]"
paramètre = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, xpath))
)
print(paramètre)
paramètre.click()
time.sleep(4)
# Accéder à la section Admin
xpath = "//div[contains(@id,'id-Admin') and contains(text(), 'Admin')]"
Admin = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, xpath))
)
print(Admin)
Admin.click()
time.sleep(7)
# Accéder à la section Catalogue
xpath = "//div[contains(@id,'id-Catalogues') and contains(text(), 'Catalogue')]"
catalogue = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, xpath))
)
print(catalogue)
catalogue.click()
time.sleep(4)
# Ajouter une variable au chemin d'URL
new_url = "https://beta.geoprod.com/gestion-produit"
# Naviguer vers la nouvelle URL
driver.get(new_url)
time.sleep(7)
# Cliquer sur le bouton "Ajouter"
driver.find_element(By.XPATH,"/html/body/app-root/app-admin-layout/div[1]/div[2]/div[1]/div/div/app-list-produit/div/div[1]/button").click()
time.sleep(9)
#remplir le formulaire produits
driver.find_element(By.NAME,"nom_produit").send_keys("produit1")
time.sleep(7)
driver.find_element(By.NAME,"code_bareme").send_keys("123455")
time.sleep(5)
# Attendre que l'élément input soit visible et cliquable
input_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "ng-autocomplete input[type='text']"))
)
# Effacer le contenu de l'input (s'il y a déjà du texte)
input_element.clear()
# Entrer du texte dans l'input
texte_a_saisir = "final test"
input_element.send_keys(texte_a_saisir)
time.sleep(5)
#cliquer sur l'option test final
#Attendre que la liste des suggestions soit visible
suggestions_container = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "ng-autocomplete .suggestions-container.is-visible"))
)

# Sélectionner le premier élément de la liste des suggestions
premier_element = suggestions_container.find_element(By.CSS_SELECTOR, "ul li.item:first-child")

# Maintenant, vous pouvez effectuer des actions sur cet élément, par exemple, cliquer dessus
premier_element.click()
#remplir input option
driver.find_element(By.NAME,"option").send_keys("option1")
time.sleep(7)
actions.send_keys(Keys.PAGE_DOWN).perform()
actions.send_keys(Keys.PAGE_DOWN).perform()
driver.find_element(By.NAME,"renfort").send_keys("Test")
time.sleep(8)
driver.find_element(By.NAME,"cotation_id").send_keys("test")
actions.send_keys(Keys.PAGE_UP).perform()
actions.send_keys(Keys.PAGE_UP).perform()
time.sleep(9)
#click information gamme
xpath = "//div[contains(@class,'mat-tab-label-content') and contains(text(), 'Informations Gamme')]"
info = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, xpath))
)
print(info)
info.click()
time.sleep(9)
#remplir la  compagnie
# Attendre que la page soit complètement chargée
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ng-autocomplete")))
# Sélectionner l'élément ng-autocomplete
autocomplete_element = driver.find_element(By.CSS_SELECTOR, "ng-autocomplete")
# Simuler un clic sur l'élément ng-autocomplete pour activer la zone de texte
autocomplete_element.click()
# Attendre que l'élément input devienne cliquable
input_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ng-autocomplete input[placeholder='Compagnie']")))

# Maintenant, vous pouvez effectuer des actions sur l'élément input, par exemple, remplir avec une valeur
input_element.send_keys("testing")
# Attendre que la liste des suggestions soit visible
suggestions_container1 = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "ng-autocomplete .suggestions-container.is-visible"))
)

# Sélectionner le premier élément de la liste des suggestions
premier_element = suggestions_container1.find_element(By.CSS_SELECTOR, "ul li.item:first-child")
# Maintenant, vous pouvez effectuer des actions sur cet élément, par exemple, cliquer dessus
premier_element.click()
time.sleep(8)
#remplir input gamme
# Attendre que la page soit complètement chargée
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ng-autocomplete")))
# Sélectionner l'élément ng-autocomplete
autocomplete_element_gamme = driver.find_element(By.CSS_SELECTOR, "ng-autocomplete")

# Simuler un clic sur l'élément ng-autocomplete pour activer la zone de texte
autocomplete_element_gamme.click()
# Attendre que l'élément input devienne cliquable
input_element_gamme = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ng-autocomplete input[placeholder='Gamme']")))
# Maintenant, vous pouvez effectuer des actions sur l'élément input, par exemple, remplir avec une valeur
input_element_gamme.send_keys("test")

# Attendre que la liste des suggestions soit visible
suggestions_container = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "ng-autocomplete .suggestions-container.is-visible"))
)
# Sélectionner le premier élément de la liste des suggestions
premier_element_gamme = suggestions_container.find_element(By.CSS_SELECTOR, "ul li.item:first-child")
# Maintenant, vous pouvez effectuer des actions sur cet élément, par exemple, cliquer dessus
premier_element_gamme.click()
time.sleep(8)
#click Enregistrer
xpath2 = "//button[contains(@class,'btn-dt-save') and contains(text(), 'Enregistrer')]"
enregistrer_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath2))
    )
    # Print information about the enregistrer_button
print(enregistrer_button)
    # Click the "Enregistrer" button
enregistrer_button.click()
time.sleep(5)
#cilck Liste des Produits
xpath = "//button[contains(@class,'swal2-confirm swal2-styled') and contains(text(), 'Liste des Produits')]"
liste = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    # Print information about the enregistrer_button
print(liste)
    # Click the "Enregistrer" button
liste.click()
time.sleep(5)
driver.quit()