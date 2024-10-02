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
def garantie_create(driver,code,nom):
    actions = ActionChains(driver)
    driver.find_element(By.ID,"code-garantie").send_keys(code)
    time.sleep(5)
    input_element = driver.find_element(By.ID,"nom-garantie")
    input_element.send_keys(nom)
    time.sleep(5)
    input2 = driver.find_element(By.ID,"valeur-min")
    input2.send_keys("50")
    time.sleep(4)
    input3 = driver.find_element(By.ID,"valeur-max")
    input3.send_keys("500")
    time.sleep(6)
    #driver.find_element(By.CLASS_NAME,"mat-select-placeholder").click()
    #time.sleep(10)
    xpath = "//span[ contains(@class, 'mat-select-placeholder')]"
    unite = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    print(unite)
    unite.click()
    time.sleep(5)
    # Wait for the "Enregistrer" button to be present (you might need to adjust the timeout)
    xpath = "//span[ contains(text(), 'EUR')]"
    unite_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    print(unite_button)
    unite_button.click()
    time.sleep(5)
    #driver.find_element(By.XPATH, "//*[@id='mat-option-2']/span").click()
    #time.sleep(5)
    #driver.find_element(By.ID,"icon-picker-search").send_keys("Ambulance")
    #time.sleep(4)
    driver.find_element(By.ID,"description" ).send_keys("testing1")
    time.sleep(5)
    # Scroller vers le haut de la page
    actions.send_keys(Keys.PAGE_UP).perform()
    actions.send_keys(Keys.PAGE_UP).perform()
    print("try")
    # Enregistrer garantie
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
            EC.element_to_be_clickable((By.XPATH, xpath1))
        )
        print(liste)
        liste.click()
        time.sleep(5)
    except TimeoutException:
        print("Timeout: Unable to locate the 'Listes des garanties ' button within the specified time.")
    finally:
        print("TRUE ")
    time.sleep(7)

