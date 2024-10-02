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
"""driver = webdriver.Chrome()
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
time.sleep(10)"""
def login(driver,email,password):
    actions = ActionChains(driver)
    # Naviguer vers la page web
    driver.get("https://beta.geoprod.com/")
    driver.maximize_window()
    # Scroller vers le bas de la page
    actions.send_keys(Keys.PAGE_DOWN).perform()
    actions.send_keys(Keys.PAGE_DOWN).perform()
    # Remplir le formulaire de login
    # entrer email
    driver.find_element(By.XPATH, "//*[@id='mat-input-0']").send_keys(email)
    time.sleep(2)
    # entrer password
    driver.find_element(By.XPATH, "//*[@id='mat-input-1']").send_keys(password)
    time.sleep(8)
    # cliquer connection
    driver.find_element(By.XPATH, "//*[@id='login-form']/form/button").click()
    time.sleep(6)



