from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_driver_path = "C:/Development/chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://practice.automationtesting.in/")

driver.quit()



