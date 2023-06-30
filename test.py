from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=46.232.13.163:8000")
driver = webdriver.Chrome(service=Service("C:/Users/user752/OneDrive/Desktop/work/chromedriver-windows-x64.exe"), options=options)

driver.get("https://ria.ru")
time.sleep(5000)