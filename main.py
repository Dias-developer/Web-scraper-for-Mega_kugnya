from parser import parsing_catalog_1, parsing_catalog_2, parsing_catalog_3
print('Крупно-бытовая техника')
url_1 = 'https://mega-kuhnya.ru/catalog/krupno-bitovaya-tekhnika/'
parsing_catalog_1(url_1)
print('Встраиваемая техника')
url_2 = 'https://mega-kuhnya.ru/catalog/vstraivaemaya-tehnika/'
parsing_catalog_2(url_2)
print('Климатическое оборудование')
url_3 = 'https://mega-kuhnya.ru/catalog/klimaticheskoe-oborudovanie/'
parsing_catalog_3(url_3)