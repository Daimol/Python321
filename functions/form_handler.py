from tkinter import messagebox
from functions.form_validation import validate_form
from functions.file_utils import get_formatted_order_number
from functions.pdf_generator import PDFGenerator

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
    category = elements["category_combobox"].get()

    device_desc = elements["entry_device_description"].get("1.0", "end").strip()
    repair_desc = elements["entry_repair_description"].get("1.0", "end").strip()
    condition_desc = elements["entry_condition_description"].get("1.0", "end").strip()


    category = "zakazky"

    # Validace formuláře
    if not validate_form(customer_name, phone, imei, email):
        return

    try:
        # Vygenerování čísla zakázky
        order_code = get_formatted_order_number(category)

        # Vytvoření PDF
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
        pdf.generate_pdf()

        messagebox.showinfo("Hotovo", "Zakázkový list byl úspěšně vygenerován.")
    except Exception as e:
        messagebox.showerror("Chyba", f"Nastala chyba při generování PDF: {e}")
