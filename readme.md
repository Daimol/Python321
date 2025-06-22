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
    ├── app/                     # Hlavní aplikační balíček
    │   ├── gui/                 # Vše, co se týká GUI (okna, widgety)
    │   │   ├── widgets/         # Vlastní widgety
    │   │   ├── app_gui.py       # Hlavní GUI aplikace
    │   │   └── theme.py         # Styl, barvy
    │   │
    │   ├── core/                # Logika aplikace (generování, výpočty, validace)
    │   │   ├── pdf_generator.py
    │   │   ├── validation.py
    │   │   └── ...
    │   │
    │   ├── data/                # Správa vstupních/konfiguračních souborů
    │   │   ├── devices.json
    │   │   ├── counters.txt
    │   │   └── ...
    │   │
    │   ├── services/            # Práce s daty – načítání, ukládání, manipulace
    │   │   ├── product_loader.py
    │   │   ├── file_utils.py
    │   │   └── order_manager.py
    │   │
    │   ├── main.py              # Vstupní bod aplikace (GUI launcher)
    │   └── __init__.py          # (prázdný nebo s definovanými exporty)
    │
    ├── product/                 # Vzorky dat (např. json soubory zařízení)
    │   └── apple.json
    │
    ├── resources/               # Obrázky, fonty, ikony
    │   ├── fonts/
    │   ├── icons/
    │   └── images/
    │
    ├── setup.py                 # Volitelně spouštěč nebo CLI
    ├── requirements.txt         # Seznam závislostí
    └── README.md

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