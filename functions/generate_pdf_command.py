from tkinter import messagebox
from functions.form_validation import validate_form
from functions.pdf_generator import generate_pdf  # nebo podle názvu souboru
from functions.file_utils import get_new_pdf_filename

def generate_pdf_command(entry_customer_name, entry_phone, entry_imei, entry_email, entry_part_name, entry_part_price, entry_labor_price, brand_combobox, model_combobox):
    customer_name = entry_customer_name.get()
    phone = entry_phone.get()
    imei = entry_imei.get()
    email = entry_email.get()
    part_name = entry_part_name.get()
    labor_price = float(entry_labor_price.get())
    brand = brand_combobox.get()
    model = model_combobox.get()

    # Zavoláme validaci
    errors = validate_form(customer_name, phone, imei, email)

    if errors:
        # Pokud jsou chyby, zobrazí se okno s chybami
        messagebox.showerror("Chyba", "\n".join(errors))
    else:
        # Pokud nejsou chyby, pokračujeme s generováním PDF

        # Získání unikátního názvu souboru
        filename = get_new_pdf_filename()  # Používáme novou funkci pro získání názvu souboru

        # Zavoláme funkci pro generování PDF
        generate_pdf(customer_name, phone, imei, email, part_name, part_price, labor_price, brand, model)

        # Zobrazí informaci o uložení souboru
        messagebox.showinfo("Hotovo", f"Soubor byl uložen:\n{filename}")
