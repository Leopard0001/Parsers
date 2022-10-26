import requests
from bs4 import BeautifulSoup

url = "https://live.skillbox.ru/"

htmlfile = requests.get(url)
soup = BeautifulSoup(htmlfile.content, "html.parser") #суп из элементов


links=soup.findAll(class_ = "webinars__item") #найти все ссылки
for link in links:
    item = link.find(class_ = "webinar-card")
    date = link.find(class_ = "webinar-card__date")

    print(f"{item}, {date}\n")


