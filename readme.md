# 🛠️ Servisní aplikace pro mobilní zařízení

---

### 🎯 Cíl aplikace  
Aplikace slouží k zadávání údajů o zakázkách pro servis mobilních zařízení a generování PDF s detailními informacemi o zákazníkovi, zařízení a ceně opravy.

---

### 📚 Použité technologie a knihovny  
- Programovací jazyk: Python  
- GUI knihovna: CustomTkinter  
- Generování PDF: FPDF  
- Další: práce se soubory, obrázky (logo)

---

### 🗂️ Struktura projektu

    Python321/
    ├── app/                        # Hlavní aplikace
    │   ├── core/                   # Jádro - generování PDF a stylování
    │   │   ├── pdf_generator.py    # Třída PDFGenerator - generuje stylizované PDF
    │   │   ├── base_theme.py       # Slovník `base_theme` - definice barev, fontů a rozměrů pro PDF
    │   │   └── __init__.py
    │   │
    │   ├── data/                   # Výstupy - vygenerovaná PDF
    │   │   (po spuštění se zde objeví PDF)
    │   │
    │   ├── gui/                    # Grafické uživatelské rozhraní (PySide6)
    │   │   ├── app_gui.py          # Třída ZakazkovyListApp - hlavní okno aplikace
    │   │   ├── theme.py            # Funkce `apply_theme` - vzhled aplikace Qt
    │   │   └── __init__.py
    │   │
    │   ├── handler/                # Obsluha logiky aplikace
    │   │   ├── generate_handler.py # Třída GenerateHandler - propojuje GUI a PDFGenerator
    │   │   └── __init__.py
    │   │
    │   ├── services/               # Pomocné služby (data, načítání produktů atd.)
    │   │   ├── company_info.py     # Funkce `get_data` - vrací údaje o servisu
    │   │   ├── product_loader.py   # Funkce pro načítání produktů/zařízení/modelů
    │   │   └── __init__.py
    │   │
    │   ├── main.py                 # Spouštěcí skript aplikace
    │   └── __init__.py
    │
    ├── resources/                  # Statické zdroje
    │   ├── fonts/                  # Použité fonty pro PDF
    │   │   └── DejaVuSans.ttf
    │   │
    │   ├── icons/                  # Ikony aplikace
    │   │   └── ikonaW.ico
    │   │
    │   ├── images/                 # Obrázky (např. logo pro PDF a ukázky)
    │   │   ├── logo.png
    │   │   └── screenshot.png
    │
    ├── tests/                      # Testovací skripty (připravit podle potřeby)
    │   └── ...
    │
    ├── .venv/                      # Virtuální prostředí (není ve verzi na GitHubu)
    │
    ├── LICENSE                     # Licence projektu
    ├── README.md                   # Dokumentace projektu
    ├── requirements.txt            # Seznam Python balíčků
    └── .gitignore                  # Ignorované soubory Git


---

### ✅ Aktuálně implementované funkce  
- Zadání údajů o zákazníkovi (jméno, telefon, email)  
- Výběr typu opravy a zařízení (značka, model, kategorie)  
- Zobrazení ceny za opravu (součástky + práce)  
- Generování PDF s informacemi a logem servisu  
- Možnost úpravy ceny opravy

---

### 📝 Plánované funkce / To-Do  
- Validace vstupních údajů (telefon, email, čísla)  
- Ukládání historie zakázek do souborů nebo databáze  
- Export historie zakázek do CSV  
- Přidání více jazykových mutací GUI a PDF  
- Integrace s databází (např. SQLite nebo externí DB)

---

### 🐞 Známé chyby a problémy  
- Při generování PDF se logo nezobrazuje správně (formát / cesta)  
- Chybová hláška při zadání neplatného emailu (nutná lepší validace)

---

### 💡 Poznámky a nápady  
- Přidání funkce pro odeslání PDF emailem přímo z aplikace  
- Implementace tmavého režimu GUI pomocí CustomTkinter  
- Vytvoření instalačního balíčku pro Windows (např. PyInstaller)  
- Vylepšení UX, například automatické doplňování modelů podle značky  
- Podpora více zařízení a typů oprav

---

### 🚀 Jak spustit aplikaci

1. Klonujte repozitář: