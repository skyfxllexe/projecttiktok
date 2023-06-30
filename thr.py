

from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import os.path
import time
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium_stealth import stealth
from selenium.webdriver.chrome.service import Service

url = ["https://tiktok.com", "https://youtube.com", "https://instagram.com"]


def func(browser: webdriver.Chrome, url: str) -> None:
    browser.get(url)

array = []

for link in url:
    
    browser = webdriver.Chrome(service=s, options= options)
    t = Thread(target= func, args = (browser, link))
    array.append([t, browser])


