import requests
from bs4 import BeautifulSoup

def get_price_by_product_code(product_code):
    search_url = f"https://www.servisnidily.cz/hledani/?q={product_code}"
    headers = {"User-Agent": "Mozilla/5.0"}

    # 1. Najdi produkt podle kódu
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    product_link = soup.find("a", class_="product-name")

    if not product_link:
        return f"Product {product_code} not found."

    # 2. Otevři detail produktu
    product_url = "https://www.servisnidily.cz" + product_link["href"]
    detail_response = requests.get(product_url, headers=headers)
    detail_soup = BeautifulSoup(detail_response.text, "html.parser")

    # 3. Najdi cenu (zkusíme více možností)
    price_tag = (
        detail_soup.find("span", class_="price-new") or
        detail_soup.find("span", class_="price js_cena") or
        detail_soup.find("span", class_="price")
    )

    if price_tag:
        return price_tag.text.strip()
    else:
        return "Price not found."

# 🧪 Test
code = "P2068"
print(f"Price for {code}: {get_price_by_product_code(code)}")
