from parser import parsing_catalog, parsing_subcategories
from saves import save_urls, load_urls
import time

import os


start = time.perf_counter()

# Category_1 #

print('Крупно-бытовая техника')
url_1 = 'https://mega-kuhnya.ru/catalog/krupno-bitovaya-tekhnika/'

#################
# SUBCATEGORIES #
#################

if os.path.exists("jsons/subcategories_1.json"):
    print('Загружаем подкатегорий из JSON...')
    subcategories_1 = load_urls('jsons/subcategories_1.json')

else:
    print('Получаем подкатегорий с сайта...')

    subcategories_1 = parsing_catalog(url_1)

    save = save_urls(
    subcategories_1,
    "jsons/subcategories_1.json"
)


################
# PRODUCT_URLS #
################

if os.path.exists('jsons/products_urls_1.json'):
    print('Загружаем ссылку на товары из JSON...')
    products_url_1 = load_urls('jsons/products_urls_1.json')
else:
    print('Получаем ссылку на товары из сайта...')
    products_url_1 = parsing_subcategories(subcategories_1)
    save_urls(
        products_url_1,
        'jsons/products_urls_1.json'
    )


# Category_2 #

print('Встраиваемая техника')
url_2 = 'https://mega-kuhnya.ru/catalog/vstraivaemaya-tehnika/'

#################
# SUBCATEGORIES #
#################

if os.path.exists("jsons/subcategories_2.json"):
    print('Загружаем подкатегорий из JSON...')
    subcategories_2 = load_urls('jsons/subcategories_2.json')
else:
    print('Получаем подкатегорий с сайта...')

    subcategories_2 = parsing_catalog(url_2)

    save = save_urls(
        subcategories_2,
        "jsons/subcategories_2.json"
    )

################
# PRODUCT_URLS #
################

if os.path.exists('jsons/products_urls_2.json'):
    print('Загружаем ссылку на товары из JSON...')
    products_url_2 = load_urls('jsons/products_urls_2.json')
else:
    print('Получаем ссылку на товары из сайта...')
    products_url_2 = parsing_subcategories(subcategories_2)

    save_urls(
        products_url_2,
        'jsons/products_urls_2.json'
    )

# Category_3 #

print('Климатическое оборудование')
url_3 = 'https://mega-kuhnya.ru/catalog/klimaticheskoe-oborudovanie/'
#################
# SUBCATEGORIES #
#################
if os.path.exists("jsons/subcategories_3.json"):
    print('Загружаем подкатегорий из JSON...')
    subcategories_3 = load_urls('jsons/subcategories_3.json')
else:
    print('Получаем подкатегорий с сайта...')

    subcategories_3 = parsing_catalog(url_3)

    save = save_urls(
        subcategories_3,
        "jsons/subcategories_3.json"
    )
################
# PRODUCT_URLS #
################

if os.path.exists('jsons/products_urls_3.json'):
    print('Загружаем ссылку на товары из JSON...')
    products_url_2 = load_urls('jsons/products_urls_3.json')
else:
    print('Получаем ссылку на товары из сайта...')
    products_url_3 = parsing_subcategories(subcategories_3)

    save_urls(
        products_url_3,
        'jsons/products_urls_3.json'
    )

end = time.perf_counter()
print(f"{end - start:.2f}")
