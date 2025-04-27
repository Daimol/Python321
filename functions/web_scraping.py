import requests

def get_price(product_code):
    url = f"https://www.servisnidily.cz/{product_code}"
    response = requests.get(url)

    if response.status_code == 200:
        price_tag = 'class="price js_cena"'
        start = response.text.find(price_tag)
        if start != -1:
            start = response.text.find('>', start) + 1
            end = response.text.find('<', start)
            price_str = response.text[start:end].strip()
            return parse_price(price_str)
    return None

def parse_price(price_str):
    try:
        return float(price_str.replace("\xa0", "").replace("Kč", "").replace(" ", "").strip())
    except ValueError:
        return 0.0
