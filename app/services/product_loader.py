from dataclasses import dataclass
from typing import List, Optional
import json
from pathlib import Path

# --- Datové třídy ---

@dataclass
class Repairability:
    score: int
    source: str

@dataclass
class Product:
    name: str
    brand: str
    type: str
    url: str
    parts: List[str]
    image: Optional[str] = None
    released: Optional[str] = None
    repairability: Optional[Repairability] = None

# --- Načtení produktů ze souboru ---

def load_products(path: str) -> List[Product]:
    """Načte seznam produktů ze zadaného JSON souboru."""
    file_path = Path(path)
    with file_path.open(encoding="utf-8") as f:
        raw_data = json.load(f)

    products = []
    for item in raw_data:
        repair = item.get("repairability")
        repairability = Repairability(**repair) if repair else None

        product = Product(
            name=item["name"],
            brand=item["brand"],
            type=item["type"],
            url=item["url"],
            parts=item["parts"],
            image=item.get("image"),
            released=item.get("released"),
            repairability=repairability
        )
        products.append(product)

    return products

# --- Pomocné funkce pro práci s produkty ---

def get_brands(products: List[Product]) -> List[str]:
    """Vrátí seřazený seznam unikátních značek."""
    return sorted(set(product.brand for product in products))

def get_models_by_brand(products: List[Product], brand: str) -> List[str]:
    """Vrátí seřazený seznam modelů podle značky."""
    return sorted(
        product.name for product in products if product.brand.lower() == brand.lower()
    )
