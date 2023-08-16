from bs4 import BeautifulSoup
import requests

from item import Item

url_m = 'https://shop.mango.com/ru/%D0%B6%D0%B5%D0%BD%D1%81%D0%BA%D0%B0%D1%8F/%D1%81%D0%BF%D0%BE%D1%80%D1%82%D0%B8%D0%B2%D0%BD%D0%B0%D1%8F-%D0%BE%D0%B4%D0%B5%D0%B6%D0%B4%D0%B0_c19503847'
url_z = 'https://zarina.ru'
url_b = 'https://belleyou.ru'

belle_links = []
l = ['1']


def paginator(page):
    links = []
    params = {'PAGEN_1': page}
    response = requests.get(url_b + '/catalog/sport/', params=params)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all(class_="all-link1")

    for item in items:
        name = item['href']
        if name.startswith('/catalog/'):
            links.append(name)
    return links


page = 1

while len(l) < 3:
    l = paginator(page)
    belle_links.extend(l)
    page += 1

for link in belle_links:
    response = requests.get(url_b + link)
    soup = BeautifulSoup(response.text, 'lxml')
    name = soup.find(class_="content-information1__title1")
    price = soup.find(class_="content-information1__price-value")
    quality = soup.find(class_="content-information1__info-content")
    item = Item(name.text, price.text, quality.text)
    item.write()
    print(name.text, price.text, quality.text)
print(belle_links)