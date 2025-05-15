import os
from datetime import datetime
from typing import Dict


class OrderManager:
    def __init__(self, base_dir: str = "PDF"):
        self.base_dir = base_dir
        self.counters_file = os.path.join(self.base_dir, "counters.txt")

        self.categories = {
            "zakazky": {"prefix": "SE", "folder": os.path.join(self.base_dir, "zakazky")},
            "reklamace": {"prefix": "RE", "folder": os.path.join(self.base_dir, "reklamace")},
            "instalace": {"prefix": "IN", "folder": os.path.join(self.base_dir, "instalace")}
        }

        self.ensure_directories()

    def ensure_directories(self) -> None:
        """Vytvoří složky pro PDF a jejich kategorie, pokud neexistují."""
        os.makedirs(self.base_dir, exist_ok=True)
        for data in self.categories.values():
            os.makedirs(data["folder"], exist_ok=True)

    def load_counters(self) -> Dict[str, int]:
        """Načte čítače ze souboru."""
        counters = {}
        if os.path.exists(self.counters_file):
            with open(self.counters_file, "r", encoding="utf-8") as file:
                for line in file:
                    if "=" in line:
                        key, val = line.strip().split("=")
                        counters[key] = int(val)
        return counters

    def save_counters(self, counters: Dict[str, int]) -> None:
        """Uloží čítače zpět do souboru."""
        with open(self.counters_file, "w", encoding="utf-8") as file:
            for key, val in counters.items():
                file.write(f"{key}={val}\n")

    def generate_order_number(self, category: str) -> str:
        """Vytvoří nové číslo zakázky a aktualizuje čítač."""
        if category not in self.categories:
            category = "zakazky"

        counters = self.load_counters()
        year = datetime.now().year % 100
        key = f"{category}_{year}"
        index = counters.get(key, 0) + 1
        counters[key] = index
        self.save_counters(counters)

        prefix = self.categories[category]["prefix"]
        return f"{prefix}{year:02d}{index:06d}"

    def get_pdf_filename(self, order_number: str, category: str) -> str:
        """Vrátí cestu k PDF souboru dle čísla zakázky a kategorie."""
        if category not in self.categories:
            category = "zakazky"
        folder = self.categories[category]["folder"]
        return os.path.join(folder, f"{order_number}.pdf")
