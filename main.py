from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from time import sleep

GAME_MINUTES = 5


def click_for_n_seconds(n: float = 5):
    global cookie
    start = datetime.now()
    while datetime.now() - start < timedelta(seconds=n):
        cookie.click()


def go_shopping():
    global driver, item_names
    for name in item_names:
        sleep(0.1)
        upgrade = driver.find_element(By.ID, name)
        if upgrade.get_attribute("class") != "grayed":
            upgrade.click()


def play_game():
    click_for_n_seconds(5)
    go_shopping()


item_names = [
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

# -------------game---------------
while datetime.now() - __start__ < timedelta(minutes=GAME_MINUTES):
    play_game()
# -------------game---------------

__end__ = datetime.now().time()
print("End:", __end__)
final_cookies = driver.find_element(By.ID, "money").text
print("\nFinal cookies:", final_cookies)
cps = driver.find_element(By.ID, "cps").text
print("Cookies/Second:", cps)

with open("scoreboard.txt", "a") as file:
    file.write(
        f"Start time: {__start__}\nEnd time: {__end__}\nCookies per second: {cps}\nCookies left: {final_cookies}\n\n")

driver.quit()
