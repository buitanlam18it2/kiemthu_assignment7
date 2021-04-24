from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

import time




chrome_driver_path = "C:/Development/chromedriver.exe"

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(chrome_driver_path,chrome_options=chrome_options)
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-50").click()
driver.find_element_by_id("reg_email").send_keys("builam18it2@gmail.com")
element = driver.find_element_by_id('reg_password')
element.send_keys("Anh01232305898")

time.sleep(5)
driver.find_element_by_class_name('register').click()

driver.find_element_by_xpath('//*[@id="customer_login"]/div[2]/form/p[3]/input[3]').click()
time.sleep(5)

driver.quit()




