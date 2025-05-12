import os
from datetime import datetime


# Cesty ke složkám
ORDER_FOLDERS = {
    "zakazky": "data/zakazky",
    "reklamace": "data/reklamace",
    "instalace": "data/instalace"
}

def ensure_directories():
    """Zajistí, že složky pro zakázky, reklamace a instalace existují."""
    for path in ORDER_FOLDERS.values():
        os.makedirs(path, exist_ok=True)
    os.makedirs("data", exist_ok=True)

def get_prefix_for_category(category):
    return {
        "zakazky": "SE",
        "instalace": "IN",
        "reklamace": "RE"
    }.get(category, "SE")  # Default SE

def load_counters():
    """Načte čítače ze souboru."""
    counters = {}
    if os.path.exists("data/counters.txt"):
        with open("data/counters.txt", "r") as f:
            for line in f:
                key, val = line.strip().split("=")
                counters[key] = int(val)
    return counters

def save_counters(counters):
    """Uloží čítače do souboru."""
    with open("data/counters.txt", "w") as f:
        for key, val in counters.items():
            f.write(f"{key}={val}\n")

def generate_order_number(category, order_index):
    year = datetime.now().year % 100
    prefix = get_prefix_for_category(category)
    return f"{prefix}{year}{order_index:06d}"

def get_next_order_number(category):
    """Vrátí nový číslo zakázky a zároveň uloží nový index do souboru."""
    ensure_directories()
    counters = load_counters()

    year = datetime.now().year % 100
    key = f"{category}_{year}"
    index = counters.get(key, 0) + 1
    counters[key] = index

    save_counters(counters)
    return generate_order_number(category, index)

def get_formatted_order_number(category="zakazky"):
    """Vrací nové číslo zakázky ve formátu SE25000001 a zároveň zvýší čítač."""
    counters = load_counters()

    year = datetime.now().year % 100
    key = f"{category}_{year}"
    index = counters.get(key, 0) + 1
    counters[key] = index
    save_counters(counters)

    return generate_order_number(category, index)

def get_new_pdf_filename(order_number, customer_name):
    safe_name = customer_name.replace(" ", "_")
    return f"{order_number}_{safe_name}.pdf"