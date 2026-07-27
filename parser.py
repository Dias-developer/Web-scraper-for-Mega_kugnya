import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0 Safari/537.36",
"Accept-Language": "ru-RU,ru;q=0.9",
}

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

    catalogs_soup = soup.find_all('div', class_='col-xxl-4 col-lg-3 col-md-4 col-sm-6 col-xs-6 custom_category_grid')
    catalogs = []

    for catalog in catalogs_soup:
        catalog_url = catalog.find('a').get('href')
        catalogs.append(catalog_url)

    for catalog in catalogs:
        print(catalog)
