from tkinter import messagebox
from functions.form_validation import validate_form
from functions.pdf_generator import generate_pdf  # nebo podle názvu souboru

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
        filename = generate_pdf(customer_name, phone, f"{brand} {model}", part_name, labor_price, imei, email)
        messagebox.showinfo("Hotovo", f"Soubor byl uložen:\n{filename}")
