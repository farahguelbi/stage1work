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
from const import n1,g1,nomligne1
driver = webdriver.Chrome()
#appeler la fonction login
login(driver,"Farah@mail.com","Farah@@12345678")
#champ pour remplir la garantie
#Accéder à la section Paramètre
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
# Accéder à la section Garantie
xpath = "//div[contains(@id,'id-Garanties') and contains(text(), 'Garantie')]"
garantie = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, xpath))
)
print(garantie)
garantie.click()
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/app-root/app-admin-layout/div[1]/div[2]/div[1]/div/div/app-list-garanties/div/div[1]/button").click()
time.sleep(5)
#appeler fonction add_garantie
garantie_create(driver,g1,n1)
#champ du ligne de produits
# Sélectionner un élément par ID
driver.find_element(By.ID,"Groupe_638").click()
time.sleep(13)
#Accéder à la section Lignes des Produits
xpath= "//div[contains(@id,'id-LignesdesProduits') ]"
lp = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
print(lp)
lp.click()
time.sleep(4)
lp.click()
time.sleep(9)
# Cliquer sur le bouton "Ajouter"
driver.find_element(By.XPATH,"/html/body/app-root/app-admin-layout/div[1]/div[2]/div[1]/div/div/app-list-ligne-produit/div/div[1]/button").click()
time.sleep(20)
#remplir le formulaire ligne de produits
#remplir le Type
name=driver.find_element(By.NAME,"type")
name.send_keys(nomligne1)
time.sleep(9)
#remplir le cycle de vie
driver.find_element(By.NAME,"workflow").send_keys("en attente")
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/mat-option/span").click()
time.sleep(5)
#remplir le input de garantie
driver.find_element(By.ID,"id-select-garantie").send_keys("143")
driver.find_element(By.XPATH,"/html/body/app-root/app-admin-layout/div[1]/div[2]/div[1]/div/div/app-fiche-ligne-produit-affaire/div[2]/mat-tab-group/div/mat-tab-body[1]/div/div/div[1]/div[4]/div/mat-form-field/div/div[1]/div/input").send_keys("testing")
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
# Cliquer sur le bouton "Liste des Lignes des Produits"
xpath="//button[contains(@class,'swal2-cancel swal2-styled') and contains(text(),'Liste des Lignes des Produits')]"
liste_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    # Print information about the enregistrer_button
print(liste_button)
    # Click the "Enregistrer" button
liste_button.click()
time.sleep(15)
driver.quit()