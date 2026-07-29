from parser import parsing_catalog, parsing_subcategories
print('Крупно-бытовая техника')
url_1 = 'https://mega-kuhnya.ru/catalog/krupno-bitovaya-tekhnika/'
subcategories_1 = parsing_catalog(url_1)
products_url_1 = parsing_subcategories(subcategories_1)
print(len(products_url_1))


print('Встраиваемая техника')
url_2 = 'https://mega-kuhnya.ru/catalog/vstraivaemaya-tehnika/'
subcategories_2 = parsing_catalog(url_2)
products_url_2 = parsing_subcategories(subcategories_2)
print(len(products_url_2))

print('Климатическое оборудование')
url_3 = 'https://mega-kuhnya.ru/catalog/klimaticheskoe-oborudovanie/'
subcategories_3 = parsing_catalog(url_3)
products_url_3 = parsing_subcategories(subcategories_3)
print(len(products_url_3))