# Importation des modules Selenium nécessaires
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import subprocess
from formulaire import garantie_create
#from const import g1
# Création d'une instance de webdriver (utilisez le driver approprié pour votre navigateur)
driver = webdriver.Chrome()
actions = ActionChains(driver)
# Naviguer vers la page web
driver.get("https://beta.geoprod.com/")
driver.maximize_window()
# Scroller vers le bas de la page
actions.send_keys(Keys.PAGE_DOWN).perform()
actions.send_keys(Keys.PAGE_DOWN).perform()
# Remplir le formulaire de login
#entrer email
driver.find_element(By.XPATH,"//*[@id='mat-input-0']").send_keys("Farah@mail.com")
time.sleep(2)
#entrer password
driver.find_element(By.XPATH,"//*[@id='mat-input-1']").send_keys("Farah@@12345678")
time.sleep(8)
#cliquer connection
driver.find_element(By.XPATH,"//*[@id='login-form']/form/button").click()
time.sleep(10)
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
# Exécuter un autre fichier (formulaire.py)
xpath= "//*[@id='mat-input-2']"
garantie_create(driver,"33G1K0")
# Scroller vers le haut de la page
actions.send_keys(Keys.PAGE_UP).perform()
actions.send_keys(Keys.PAGE_UP).perform()
print("try")
#Enregistrer garantie
try:
    # Wait for the "Enregistrer" button to be present (you might need to adjust the timeout)
    xpath = "//button[contains(@class,'btn-dt-save') and contains(text(), 'Enregistrer')]"
    enregistrer_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    # Print information about the enregistrer_button
    print(enregistrer_button)
    # Click the "Enregistrer" button
    enregistrer_button.click()
    time.sleep(5)
except TimeoutException:
    print("Timeout: Unable to locate the 'Enregistrer' button within the specified time.")

finally:
    # Close the webdriver

    print("Close the webdriver")
time.sleep(7)
# Cliquer sur le bouton "Liste des garanties"
try:
       xpath1 = "//button[contains(@class,'swal2-confirm swal2-styled') ]"

       liste = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,xpath1))
   )
       print(liste)
       liste.click()
       time.sleep(5)
except TimeoutException:
    print("Timeout: Unable to locate the 'Listes des garanties ' button within the specified time.")
finally:
    print("TRUE ")
time.sleep(17)
# Sélectionner un élément par ID
driver.find_element(By.ID,"Groupe_638").click()
time.sleep(13)
# Accéder à la section "Lignes des Produits"
xpath= "//div[contains(@class,'Tableau_de_Bord_t_not_active') and contains(text(),'Lignes des Produits')]"
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
# Remplir le formulaire de la ligne de produit
#remplir le Type
name=driver.find_element(By.XPATH,'/html/body/app-root/app-admin-layout/div[1]/div[2]/div[1]/div/div/app-fiche-ligne-produit-affaire/div[2]/mat-tab-group/div/mat-tab-body[1]/div/div/div[1]/div[1]/div/mat-form-field/div/div[1]/div/input')
name.send_keys("Santé")
time.sleep(9)
#remplir le cycle de vie
driver.find_element(By.XPATH,"/html/body/app-root/app-admin-layout/div[1]/div[2]/div[1]/div/div/app-fiche-ligne-produit-affaire/div[2]/mat-tab-group/div/mat-tab-body[1]/div/div/div[1]/div[2]/div/mat-form-field/div/div[1]/div/input").send_keys("en attente")
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/mat-option/span").click()
time.sleep(5)
#remplir le input de garantie
driver.find_element(By.XPATH,"/html/body/app-root/app-admin-layout/div[1]/div[2]/div[1]/div/div/app-fiche-ligne-produit-affaire/div[2]/mat-tab-group/div/mat-tab-body[1]/div/div/div[1]/div[3]/div/mat-form-field/div/div[1]/div/mat-chip-list/div/input").send_keys("143")
driver.find_element(By.XPATH,"/html/body/app-root/app-admin-layout/div[1]/div[2]/div[1]/div/div/app-fiche-ligne-produit-affaire/div[2]/mat-tab-group/div/mat-tab-body[1]/div/div/div[1]/div[4]/div/mat-form-field/div/div[1]/div/input").send_keys("testing")
# Cliquer sur le bouton "enregistre" du garanties
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
#path to garantie
driver.find_element(By.XPATH,"//*[@id='Rectangle_64']").click()
time.sleep(9)
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
# Exécuter un autre fichier (formulaire.py)
xpath=   " // *[ @ id = 'mat-input-12']"
garantie_create(driver,"knFF215")
time.sleep(6)
# Cliquer sur le bouton "enregistre" du garanties
xpath2 = "//button[contains(@class,'btn-dt-save') and contains(text(), 'Enregistrer')]"
enregistrer_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath2))
    )
    # Print information about the enregistrer_button
print(enregistrer_button)
    # Click the "Enregistrer" button
enregistrer_button.click()
time.sleep(8)
try:
       xpath1 = "//button[contains(@class,'swal2-confirm swal2-styled') ]"

       liste = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,xpath1))
   )
       print(liste)
       liste.click()
       time.sleep(5)
except TimeoutException:
    print("Timeout: Unable to locate the 'Listes des garanties ' button within the specified time.")
finally:
    print("TRUE ")
time.sleep(17)
# Sélectionner un élément par ID
driver.find_element(By.ID,"Groupe_638").click()
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
#remplir le formulaire GAMME

driver.find_element(By.NAME,"nom_gamme").send_keys("test")
time.sleep(6)
driver.find_element(By.NAME,"type").send_keys("santé")
time.sleep(6)
xpath = "//span[ contains(text(), ' Santé ')]"
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
driver.find_element(By.XPATH,"id_externe").send_keys("test1")
time.sleep(6)
driver.find_element(By.XPATH,"//*[@id='mat-input-15']").send_keys("TesT")
time.sleep(5)
#click enregistrer_button
xpath2 = "//button[contains(@class,'btn-dt-save') and contains(text(), 'Enregistrer')]"
enregistrer_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath2))
    )
    # Print information about the enregistrer_button
print(enregistrer_button)
    # Click the "Enregistrer" button
enregistrer_button.click()
time.sleep(5)
#click liste des Gammes 
xpath2 = "//button[contains(@class,'swal2-confirm swal2-styled') and contains(text(), 'Liste des Gammes')]"
liste = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath2))
    )
print(liste)
liste.click()
time.sleep(5)
#path to produits
#click Produits
xpath = "//div[contains(@class,'Tableau_de_Bord_t') and contains(text(), 'Produits')]"
produits  = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, xpath))
)
print(produits)
produits.click()
time.sleep(10)
#remplir le formulaire produits 
driver.find_element(By.XPATH,"//*[@id='mat-input-92']").send_keys("produit1")
driver.find_element(By.XPATH,"//*[@id='mat-input-93']").send_keys("123455")
driver.find_element(By.XPATH,"//*[@id='mat-tab-content-8-0']/div/div/div[1]/div[4]/div/ng-autocomplete/div[1]/div[1]/input").send_keys("Santé")
driver.find_element(By.XPATH,"//*[@id='mat-tab-content-8-0']/div/div/div[1]/div[4]/div/ng-autocomplete/div[1]/div[2]/ul/li[5]/div/a").click()
driver.find_element(By.XPATH,"//*[@id='mat-input-110']").send_keys("option1")
driver.find_element(By.XPATH,"//*[@id='mat-input-111']").send_keys("Test")
driver.find_element(By.XPATH,"//*[@id='mat-input-112']").send_keys("test")
#click information gamme
driver.find_element(By.XPATH,"//*[@id='mat-tab-label-9-1']/div").click()
#remplir la  gamme
driver.find_element(By.XPATH,"//*[@id='mat-tab-content-9-1']/div/div/div[1]/div[1]/div/ng-autocomplete/div/div[1]/input").send_keys("testing")
driver.find_element(By.XPATH,"//*[@id='mat-tab-content-9-1']/div/div/div[2]/div/div/div/ng-autocomplete/div/div[1]/input").send_keys("test")
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



















