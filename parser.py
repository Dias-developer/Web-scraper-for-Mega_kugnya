import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0 Safari/537.36",
"Accept-Language": "ru-RU,ru;q=0.9",
}
thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = make_session()

    return thread_local.session



def make_session():
    session = requests.Session()
    session.headers.update(headers)

    retry = Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"],
        respect_retry_after_header=True,
    )
    session.mount("https://", HTTPAdapter(max_retries=retry))
    session.mount("http://", HTTPAdapter(max_retries=retry))
    return session

def parsing_catalog(url):
    session = make_session()
    response = session.get(url, timeout=(3.05, 27))

    soup = BeautifulSoup(response.text, 'lxml')

    catalog_soup = soup.find_all('div', class_='col-xxl-4 col-lg-3 col-md-4 col-sm-6 col-xs-6 custom_category_grid')
    subcategories = []

    for catalog in catalog_soup:
        catalog_url = catalog.find('a').get('href')
        subcategories.append(catalog_url)

    return subcategories

def parsing_subcategory(subcategory_url):
    session = make_session()
    products_url = []

    for page in range(1, 94):

        url = f"{subcategory_url}?page={page}"

        response = session.get(
            url,
            timeout=(3.05, 27)
        )

        soup = BeautifulSoup(
            response.text,
            'lxml'
        )

        products = soup.select("a.title")

        if not products:
            break

        for product in products:
            product_url = product.get('href')

            if product_url:
                products_url.append(product_url)

    return products_url

def parsing_subcategories(subcategories_urls):
    products_url = []

    with ThreadPoolExecutor(max_workers=20) as executor:

        futures = [
            executor.submit(
                parsing_subcategory,
                subcategory_url
            )
            for subcategory_url in subcategories_urls
        ]

        for future in as_completed(futures):

            result = future.result()

            products_url.extend(result)

            print(
                f"Получено URL: {len(result)} | "
                f"Всего: {len(products_url)}"
            )

    return list(dict.fromkeys(products_url))

def parse_product(url):
    session = get_session()

    response = session.get(url, timeout=(3.05, 27))
    soup = BeautifulSoup(response.text, 'lxml')

    # name
    name_tag = soup.find('h1')
    name = name_tag.text.strip() if name_tag else None

    # price
    price_tag = soup.select_one('div.product-page__price.price')
    price = price_tag.text.strip() if price_tag else 'Можно запросить цену'

    return {
        'url': url,
        'name': name,
        'price': price
    }

def parse_products(urls):
    products = []
    with ThreadPoolExecutor(max_workers=20) as executor:

        futures = [
            executor.submit(
                parse_product,
                url
            )
            for url in urls
        ]

        for i, future in enumerate(as_completed(futures), 1):
            try:
                result = future.result()
                products.append(result)
            except Exception as e:
                print(f'Ошибка: {e}')

            if i % 100 == 0:
                print(f'Обработано: {i}/{len(urls)}')
    return products




