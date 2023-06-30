from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import os.path
import time
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium_stealth import stealth
variable = os.getcwd()
chrome_path = '/chromedriver/chromedriver-windows-x64.exe'
options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={variable}/tik-tok-test2")
options.add_argument("--start-maximized")
browser = webdriver.Chrome(options=options)
action = ActionChains(browser)
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
browser.get("https://tiktok.com")
time.sleep(1)
block = browser.find_elements(By.TAG_NAME, 'span')
for i in block:
    if (i.get_attribute("class") == 'tiktok-j2a19r-SpanText efbd9f0'):
        time.sleep(2)
        i.click()
        break
html = browser.find_element(By.TAG_NAME, 'body')
time.sleep(2)
subscribe = browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div/div[2]/div[1]/button')
report = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[4]/div/div[1]/div[5]')
like = browser.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[4]/div/div[2]/div[2]/div[3]/div[1]/div[1]/button[1]/span')
for iterator in range(15):
    time.sleep(random.randint(2, 5))
    if iterator % 6 == 0:
        subscribe.click()
        time.sleep(2)
    elif iterator % 3 == 0:
        like.click()
    time.sleep(1)

    html.send_keys(Keys.DOWN)
time.sleep(3000)