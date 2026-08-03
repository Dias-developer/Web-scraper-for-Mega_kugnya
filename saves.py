import json
def save_urls(urls, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(urls, file, ensure_ascii=False, indent=4)

def load_urls(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        urls = json.load(file)
        return urls