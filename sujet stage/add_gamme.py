# Importation des modules Selenium nécessaires
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
from login import login
from add_garantie import garantie_create
from const import nomgamme,g2,n2
driver = webdriver.Chrome()
actions = ActionChains(driver)
#appeler la fonction login
login(driver,"Farah@mail.com","Farah@@12345678")
#champ pour remplir une autre garantie
# Accéder à la section Paramètre
xpath = "//div[contains(@class,'Tableau_de_Bord_t') and contains(text(), 'Paramètre')]"
paramètre = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, xpath))
)
print(paramètre)
paramètre.click()
time.sleep(4)
# Accéder à la section Admin
xpath = "//div[contains(@class,'Tableau_de_Bord_t') and contains(text(), 'Admin')]"
Admin = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, xpath))
)
print(Admin)
Admin.click()
time.sleep(7)
# Accéder à la section Catalogue
xpath = "//div[contains(@class,'Tableau_de_Bord_t') and contains(text(), 'Catalogue')]"
catalogue = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, xpath))
)
print(catalogue)
catalogue.click()
time.sleep(4)
# Accéder à la section Garantie
xpath = "//div[contains(@class,'Tableau_de_Bord_t') and contains(text(), 'Garantie')]"
garantie = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, xpath))
)
print(garantie)
garantie.click()
time.sleep(5)
# Cliquer sur le bouton "Ajouter"
driver.find_element(By.XPATH,"/html/body/app-root/app-admin-layout/div[1]/div[2]/div[1]/div/div/app-list-garanties/div/div[1]/button").click()
time.sleep(5)
#appeler la fonction add_garantie
garantie_create(driver,g2,n2)
#champs pour gamme
# Sélectionner un élément par ID
driver.find_element(By.ID,"Groupe_637").click()
time.sleep(13)
# Accéder à la section "Gammes
xpath = "//div[contains(@class,'Tableau_de_Bord_t') and contains(text(), 'Gammes')]"
gamme = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, xpath))
)
print(gamme)
gamme.click()
time.sleep(10)
# Cliquer sur le bouton "Ajouter"
driver.find_element(By.XPATH,"/html/body/app-root/app-admin-layout/div[1]/div[2]/div[1]/div/div/app-gestion-gammes/div/div[1]/button").click()
time.sleep(6)
#remplir le formulaire GAMME
driver.find_element(By.NAME,"nom_gamme").send_keys(nomgamme)
time.sleep(6)
driver.find_element(By.NAME,"type").send_keys("final test")
time.sleep(6)
xpath = "//span[contains (@class,'mat-option-text') and contains(text(), ' final test ')]"
button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
print(button)
button.click()
time.sleep(5)
driver.find_element(By.NAME,"compagnie").send_keys("testing")
xpath = "//span[ contains(text(), ' testing ')]"
button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
print(button)
button.click()
time.sleep(6)
driver.find_element(By.NAME,"age_min").send_keys("18")
time.sleep(9)
driver.find_element(By.NAME,"age_max").send_keys("60")
time.sleep(5)
driver.find_element(By.NAME,"conditions_souscription").send_keys("testt")
time.sleep(8)
driver.find_element(By.NAME,"description").send_keys("testing")
time.sleep(8)
driver.find_element(By.NAME,"id_externe").send_keys("test1")
time.sleep(6)
driver.find_element(By.ID,"id-search-garantie" ).send_keys("03080")
time.sleep(2)
actions.send_keys(Keys.PAGE_DOWN).perform()
actions.send_keys(Keys.PAGE_DOWN).perform()
xpath = "//span[contains(@class,'mat-option-text') and contains(text(), ' med (03080) ')]"
select = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, xpath))
)
print(select)
select.click()
time.sleep(19)
driver.find_element(By.XPATH,"//*[@id='030800']/div/div[2]/div").click()
time.sleep(6)
xpath="//span [contains(@class,'mat-option-text') and contains(text(),'Hospitalistions')]"
select1 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, xpath))
)
print(select1)
select1.click()

"""# Attendre que la combobox soit chargée
wait = WebDriverWait(driver, 10)
combobox = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@role='combobox']")))

# Créer un objet Select pour interagir avec la combobox
select = Select(combobox)

# Sélectionner l'option par son texte visible
select.select_by_visible_text("Hospitalistions")"""
time.sleep(20)
actions.send_keys(Keys.PAGE_UP).perform()
actions.send_keys(Keys.PAGE_UP).perform()
time.sleep(4)
# Cliquer sur le bouton "enregistre" du liste des produits
xpath2 = "//button[contains(@class,'btn-dt-save') and contains(text(), 'Enregistrer')]"
enregistrer_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath2))
    )
    # Print information about the enregistrer_button
print(enregistrer_button)
    # Click the "Enregistrer" button
enregistrer_button.click()
time.sleep(5)
# Cliquer sur le bouton "Liste des Lignes des Gammes "
xpath="//button[contains(@class,'swal2-confirm swal2-styled') and contains(text(),'Liste des Gammes')]"
liste_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    # Print information about the enregistrer_button
print(liste_button)
    # Click the "Enregistrer" button
liste_button.click()
time.sleep(15)
driver.quit()
