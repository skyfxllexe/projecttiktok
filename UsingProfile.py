from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium_stealth import stealth
from nickgenerator import CreateUsername
import os.path
import time
import random
import sqlite3
from threading import Thread
from selenium.webdriver.chrome.service import Service
user_agent_list = []
f = open("userPConly.txt")
for i in f:
    user_agent_list.append(i[:-1])

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

s=Service('/chromedriver-windows-x64.exe')
class User():
    def __init__(self, package, package_meta) -> None:
        self.login = package[0]
        self.password = package[1]
        self.ID = package[2]
        self.user_agent = package_meta[0]
        
        # self.user_agent = user_agent
        self.driver = webdriver.Chrome(service = s)
    
    def set_options(self)-> webdriver.ChromeOptions:
        options = webdriver.ChromeOptions()
        options.add_argument(f"user-data-dir={os.getcwd}/first_generation/{self.ID}")
        return options
    
    def set_stealh(self) -> None:
        stealth(self.driver,
                user_agent=self.user_agent,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )
    
    def enter_to_data_base(self) -> None:
        
        cur.execute(
            f'''
            INSERT INTO accounts(nickname, time, scheme, content_type, proxy, condition, cookie, is_alive, login, password, user_agent)
            VALUES('{self.login}', 1, 'emulation', 'porn', 'proxy_null', 'none', 'cookie_null', '1', '{self.login}', '{self.password}', '{self.user_agent}');
            '''
        )
        con.commit()
    
    def set_all(self) -> None:
        self.driver.options = self.set_options()
        self.set_stealh()
    
    
    def start_emulation(self) -> None:
        self.driver.get("https://tiktok.com")
        block = self.driver.find_elements(By.TAG_NAME, 'span')
        for i in block:
            if (i.get_attribute("class") == 'tiktok-j2a19r-SpanText efbd9f0'):
                time.sleep(2)
                i.click()
                break
        time.sleep(2)
        subscribe = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div/div[2]/div[1]/button')
        like = self.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[4]/div/div[2]/div[2]/div[3]/div[1]/div[1]/button[1]/span')
        for iterator in range(15):
            time.sleep(random.randint(2, 5))
            if iterator % 6 == 0:
                subscribe.click()
                time.sleep(2)
            elif iterator % 3 == 0:
                like.click()
            time.sleep(1)

    def authorize(self) -> None:
        self.driver.get("https://www.tiktok.com/login/phone-or-email/email")
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body"))) # waiting
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/form/div[1]/input').send_keys(self.login)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/form/div[2]/div/input').send_keys(self.password)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/form/button').click()
        time.sleep(100)
    
    def start_test(self) -> None:
        self.driver.get("https://tiktok.com")
        time.sleep(1000)

    def upload_video(self, path: str) -> None:
        self.driver.get("https://www.tiktok.com/upload?lang=en")
        wait = WebDriverWait(self.driver, 10) # wait till loaded
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body"))) # waiting
        iframe = self.driver.find_element(By.CSS_SELECTOR, 'iframe')
        self.driver.switch_to.frame(iframe)
        # path = "C:/Users/user752/OneDrive/Desktop/work/vid.mp4"
        file_input = self.driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
        file_input.send_keys(path)
        time.sleep(10)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div[7]/div[2]/button/div/div').click()
    
    def fill_video_info(self) -> None:
        ...
    
    def select_music(self) -> None:
        ...


def delete_from_DB(nick: str) -> None:
    cur.execute(f'DELETE FROM accounts WHERE nickname ="{nick}"')
    con.commit()


def clear_all_DB() -> None:
    cur.execute('DELETE FROM accounts')
    con.commit()

def goThread(objects: list) -> None:
    for object in objects:
        Thread(target=object.start_test()).start()


package_main_info = ["skyfxllexe", "Ghbphfr1#", "1"]
package_meta_info = [str(user_agent_list[random.randint(0,len(user_agent_list)-1)])]

account1 = User(package_main_info, package_meta_info)
# account2 = newUser(package_main_info, package_meta_info)
# arrayOfObjects = [account1, account2]


account1.set_all()
account1.start_test()