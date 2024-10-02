from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os

# Check if it's the first or second execution
is_first_execution = os.environ.get('IS_FIRST_EXECUTION', 'true').lower() == 'true'

# Use different values based on the execution
if is_first_execution:
    garantie = os.getenv(garantie1)
else:
    garantie = os.environ.get(GARANTIE_SECOND_EXECUTION)

# Rest of your code using garantie_value
driver.find_element(By.XPATH, "//*[@id='mat-input-2']").send_keys(garantie_value)
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='mat-input-3']").send_keys("med")
time.sleep(4)
driver.find_element(By.XPATH, "//*[@id='mat-input-4']").send_keys("50")
time.sleep(6)
driver.find_element(By.XPATH, "//*[@id='mat-input-5']").send_keys("500")
time.sleep(6)
driver.find_element(By.XPATH, "/html/body/app-root/app-admin-layout/div[1]/div[2]/div[1]/div/div/app-add-garantie/div[2]/div[3]/div/form/div/div[5]/div/mat-form-field/div/div[1]/div").click()
time.sleep(10)
driver.find_element(By.XPATH, "//*[@id='mat-option-2']/span").click()
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='mat-input-7']").send_keys("Ambulance")
time.sleep(4)
driver.find_element(By.XPATH, "//*[@id='mat-input-6']").send_keys("testing1")
time.sleep(5)
