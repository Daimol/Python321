import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
import requests
from fpdf import FPDF
import os
from datetime import datetime

# CENOVÉ FUNKCE
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

# Funkce pro generování PDF s podporou Unicode
def generate_pdf(customer_name, phone_model, product_code, product_price, labor_price, imei, email, consent):
    pdf = FPDF()
    pdf.add_page()

    # Nastavení fontu s podporou UTF-8 (font musí být v "fonts/DejaVuSans.ttf" nebo jiném souboru)
    pdf.add_font("DejaVu", "", "fonts/DejaVuSans.ttf", uni=True)
    pdf.set_font("DejaVu", size=12)

    # Přidání loga
    pdf.image("logo/logo.png", x=10, y=8, w=33)

    # Přidání textu (česky)
    pdf.cell(200, 10, txt=f"Zákazkový list - {customer_name}", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Model telefonu: {phone_model}", ln=True)
    pdf.cell(200, 10, txt=f"IMEI: {imei}", ln=True)
    pdf.cell(200, 10, txt=f"E-mail: {email}", ln=True)
    pdf.cell(200, 10, txt=f"Kód produktu: {product_code}", ln=True)
    pdf.cell(200, 10, txt=f"Cena dílu: {product_price} Kč", ln=True)
    pdf.cell(200, 10, txt=f"Cena práce: {labor_price} Kč", ln=True)
    pdf.cell(200, 10, txt=f"Celková cena: {float(product_price) + labor_price} Kč", ln=True)
    pdf.cell(200, 10, txt=f"Souhlas se servisem: {'Ano' if consent else 'Ne'}", ln=True)
    pdf.cell(200, 10, txt=f"Datum: {datetime.now().strftime('%d.%m.%Y %H:%M')}", ln=True)

    # Uložení PDF
    os.makedirs("zakazky", exist_ok=True)
    filename = f"zakazky/{customer_name}_{phone_model}_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"
    pdf.output(filename)
    return filename

# TKINTER GUI
ctk.set_appearance_mode("dark")  # Nastavení tmavého režimu
ctk.set_default_color_theme("blue")
root = ctk.CTk()
root.title("Generátor zakázkového listu")

# Nastavení velikosti okna a umístění na střed
root.geometry("1000x600")  # Velikost okna (šířka 1000px a výška 600px)

# Centrování okna
window_width = 1000
window_height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Vypočítání pozice pro centrování okna
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

# Nastavení okna na střed
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# VSTUPNÍ PRVKY
label_customer_name = ctk.CTkLabel(root, text="Jméno zákazníka")
entry_customer_name = ctk.CTkEntry(root)

label_phone_model = ctk.CTkLabel(root, text="Model telefonu")
phone_model_combobox = ctk.CTkComboBox(root, values=["Apple iPhone 5S", "Samsung Galaxy S10", "Huawei P30", "Jiný"])

label_imei = ctk.CTkLabel(root, text="IMEI")
entry_imei = ctk.CTkEntry(root)

label_email = ctk.CTkLabel(root, text="E-mail")
entry_email = ctk.CTkEntry(root)

label_product_code = ctk.CTkLabel(root, text="Kód produktu")
entry_product_code = ctk.CTkEntry(root)

label_labor_price = ctk.CTkLabel(root, text="Cena práce (Kč)")
entry_labor_price = ctk.CTkEntry(root)
entry_labor_price.insert(0, "500")

consent_var = tk.BooleanVar()
checkbox_consent = ctk.CTkCheckBox(root, text="Zákazník souhlasí s opravou", variable=consent_var)

# FUNKCE PO STISKNUTÍ TLAČÍTKA
def calculate_price():
    customer_name = entry_customer_name.get()
    phone_model = phone_model_combobox.get()
    product_code = entry_product_code.get()
    labor_price = float(entry_labor_price.get())
    imei = entry_imei.get()
    email = entry_email.get()
    consent = consent_var.get()

    product_price = get_price(product_code)
    if not product_price:
        messagebox.showerror("Chyba", "Produkt nebyl nalezen.")
        return

    filename = generate_pdf(customer_name, phone_model, product_code, product_price, labor_price, imei, email, consent)
    messagebox.showinfo("Hotovo", f"Soubor byl uložen:\n{filename}")

# TLAČÍTKO
button_generate = ctk.CTkButton(root, text="Vygenerovat zakázkový list", command=calculate_price)

# ROZLOŽENÍ
for widget in [
    label_customer_name, entry_customer_name,
    label_phone_model, phone_model_combobox,
    label_imei, entry_imei,
    label_email, entry_email,
    label_product_code, entry_product_code,
    label_labor_price, entry_labor_price,
    checkbox_consent,
    button_generate
]:
    widget.pack(padx=20, pady=10)

root.mainloop()
