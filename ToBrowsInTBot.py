from selenium import webdriver
import chromedriver_binary as chr #иногда нужна для браузера, как правило после первого запуска остается в памяти и больше не нужен
from selenium.webdriver.common.by import By
import re
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters

def parse_hh(job_title):
    browser = webdriver.Chrome() #запуск браузера
    browser.get("http://hh.ru")

    search_input = browser.find_element(By.ID, "a11y-search-input") #находим поле запроса
    search_input.send_keys(job_title) #вводим текст

    search_button = browser.find_element(By.CSS_SELECTOR, '[data-qa="search-button"]')
    search_button.click()

    job_count = browser.find_element(By.CSS_SELECTOR,'[data-qa="vacancies-search-header"] h1') #заголовок с количеством вакансий

    count = re.sub(r"\D", "", job_count.text) # удалить выбранные символы \D-не являющиеся числом r-регулярные выражения

    browser.close()
    return count

app = ApplicationBuilder().token("Your token").build()

async def text_reply(upd: Update, _ctx): #вызывается при получении сообщения
    user_text = upd.message.text
    print(f"User: {user_text}")
    name = upd.message.from_user.full_name
    jobs_count = parse_hh(user_text)
    await upd.message.reply_text(f"Найденно вакансий: {jobs_count}")


hendler = MessageHandler(filters.TEXT, text_reply)
#MessageHandler - для сообщений (текстовые, аудио, анимации, стикеры)
#CommandHandler - для комманд (типа /hello /start)

app.add_handler(hendler) #прикрепляем обработчик к приложению

app.run_polling() #запускаем приложение
