"""from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
driver.find_element(By.XPATH,"//*[@id='mat-input-2']").send_keys(os.environ.get(garantie ))
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='mat-input-3']").send_keys("med")
time.sleep(4)
driver.find_element(By.XPATH,"//*[@id='mat-input-4']").send_keys("50")
time.sleep(6)
driver.find_element(By.XPATH,"//*[@id='mat-input-5']").send_keys("500")
time.sleep(6)
driver.find_element(By.XPATH,"/html/body/app-root/app-admin-layout/div[1]/div[2]/div[1]/div/div/app-add-garantie/div[2]/div[3]/div/form/div/div[5]/div/mat-form-field/div/div[1]/div").click()
time.sleep(10)
driver.find_element(By.XPATH,"//*[@id='mat-option-2']/span").click()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='mat-input-7']").send_keys("Ambulance")
time.sleep(4)
driver.find_element(By.XPATH,"//*[@id='mat-input-6']").send_keys("testing1")
time.sleep(5)"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os

def garantie_create(driver,code):
    # Rest of your code using garantie_value
    #import  pdb;pdb.set_trace();
    #driver.find_element(By.XPATH, "//*[@id='mat-input-2']").send_keys(code)
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"mat-input-element")))
    print(element)
    element.send_keys(code)
    time.sleep(8)
    """wait =  WebDriverWait(driver, 10)
    element1 = wait.until(
 EC.presence_of_element_located((By.XPATH, "//*[@id='mat-input-9' and contains(@class, 'mat-input-element')]"))
    )
    print(element1)
    time.sleep(6)
    #driver.find_element(By.ID,"mat-input-9").send_keys("med")
    input_element = driver.find_element(By.XPATH,"//input[@placeholder='Nom garantie']")
    input_element.send_keys("med")"""
    input_element = driver.find_element(By.ID,"nom-garantie")
    input_element.send_keys("med")
    time.sleep(5)
    input2 = driver.find_element(By.ID,"valeur-min")
    input2.send_keys("50")
    time.sleep(4)
    input3 = driver.find_element(By.ID,"valeur-max")
    input3.send_keys("500")
    time.sleep(6)
     #driver.find_element(By.XPATH, "/html/body/app-root/app-admin-layout/div[1]/div[2]/div[1]/div/div/app-add-garantie/div[2]/div[3]/div/form/div/div[5]/div/mat-form-field/div/div[1]/div").click()
    driver.find_element(By.ID,"unite").click()
    time.sleep(10)
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
    driver.quit()
