from selenium import webdriver
from selenium.webdriver.chrome.options import Options



chrome_driver_path = "C:/Development/chromedriver.exe"

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(chrome_driver_path,chrome_options=chrome_options)

driver.get("http://practice.automationtesting.in/")

print(driver.current_url)

driver.quit()