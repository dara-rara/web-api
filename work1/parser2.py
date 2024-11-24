import requests as rq
from bs4 import BeautifulSoup


def parse_maxidom():
    products = []
    url = 'https://www.maxidom.ru/catalog/kraski-i-emali/'
    while url:
        response = rq.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        # Находим все товары на странице
        items_name = soup.find_all('div', class_='l-product__name')
        items_price = soup.find_all('div', class_='l-product__buy')

        for i in range(len(items_name)):
            title = items_name[i].find('span', itemprop='name').text.strip()
            price = items_price[i].find('div', class_='l-product__price-base').text.strip()
            products.append({'title': title, 'price': int("".join(filter(str.isdigit, price)))})

        # Переход на следующую страницу
        next_page = soup.find('div', class_='lvl2__content-nav-numbers-number').find_all('a')
        if len(next_page) == 3 and next_page[1]['href'] != '#':
            url = 'https://www.maxidom.ru' + next_page[1]['href']
        elif len(next_page) == 4:
            url = 'https://www.maxidom.ru' + next_page[2]['href']
        elif len(next_page) == 3 and next_page[1]['href'] == '#':
            url = 'https://www.maxidom.ru' + next_page[2]['href']
        else:
            url = None
    return products


if __name__ == "__main__":
    product_data = parse_maxidom()
    for product in product_data:
        print(f"Товар: {product['title']}, Цена: {product['price']}")