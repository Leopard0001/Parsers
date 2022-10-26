from selenium import webdriver
import chromedriver_binary as chr
import time
from selenium.webdriver.common.by import By
import re

browser = webdriver.Chrome() #запуск браузера

browser.get("http://hh.ru")
search_input = browser.find_element(By.ID, "a11y-search-input") #находим поле запроса
search_input.send_keys("Junior Python") #вводим текст

search_button = browser.find_element(By.CSS_SELECTOR, '[data-qa="search-button"]')
search_button.click()

job_count = browser.find_element(By.CSS_SELECTOR,'[data-qa="vacancies-search-header"] h1') #заголовок с количеством вакансий
print(job_count.text)

count = re.sub(r"\D", "", job_count.text) # удалить выбранные символы \D-не являющиеся числом r-регулярные выражения
print(f"Found exactyle {count} jobs")


time.sleep(10)
browser.close()