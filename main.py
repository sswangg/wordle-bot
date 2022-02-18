from time import sleep
from datetime import date

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_word():
    today = date.today()
    cigar_day = date(2021, 6, 19)
    days_from_cigar_day = (today-cigar_day).days
    with open("words.txt", "r") as file:
        words = [s.strip() for s in file.readlines()]
    return words[days_from_cigar_day % 2309]


browser = webdriver.Chrome()
browser.get('https://www.powerlanguage.co.uk/wordle/')

document = browser.find_element(By.TAG_NAME, 'html')
document.click()

document.send_keys(get_word())
document.send_keys(Keys.ENTER)

sleep(5)

browser.quit()
