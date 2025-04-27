import customtkinter as ctk
import tkinter as tk
from functions.web_scraping import get_price
from functions.generate_pdf_command import generate_pdf_command


# Když se změní značka, aktualizuj modely
def on_brand_selected(choice, model_combobox, devices_data):
    models = devices_data.get(choice, [])
    model_combobox.configure(values=models)
    if models:
        model_combobox.set(models[0])
    else:
        model_combobox.set("")


def create_left_frame(root):
    frame_left = ctk.CTkFrame(root)
    frame_left.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    label_customer_name = ctk.CTkLabel(frame_left, text="Jméno zákazníka")
    entry_customer_name = ctk.CTkEntry(frame_left)

    label_phone = ctk.CTkLabel(frame_left, text="Telefonní číslo")
    entry_phone = ctk.CTkEntry(frame_left)

    label_imei = ctk.CTkLabel(frame_left, text="IMEI")
    entry_imei = ctk.CTkEntry(frame_left)

    label_email = ctk.CTkLabel(frame_left, text="E-mail")
    entry_email = ctk.CTkEntry(frame_left)

    for i, widget in enumerate([label_customer_name, entry_customer_name,
                                 label_phone, entry_phone,
                                 label_imei, entry_imei,
                                 label_email, entry_email]):
        widget.grid(row=i, column=0, pady=5, sticky="ew")

    return frame_left, entry_customer_name, entry_phone, entry_imei, entry_email


def create_right_frame(root, devices_data):
    frame_right = ctk.CTkFrame(root)
    frame_right.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

    brand_combobox = ctk.CTkComboBox(frame_right, values=list(devices_data.keys()), command=lambda choice: on_brand_selected(choice, model_combobox, devices_data))
    brand_combobox.set("Vyber značku")

    model_combobox = ctk.CTkComboBox(frame_right, values=[])
    model_combobox.set("Vyber model")

    label_part_name = ctk.CTkLabel(frame_right, text="Název dílu")
    entry_part_name = ctk.CTkEntry(frame_right)

    label_part_price = ctk.CTkLabel(frame_right, text="Cena dílu (nezobrazuje se v PDF)")
    entry_part_price = ctk.CTkEntry(frame_right)

    # Funkce pro automatické načtení ceny
    def update_price_from_code(event=None):
        code = entry_part_name.get()
        price = get_price(code)
        if price:
            entry_part_price.delete(0, tk.END)
            entry_part_price.insert(0, str(price))

    entry_part_name.bind("<FocusOut>", update_price_from_code)

    for i, widget in enumerate([brand_combobox, model_combobox, label_part_name, entry_part_name, label_part_price, entry_part_price]):
        widget.grid(row=i, column=0, pady=5, sticky="ew")

    return frame_right, entry_part_name, entry_part_price, brand_combobox, model_combobox


def create_bottom_frame(root):
    frame_bottom = ctk.CTkFrame(root)
    frame_bottom.grid(row=1, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

    label_labor_price = ctk.CTkLabel(frame_bottom, text="Cena práce (Kč)")
    entry_labor_price = ctk.CTkEntry(frame_bottom)
    entry_labor_price.insert(0, "500")

    button_generate = ctk.CTkButton(frame_bottom, text="Vygenerovat zakázkový list",

                                    command=lambda: generate_pdf_command(entry_customer_name, entry_phone, entry_imei,
                                                                         entry_email, entry_part_name, entry_part_price,
                                                                         entry_labor_price, brand_combobox,
                                                                         model_combobox))


    label_labor_price.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_labor_price.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
    button_generate.grid(row=0, column=2, padx=10, pady=5)

    frame_bottom.grid_columnconfigure(1, weight=1)

    return frame_bottom, entry_labor_price, button_generate
