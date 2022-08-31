import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
from time import sleep


def click_for_n_seconds(n: float = 5):
    global cookie
    start = datetime.now()
    while datetime.now() - start < timedelta(seconds=n):
        cookie.click()


def go_shopping():
    global driver
    money = driver.find_element(By.ID, "money").text


def play_game():
    click_for_n_seconds(5)
    go_shopping()


shopping_list = [
    "buyTime machine",
    "buyPortal",
    "buyAlchemy lab",
    "buyShipment",
    "buyMine",
    "buyFactory",
    "buyGrandma",
    "buyCursor"
]
service = Service(r"C:\Users\Maciek\Programming\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")

sleep(2)
notification = driver.find_element(By.CLASS_NAME, "cc_btn_accept_all")
notification.click()
sleep(1)

__start__ = datetime.now()
print("\nStart:", __start__.time())
while datetime.now() - __start__ < timedelta(seconds=5):
    play_game()
print("End:", datetime.now().time())
print("\nFinal cookies:",driver.find_element(By.ID, "money").text)
print("Cookies/Second:",driver.find_element(By.ID, "cps").text)

driver.quit()
