from functions.pdf_generator import generate_pdf
from functions.form_validation import validate_form
from functions.file_utils import get_current_order_number
from tkinter import messagebox

def on_generate_button_click(elements):
    # Získání dat z formuláře
    customer_name = elements["entry_customer_name"].get()
    phone = elements["entry_phone"].get()
    imei = elements["entry_imei"].get()
    email = elements["entry_email"].get()
    part_name = elements["entry_part_name"].get()
    part_price = elements["entry_part_price"].get()
    labor_price = elements["entry_labor_price"].get()
    brand = elements["brand_combobox"].get()
    model = elements["model_combobox"].get()

    # Validace formuláře
    valid = validate_form(customer_name, phone, imei, email)
    if not valid:
        return  # Pokud validace neprošla, nebudeme pokračovat

    try:
        # Generování PDF
        generate_pdf(customer_name, phone, imei, email, part_name, part_price, labor_price, brand, model)

        # Aktualizace labelu s číslem zakázky
        new_order_number = get_current_order_number()
        elements["label_order_number"].configure(text=f"Číslo zakázky: SE{new_order_number}")

        messagebox.showinfo("Hotovo", "Zakázkový list byl úspěšně vygenerován.")
    except Exception as e:
        messagebox.showerror("Chyba", f"Nastala chyba při generování PDF: {e}")