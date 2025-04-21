import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
import requests
from fpdf import FPDF
import os
from datetime import datetime
import json

# Načtení JSON databáze značek a modelů
def load_devices():
    with open("devices.json", "r", encoding="utf-8") as f:
        return json.load(f)

devices_data = load_devices()

# Callback při výběru značky
def on_brand_selected(choice):
    models = devices_data.get(choice, [])
    model_combobox.configure(values=models)
    if models:
        model_combobox.set(models[0])
    else:
        model_combobox.set("")

# FPDF - GENERÁTOR PDF
def generate_pdf(customer_name, phone, phone_model, part_name, labor_price, imei, email):
    pdf = FPDF()
    pdf.add_page()

    pdf.add_font("DejaVu", "", "fonts/DejaVuSans.ttf", uni=True)
    pdf.set_font("DejaVu", size=12)
    pdf.image("logo/logo.png", x=10, y=8, w=33)

    pdf.cell(200, 10, txt=f"Zákazkový list - {customer_name}", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Telefon: {phone}", ln=True)
    pdf.cell(200, 10, txt=f"Model telefonu: {phone_model}", ln=True)
    pdf.cell(200, 10, txt=f"IMEI: {imei}", ln=True)
    pdf.cell(200, 10, txt=f"E-mail: {email}", ln=True)
    pdf.cell(200, 10, txt=f"Název dílu: {part_name}", ln=True)
    pdf.cell(200, 10, txt=f"Cena práce: {labor_price} Kč", ln=True)
    pdf.cell(200, 10, txt=f"Celková cena: {labor_price} Kč", ln=True)
    pdf.cell(200, 10, txt=f"Datum: {datetime.now().strftime('%d.%m.%Y %H:%M')}", ln=True)

    os.makedirs("zakazky", exist_ok=True)
    filename = f"zakazky/{customer_name}_{phone_model}_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"
    pdf.output(filename)
    return filename

# SCRAPING - CENA DÍLU
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

# TKINTER GUI
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("Generátor zakázkového listu")
root.geometry("1000x600")
root.eval('tk::PlaceWindow . center')

# GRID
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# FRAMES
frame_left = ctk.CTkFrame(root)
frame_left.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

frame_right = ctk.CTkFrame(root)
frame_right.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

frame_bottom = ctk.CTkFrame(root)
frame_bottom.grid(row=1, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

# LEVÝ SLOUPEC
label_customer_name = ctk.CTkLabel(frame_left, text="Jméno zákazníka")
entry_customer_name = ctk.CTkEntry(frame_left, width=230)

label_phone = ctk.CTkLabel(frame_left, text="Telefonní číslo")
entry_phone = ctk.CTkEntry(frame_left, width=230)

label_imei = ctk.CTkLabel(frame_left, text="IMEI")
entry_imei = ctk.CTkEntry(frame_left, width=230)

label_email = ctk.CTkLabel(frame_left, text="E-mail")
entry_email = ctk.CTkEntry(frame_left, width=230)

# PRAVÝ SLOUPEC
label_brand = ctk.CTkLabel(frame_right, text="Značka")
brand_combobox = ctk.CTkComboBox(frame_right, values=list(devices_data.keys()), command=on_brand_selected, width=230)
brand_combobox.set("Vyber značku")

label_model = ctk.CTkLabel(frame_right, text="Model")
model_combobox = ctk.CTkComboBox(frame_right, values=[], width=230)
model_combobox.set("Vyber model")

label_part_name = ctk.CTkLabel(frame_right, text="Název dílu")
entry_part_name = ctk.CTkEntry(frame_right, width=230)

label_part_price = ctk.CTkLabel(frame_right, text="Cena dílu (nezobrazuje se v PDF)")
entry_part_price = ctk.CTkEntry(frame_right, width=230)

# FUNKCE: automatické načtení ceny
def update_price_from_code(event=None):
    code = entry_part_name.get()
    price = get_price(code)
    if price:
        entry_part_price.delete(0, tk.END)
        entry_part_price.insert(0, str(price))

entry_part_name.bind("<FocusOut>", update_price_from_code)

# SPODNÍ ČÁST
label_labor_price = ctk.CTkLabel(frame_bottom, text="Cena práce (Kč)")
entry_labor_price = ctk.CTkEntry(frame_bottom, width=100)
entry_labor_price.insert(0, "500")

def calculate_price():
    customer_name = entry_customer_name.get()
    phone = entry_phone.get()
    imei = entry_imei.get()
    email = entry_email.get()
    brand = brand_combobox.get()
    model = model_combobox.get()
    part_name = entry_part_name.get()
    labor_price = float(entry_labor_price.get())

    if not customer_name or not phone:
        messagebox.showerror("Chyba", "Vyplňte prosím jméno zákazníka a telefonní číslo.")
        return

    phone_model = f"{brand} {model}"
    filename = generate_pdf(customer_name, phone, phone_model, part_name, labor_price, imei, email)
    messagebox.showinfo("Hotovo", f"Soubor byl uložen:\n{filename}")

button_generate = ctk.CTkButton(frame_bottom, text="Vygenerovat zakázkový list", command=calculate_price)

# UMÍSTĚNÍ WIDGETŮ
for i, widget in enumerate([
    label_customer_name, entry_customer_name,
    label_phone, entry_phone,
    label_imei, entry_imei,
    label_email, entry_email
]):
    widget.grid(row=i, column=0, pady=5, sticky="ew")

for i, widget in enumerate([
    label_brand, brand_combobox,
    label_model, model_combobox,
    label_part_name, entry_part_name,
    label_part_price, entry_part_price
]):
    widget.grid(row=i, column=0, pady=5, sticky="ew")

label_labor_price.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_labor_price.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
button_generate.grid(row=0, column=2, padx=10, pady=5)

frame_bottom.grid_columnconfigure(1, weight=1)

root.mainloop()
