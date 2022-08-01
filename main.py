from time import sleep
from datetime import date

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


def get_word():
    today = date.today()
    cigar_day = date(2021, 6, 19)
    days_from_cigar_day = (today-cigar_day).days
    with open("words.txt", "r") as file:
        words = [s.strip() for s in file.readlines()]
    return words[days_from_cigar_day % 2309]


service = ChromeService(executable_path=ChromeDriverManager().install())

browser = webdriver.Chrome(service=service)
browser.get('https://www.nytimes.com/games/wordle/index.html')

button = browser.find_element(By.CLASS_NAME, "Modal-module_closeIcon__b4z74")
button.click()

document = browser.find_element(By.TAG_NAME, 'html')
document.send_keys(get_word())
document.send_keys(Keys.ENTER)

sleep(5)

browser.quit()
