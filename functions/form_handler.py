from tkinter import messagebox
from functions.form_validation import validate_form
from functions.pdf_generator import PDFGenerator
from functions.file_utils import get_formatted_order_number  # import funkce pro číslo zakázky

def on_generate_button_click(elements):
    # Získání hodnot z GUI
    customer_name = elements["entry_customer_name"].get()
    phone = elements["entry_phone"].get()
    imei = elements["entry_imei"].get()
    email = elements["entry_email"].get()
    part_name = elements["entry_part_name"].get()
    part_price = elements["entry_part_price"].get()
    labor_price = elements["entry_labor_price"].get()
    brand = elements["brand_combobox"].get()
    model = elements["model_combobox"].get()
    category = elements["dropdown_category"].get()

    device_desc = elements["entry_device_description"].get("1.0", "end").strip()
    repair_desc = elements["entry_repair_description"].get("1.0", "end").strip()
    condition_desc = elements["entry_condition_description"].get("1.0", "end").strip()

    # Validace formuláře - vrací True/False
    if not validate_form(customer_name, phone, imei, email):
        return  # Pokud validace neprojde, ukončíme funkci

    try:
        # Vygeneruj unikátní číslo zakázky podle kategorie
        order_code = get_formatted_order_number(category)

        # Vytvoř instanci PDFGeneratoru s daty z formuláře
        pdf = PDFGenerator(
            order_number=order_code,
            customer_name=customer_name,
            phone=phone,
            imei=imei,
            email=email,
            brand=brand,
            model=model,
            part_name=part_name,
            part_price=part_price,
            labor_price=labor_price,
            device_description=device_desc,
            repair_description=repair_desc,
            condition_description=condition_desc,
            category=category
        )
        # Vygeneruj PDF a ulož jej, název souboru uložíme
        filename = pdf.generate_pdf()

        # Zobraz potvrzení uživateli
        messagebox.showinfo("Hotovo", f"Zakázkový list byl úspěšně vygenerován:\n{filename}")

        # Vyčisti formulář pro další zadání
        reset_form(elements)

    except Exception as e:
        messagebox.showerror("Chyba", f"Nastala chyba při generování PDF: {e}")


def reset_form(elements):
    # Vymazání všech vstupních polí a nastavení výchozích hodnot
    elements["entry_customer_name"].delete(0, "end")
    elements["entry_phone"].delete(0, "end")
    elements["entry_imei"].delete(0, "end")
    elements["entry_email"].delete(0, "end")
    elements["entry_part_name"].delete(0, "end")
    elements["entry_part_price"].delete(0, "end")
    elements["entry_labor_price"].delete(0, "end")
    elements["brand_combobox"].set('Vyber značku')
    elements["model_combobox"].set('Vyber model')
    elements["dropdown_category"].set('zakázky')

    elements["entry_device_description"].delete("1.0", "end")
    elements["entry_repair_description"].delete("1.0", "end")
    elements["entry_condition_description"].delete("1.0", "end")
