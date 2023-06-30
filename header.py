from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import os.path
import time
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium_stealth import stealth

user_agent_list = []
f = open("useragents.txt")
for i in f:
    user_agent_list.append(i[:-1])
variable = os.getcwd()

def set_options(acc_id: str) -> webdriver.ChromeOptions:
    variable = os.getcwd()
    chrome_path = '/chromedriver/chromedriver-windows-x64.exe'
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-data-dir={variable}/first_generation/{acc_id}")
    return options

def set_stealh(driver: webdriver, user_agent: list) -> None:
    stealth(driver,
        user_agent=str(user_agent[random.randint(0,len(user_agent)-1)]),
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
    
    # eof user-agent settings