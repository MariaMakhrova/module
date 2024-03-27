import requests
from lxml import html
import csv

# Функція для витягування даних зі сторінки мікрофонів
def extract_microphones(url):
    response = requests.get(url)
    tree = html.fromstring(response.content)
    
    # елементи мікрофонів за допомогою XPath
    names = tree.xpath('//div[@class="list-body__content content flex-wrap"]/div/a/text()')
    prices = tree.xpath('//div[@class="list-body__content content flex-wrap"]/div[@class="list-item__value-price text-md text-orange text-lh--1"]/text()')
    shops = tree.xpath('//div[@class="list-body__content content flex-wrap"]/div[@class="list"]/div[@class="list__item row flex"]/a[@class="shop__title"]/text()')
    
    # місце де зберігаються дані у список кортежів
    data = zip(names, prices, shops)
    
    return data

# Основна функція
def main():
    url = 'https://hotline.ua/audio/mikrofony/'
    data = extract_microphones(url)
    
    # Записуємо дані у CSV-файл
    with open('microphones.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Назва', 'Ціна', 'Магазин'])
        writer.writerows(data)

if __name__ == "__main__":
    main()