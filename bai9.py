from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import *
from selenium.webdriver.support import expected_conditions as EC
import time




chrome_driver_path = "C:/Development/chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://itmscoaching.herokuapp.com/form")

time.sleep(3)

driver.find_element_by_id('first-name').send_keys("Binh")
driver.find_element_by_id('last-name').send_keys("Nguyen")
driver.find_element_by_id('job-title').send_keys("Tester")
driver.find_element_by_id('radio-button-3').click()
driver.find_element_by_id('checkbox-2').click()

year_of_ex = Select(driver.find_element_by_id('select-menu'))
year_of_ex.select_by_value('3')

driver.find_element_by_id('datepicker').send_keys("20/7/2011")

time.sleep(2)

submit = driver.find_element(By.XPATH,("/html/body/div/form/div/div[8]/a"))
submit.click()

time.sleep(3)
driver.quit()

