# library
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import os.path
import time
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium_stealth import stealth
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
#eof library

# options
variable = os.getcwd()
chrome_path = '/chromedriver/chromedriver-windows-x64.exe'
options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={variable}/tik-tok-test2")
options.add_argument("--start-maximized")
browser = webdriver.Chrome(options = options)
action = ActionChains(browser)
# eof options

# user-agent settings
stealth(browser,
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,'
                   ' like Gecko) Chrome/112.0.0.0 Safari/537.36',
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
# eof user-agent settings


browser.get("https://www.tiktok.com/upload?lang=en")
wait = WebDriverWait(browser, 10) # wait till loaded
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body"))) # waiting
iframe = browser.find_element(By.CSS_SELECTOR, 'iframe')
browser.switch_to.frame(iframe)
path = "C:/Users/user752/OneDrive/Desktop/work/vid.mp4"
file_input = browser.find_element(By.CSS_SELECTOR, 'input[type="file"]')
file_input.send_keys(path)
time.sleep(10)
browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div[7]/div[2]/button/div/div').click()
time.sleep(3500)
