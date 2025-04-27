import customtkinter as ctk
from tkinter import messagebox
from functions.device_loader import load_devices
from functions.gui_elements import create_left_frame, create_right_frame, create_bottom_frame
from functions.form_validation import validate_form
from functions.generate_pdf_command import generate_pdf  # Pokud máte tuto funkci v samostatném souboru

# Načti data zařízení
devices_data = load_devices()

# Vytvoření GUI
root = ctk.CTk()
root.title("Generátor zakázkového listu")
root.geometry("1000x600")
root.eval('tk::PlaceWindow . center')

frame_left, entry_customer_name, entry_phone, entry_imei, entry_email = create_left_frame(root)
frame_right, entry_part_name, entry_part_price, brand_combobox, model_combobox = create_right_frame(root, devices_data)
frame_bottom, entry_labor_price, button_generate = create_bottom_frame(root)

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

# Nastavení akce pro tlačítko "Vygenerovat zakázkový list"
button_generate.configure(command=lambda: generate_pdf_command(
    entry_customer_name, entry_phone, entry_imei, entry_email,
    entry_part_name, entry_part_price, entry_labor_price,
    brand_combobox, model_combobox))

root.mainloop()


