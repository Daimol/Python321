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

    app/
    ├── core.py                 # Startovací a hlavní logika aplikace
    ├── main.py                 # Spouštěcí skript aplikace
    ├── gui/
    │   └── app_gui.py          # Definice GUI třídy a vizuální logika
    ├── handler/
    │   └── generate_handler.py # Logika generování PDF, validace, event handler
    ├── functions/              # Pomocné funkce (validace, práce s čísly, atd.)
    ├── data/                   # Ukládání dat o zakázkách
    ├── fonts/                  # Písma používaná v PDF
    ├── logo/                   # Logo servisu pro PDF
    └── resources/
    └── icons/
        └── ikona.ico       # Ikona aplikace
    requirements.txt            # Seznam závislostí
    readme.md                  # Popis projektu a návod k použití

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