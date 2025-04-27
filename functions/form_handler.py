from functions.generate_pdf_command import generate_pdf
from functions.form_validation import validate_form

def on_generate_button_click(entry_customer_name, entry_phone, entry_imei, entry_email,
                              entry_part_name, entry_part_price, entry_labor_price,
                              brand_combobox, model_combobox):
    customer_name = entry_customer_name.get()
    phone = entry_phone.get()
    imei = entry_imei.get()
    email = entry_email.get()
    part_name = entry_part_name.get()
    part_price = entry_part_price.get()
    labor_price = entry_labor_price.get()
    brand = brand_combobox.get()  # Získání značky
    model = model_combobox.get()  # Získání modelu

    print(f"Validating form...")
    if not validate_form(customer_name, phone, imei, email):
        return

    print(f"Form valid, generating PDF...")
    filename = generate_pdf(customer_name, phone, imei, email, part_name, part_price, labor_price, brand, model)
    print(f"PDF generated: {filename}")
