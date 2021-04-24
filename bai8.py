from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time




chrome_driver_path = "C:/Development/chromedriver.exe"

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(chrome_driver_path,chrome_options=chrome_options)
driver.get("https://the-internet.herokuapp.com/")

time.sleep(2)

driver.find_element_by_xpath('//*[@id="content"]/ul/li[21]/a').click()
driver.find_element_by_id('username').send_keys("tomsmith")
driver.find_element_by_id('password').send_keys("SuperSecretPassword!")

login = driver.find_element(By.XPATH,("/html/body/div[2]/div/div/form/button"))
login.click()
print(driver.title)
time.sleep(2)
driver.quit()

