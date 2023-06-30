from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os.path
import time
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium_stealth import stealth




user_agent_list = []
f = open("userPConly.txt")
for i in f:
    user_agent_list.append(i[:-1])
variable = os.getcwd()

def set_options(acc_id: str, proxy_server_url = 0) -> webdriver.ChromeOptions:
    variable = os.getcwd()
    chrome_path = '/chromedriver/chromedriver-windows-x64.exe'
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-data-dir={variable}/first_generation/{acc_id}")
    options.add_argument("--mute-audio")
    if proxy_server_url != 0:
        options.add_argument(f'--proxy-server={proxy_server_url}')
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


options = set_options(1)

driver = webdriver.Chrome(options=options)
set_stealh(driver, user_agent_list)

driver.get("https://tiktok.com")
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[1]/div/div[3]/button'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div[3]/div/div/div[1]/div[3]/a'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div[3]/div/div/div[1]/div[1]/div/div/div[2]/a'))).click()
time.sleep(2000)

month_dict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}
day = 0
year = random.randint(1997, 2002)
month_num = random.randint(1,12)
month = month_dict[month_num]
day = random.randint(1, 30 + (month_num % 2 != 0 and month != 2) - (month==2))
