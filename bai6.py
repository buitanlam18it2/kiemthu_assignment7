from selenium import webdriver
from selenium.webdriver.chrome.options import Options



chrome_driver_path = "C:/Development/chromedriver.exe"

chrome_options = Options()
chrome_options.add_argument("--window-size=900,900")

driver = webdriver.Chrome(chrome_driver_path,chrome_options=chrome_options)

driver.get("http://practice.automationtesting.in/")

print(driver.page_source)

driver.quit()