import os
import json
def save_to_json(parsed_products, filename):
    os.makedirs('parsed_products', exist_ok=True)

    with open(f'parsed_products/{filename}.json', 'w', encoding='utf-8') as file:
        json.dump(parsed_products, file, ensure_ascii=False, indent=4)