# FrontEnd (в браузере) <= HTTP => Backend (на сервере)
# STATUS CODE (404, 200, 300, 400, 500)
# HEADERS + BODY
# HEADERS = СЛУЖЕБНАЯ ИНФОРМАЦИЯ
# BODY = пользовательская информация
# HTTP METHOD - тип запроса
# GET - получение данных
# POST - обновление данных

'''
import requests

# Создаем функцию для HTTP запросов
# Что нужно знать? URL, params={ HEADERS, BODY, METHOD }
def fetch(url, params):
    headers = params["headers"]
    body = params["body"]
    method = params["method"]
    if method == "POST":
        return requests.post(url, headers=headers, data=body)
    if method == "GET":
        return requests.get(url, headers=headers)




amulets = fetch("https://auto.ru/-/ajax/desktop/listing/", {
  "headers": {
    "accept": "*/*",
    "accept-language": "en,ru;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "same-origin",
    "sec-fetch-site": "same-origin",
    "x-client-app-version": "174.0.10149016",
    "x-client-date": "1665512127941",
    "x-csrf-token": "9fbf73a9e0920f1257c10d02b30351ca8674e7f6ee98ff56",
    "x-page-request-id": "0496979788b6af30141408ec261da764",
    "x-requested-with": "XMLHttpRequest",
    "x-retpath-y": "https://auto.ru/cars/chery/amulet/all/",
    "x-yafp": "{\"a1\":\"hJ0Jxg==;0\",\"a2\":\"fjiD0DfABXvjgLPAUVdm1DhMgCvm2g==;1\",\"a3\":\"l5qhF5PyQMX0A8mx0jNWcQ==;2\",\"a4\":\"g0UpJ2nc/JHJKA==;3\",\"a5\":\"hj6bO/Th+STR0w==;4\",\"a6\":\"UiE=;5\",\"a7\":\"mb61YJzTJYEYlg==;6\",\"a8\":\"oPulSPztot0=;7\",\"a9\":\"b59wUBcWZnN3uA==;8\",\"b1\":\"6T2xcKQ6PW4=;9\",\"b2\":\"TkCyYGgEm8kbTw==;10\",\"b3\":\"W3S9w9utxKS5Jg==;11\",\"b4\":\"GGyvDOVNLdA=;12\",\"b5\":\"1C+E1Gp0EJlgVg==;13\",\"b6\":\"gfHSqDMjL/bBdQ==;14\",\"b7\":\"r2XIofXtR6vxzQ==;15\",\"b8\":\"X+8LXdC9eDbDZg==;16\",\"b9\":\"fOfIjH8T2//kpQ==;17\",\"c1\":\"kLXJ3w==;18\",\"c2\":\"o6VobTp27FfXTyi+bzK4gg==;19\",\"c3\":\"38podf7YcUINybTtWRC6CQ==;20\",\"c4\":\"F+yuQLmXUcw=;21\",\"c5\":\"5XcCK7LktN0=;22\",\"c6\":\"JOMQFA==;23\",\"c7\":\"Jd9/Y13FWjo=;24\",\"c8\":\"d8o=;25\",\"c9\":\"znWnC+Bc4xQ=;26\",\"d1\":\"bUuRNlKLFxk=;27\",\"d2\":\"Jxw=;28\",\"d3\":\"iwUSsZvbk9a8HA==;29\",\"d4\":\"jGBfahOalyg=;30\",\"d5\":\"2NQDQQl6qkM=;31\",\"d7\":\"aQ8=;32\",\"d8\":\"8LESb+ZncAI0bM9BDsHuauZTZol1liJ6CXI=;33\",\"d9\":\"w9iakWzvVho=;34\",\"e1\":\"x1HVuDy8Lkdd/w==;35\",\"e2\":\"TIu291xZ7Ew=;36\",\"e3\":\"lfUoIVXsI1M=;37\",\"e4\":\"ZaedY+Qyxms=;38\",\"e5\":\"gy3zS1akF0+r7Q==;39\",\"e6\":\"cH4CnRh2r2M=;40\",\"e7\":\"bron+CT+fBi6FA==;41\",\"e8\":\"RyLLs47imW8=;42\",\"e9\":\"KxNuDTBdKAI=;43\",\"f1\":\"CBhVFIBwmNpaew==;44\",\"f2\":\"/rdPRq2GBzU=;45\",\"f3\":\"bwpNG7DhUVEEnQ==;46\",\"f4\":\"pgzD12gXcjI=;47\",\"f5\":\"w0HvDhKMMeQLrw==;48\",\"f6\":\"f0KTMJzGMuDuBA==;49\",\"f7\":\"AHe/L3MChy+tww==;50\",\"f8\":\"jRNM5Ix0ebcMuQ==;51\",\"f9\":\"m1U/pSivFvM=;52\",\"g1\":\"+Aep/BIpNpn9Gg==;53\",\"g2\":\"LINDaOeBEVVkRw==;54\",\"g3\":\"05IgEHVKQn0=;55\",\"g4\":\"s1U5pgTX+NgGJA==;56\",\"g5\":\"VwQZQ8hdWUE=;57\",\"g6\":\"dI9fifqOOaA=;58\",\"g7\":\"JzbWhr4+DeM=;59\",\"g8\":\"P3FffzvdY3w=;60\",\"g9\":\"f2qgCFUpAD8=;61\",\"h1\":\"xLx+YnM/5KfIVw==;62\",\"h2\":\"sbEB9xaox/lZkw==;63\",\"h3\":\"4sTr3Q2yOHgQsw==;64\",\"h4\":\"HYpRnYkjR7WwBQ==;65\",\"h5\":\"tCx9Yf99waQ=;66\",\"h6\":\"rAZD2yxdEqei9w==;67\",\"h7\":\"sAOYRyE+iWjX1tFaHz4OX9hrdFgf7oNU+a4mk986nnBrnack;68\",\"h8\":\"aCmf67fyI7P64A==;69\",\"h9\":\"rvD/ZRE/Stj+mA==;70\",\"i1\":\"6wEZ0yR/ieU=;71\",\"i2\":\"aP3CNgmna3oKNw==;72\",\"i3\":\"9sEBGephYRXfMg==;73\",\"i4\":\"SKd/puDeeTBA9Q==;74\",\"i5\":\"tz3e5aJacNaKhQ==;75\",\"z1\":\"HuagcV1PHUhCvo4XKHIUcMFiYEB2HLkcXcXD3jQmRHtUuphvQnUDYkT/05Z64XSpEB14wh91VRNSfKsf4agOZw==;76\",\"z2\":\"TY+Ogm3oyxwHc1Scl5SHzF46gGEhQMGywRck3mhXoJVVR+Ux8pSbQaI7VBqEfxYVrwjQEywP3rekJ1kCbN5aJQ==;77\",\"y2\":\"cDaPm44Dhou/zg==;78\",\"y3\":\"NMuMa7rmCtwygA==;79\",\"y6\":\"LAS6r75Sr32/GQ==;80\",\"y8\":\"NC9bRbrF/oyDmw==;81\",\"x4\":\"CLNn26owDNWzTg==;82\",\"z5\":\"2gSrXBIB/sw=;83\",\"z4\":\"nOaQsgd3xSCPQQ==;84\",\"z6\":\"VrNM4wibfm7LKGbh;85\",\"z7\":\"oyvVIwMa+Hy3nGWi;86\",\"z8\":\"w/HxLOuJXAL5F+iQzv4=;87\",\"z9\":\"PIEhkcnfXeZyFADQ;88\",\"y1\":\"oaj3bJRnsIFyOCKJ;89\",\"y4\":\"x7xBOROA4G2+FEkI;90\",\"y5\":\"/Qn2u2WAjvEbYKaCS3Q=;91\",\"y7\":\"ZhCvsxknzPF0S/Uo;92\",\"y9\":\"N82jZzMKEE7KQEJPVmQ=;93\",\"y10\":\"ZfDn3v2LWqjRsiUGTVQ=;94\",\"x1\":\"MZwgjZhNJ519jAU6;95\",\"x2\":\"fi++guvyRJKbQfzTAZ8=;96\",\"x3\":\"0BERXkTgFO3l7VtG;97\",\"x5\":\"676L4pWZvFxZjDll;98\",\"z3\":\"9flxkhIUI5+8IKtMjnR34TEOPdKFWNx/Bk4Q8ANXqyY=;99\",\"v\":\"6.3.1\",\"pgrdt\":\"CGvwa8LJccKIr5zVSIktscz61Gg=;100\",\"pgrd\":\"OjlIpQGIq3z43cjk31zxFi8x+7mssXgFkOu4x1G8G4gj4Z82/m+irDaqflIAU4I9HVqMaf1Rs0abxyGtpJhQeZZ7wqf1sSInfq3PtQNA21P7aB6k2qrD1om1SdIR3G+lFaB6g040alR6HFjyRqcU+xLzPa0elvwHxObBPuIe66VdmX6b+uA1TcaItPPSjGWySXVC8skoyTTqoZFs3N8MuYYOZb4=\"}",
    "cookie": "_csrf_token=9fbf73a9e0920f1257c10d02b30351ca8674e7f6ee98ff56; autoru_gdpr=1; suid=85f19f0b88f068335ba14eba3f5e3435.14c9674db7da17f1988676e377b9dc01; from=direct; yandex_login=mike.ovc; gdpr=0; _ym_uid=1645564389770852331; i=W3pN8VedXKw9z/zUZuNtX9crMdBXBkObKZYvjxTIKwCymxxNTPxqI+y7X8XtWcHbLtC+mY8IX+xDWEk3oIGp5yFgIMQ=; autoruuid=g6337310c2tardre4d9t5ucf84easarv.7776dc5fa119e1e595ddbeae3eec6b40; yandexuid=6280271851523913546; my=YwA%3D; los=1; bltsr=1; yuidlt=1; autoru_sid=a%3Ag6337310c2tardre4d9t5ucf84easarv.7776dc5fa119e1e595ddbeae3eec6b40%7C1665511924974.604800.nXbEq8bUyLhAf43F3Szmeg.5aJcdoesiNkm_PV9bysya6bq_y4PNxy4w5ufayggo10; crookie=+gZA1m1OI7Hj+AUpbbYMBfOiTOTH5XshkEAJ/kfqGpz7NKiC+9UD/6nZZP3NcWrlP/VgSOzn7hyt9soOXKE1Z5HDtts=; cmtchd=MTY2NTUxMTkyNzU3MQ==; _ym_isad=1; Session_id=3:1665511927.5.0.1610028951543:Y0DWUY4Md_wArzqJAEsBKg:32.1.2:1|348690723.-1.2.0:3.1:63090147|61:10008043.834992.K39B9R6GeKm_qe8XX3loXzLDGxk; ys=udn.cDrQnNC40YXQsNC40Lsg0J7QstGH0LjQvdC90LjQutC%2B0LI%3D#c_chck.1019850766; mda2_beacon=1665511927045; sso_status=sso.passport.yandex.ru:synchronized; _yasc=5qKbxNsmm06O27PaYqZ5mcIQ5VUcb2YKiWEwhDn9WHWlZA4H; _ym_visorc=b; listing_view_session={}; spravka=dD0xNjY1NTEyMDY4O2k9MmEwMTo0YjAwOmE4NWY6ODgwMDpmYzc3OmM4ZTo1MWQ2OjQwNjM7RD1GMkI1QkUzRjIxRUY4RjJFMThDOEQ3MzBDNDJGMERFOTczMTQwODI0MjJEQTFGMTY3NEM1QzEzMEQzOTJEOEY1RjQ0OTlBQTQ7dT0xNjY1NTEyMDY4Mzk2OTgwMTc5O2g9ZjcwMzU2N2QwZWYxZGEzYmQ0YzE0MWViZTk0YTA0MmE=; listing_view=%7B%22output_type%22%3A%22carousel%22%2C%22version%22%3A1%7D; layout-config={\"win_width\":888.148193359375,\"win_height\":954.8148803710938}; from_lifetime=1665512072940; _ym_d=1665512076",
    "Referer": "https://auto.ru/cars/chery/amulet/all/",
    "Referrer-Policy": "no-referrer-when-downgrade"
  },
  "body": "{\"catalog_filter\":[{\"mark\":\"CHERY\",\"model\":\"AMULET\"}],\"section\":\"all\",\"category\":\"cars\",\"output_type\":\"carousel\"}",
  "method": "POST"
})


amulets.status_code
200

# Заголовки ответа:
amulets.headers["Content-Type"]
application/json; charset=utf-8


offers = amulets.json()["offers"]
len(offers)
37


for offer in offers:
    price = offer["price_info"]["USD"]
    name = offer["vehicle_info"]["model_info"]["name"]
    mileage = offer["state"]["mileage"]
    print(f"Найден {name} всего за ${price}, пробег всего {mileage} км")
'''



import requests
from bs4 import BeautifulSoup
import json

# datafile = open("anscombe.json", "r", encoding="utf-8")
# data = json.load(datafile)
# for seria in data:
#     print(seria["Series"])

url = "https://live.skillbox.ru/"

htmlfile = requests.get(url)
soup = BeautifulSoup(htmlfile.content, "html.parser") #суп из элементов

#soup.findAll("селектор")
#soup.findAll("a") #найти все ссылки
#soup.findAll("button") # найти все кнопки
links=soup.findAll(class_ = "webinars__item") #найти все ссылки
for link in links:
    item = link.find(class_ = "webinar-card")
    date = link.find(class_ = "webinar-card__date")
    #print(link.string.strip())
    #print(link.get("href"))
    print(f"Вебинар {item} прошел {date};\n")
#print(links)
































