import json
import os
import re
from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Model:
    model: str
    year: int = None
    price: int = None
    # další atributy...

@dataclass
class ModelSeries:
    model_series: str
    models: List[Model]


def load_all_products(folder_path: str) -> Dict[str, List[ModelSeries]]:
    products = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as f:
                data = json.load(f)
                device_name = data["device"]

                brands = []
                for b in data["brands"]:
                    models = [Model(**m) for m in b["models"]]
                    brand = ModelSeries(model_series=b["model_series"], models=models)
                    brands.append(brand)

                products[device_name] = brands
    return products



def natural_sort_key(s: str):
    """
    Klíč pro přirozené řazení, který rozpozná čísla i text.
    Například: '11', '12', '13', 'X', 'XS', '14' budou správně seřazeny.
    """
    # rozdělí řetězec na čísla a jiné znaky (čísla převede na int)
    return [
        int(text) if text.isdigit() else text.lower()
        for text in re.split(r'(\d+)', s)
    ]

def get_brands(brands: List[ModelSeries]) -> List[str]:
    """
    Vrátí seznam modelových řad správně seřazených pomocí natural sort.
    """
    return sorted((b.model_series for b in brands), key=natural_sort_key)


def get_models_by_brand(products: List[ModelSeries], selected_series: str) -> List[str]:
    for b in products:
        if b.model_series == selected_series:
            return [m.model for m in b.models]
    return []
