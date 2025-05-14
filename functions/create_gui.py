import tkinter as tk
import customtkinter as ctk
from functions.update_model_combobox import on_series_selected, on_brand_selected, save_selected_values
from functions.web_scraping import get_price
from functions.form_handler import on_generate_button_click
from functions.file_utils import update_device_record

def create_gui(root, devices_data):
    ctk.set_appearance_mode("dark")
    root.configure(fg_color="black")
    root.grid_columnconfigure((0, 1, 2), weight=1)
    root.grid_rowconfigure(1, weight=1)

    # Horní rámec
    frame_top = ctk.CTkFrame(root, fg_color="gray15")
    frame_top.grid(row=0, column=0, columnspan=3, padx=20, pady=(20, 10), sticky="ew")
    frame_top.grid_columnconfigure(0, weight=1)

    label_order_number = ctk.CTkLabel(frame_top, text="Číslo zakázky: 001", font=("Arial", 18, "bold"))
    label_order_number.grid(row=0, column=0, padx=20, pady=10, sticky="w")

    # První sloupec (levý)
    frame_first = ctk.CTkFrame(root, fg_color="gray10")
    frame_first.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
    frame_first.grid_columnconfigure(0, weight=1)

    label_category = ctk.CTkLabel(frame_first, text="Typ zakázky:")
    label_category.grid(row=0, column=0, pady=(5, 0), padx=20, sticky="w")
    dropdown_category = ctk.CTkOptionMenu(frame_first, values=["zakázky", "instalace", "reklamace"])
    dropdown_category.set("zakázky")
    dropdown_category.grid(row=1, column=0, padx=20, pady=(0, 10), sticky="ew")

    labels_entries_left = [
        ("Jméno zákazníka", ctk.CTkEntry(frame_first)),
        ("Telefonní číslo", ctk.CTkEntry(frame_first)),
        ("IMEI", ctk.CTkEntry(frame_first)),
        ("E-mail", ctk.CTkEntry(frame_first)),
    ]

    for i, (text, entry) in enumerate(labels_entries_left):
        label = ctk.CTkLabel(frame_first, text=text)
        label.grid(row=i * 2 + 2, column=0, pady=(5, 0), padx=20, sticky="w")
        entry.grid(row=i * 2 + 3, column=0, padx=20, pady=(0, 10), sticky="ew")

    entry_customer_name = labels_entries_left[0][1]
    entry_phone = labels_entries_left[1][1]
    entry_imei = labels_entries_left[2][1]
    entry_email = labels_entries_left[3][1]

    # Druhý sloupec (prostřední)
    frame_second = ctk.CTkFrame(root, fg_color="gray10")
    frame_second.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")
    frame_second.grid_columnconfigure(0, weight=1)

    brand_combobox = ctk.CTkComboBox(frame_second, values=list(devices_data.keys()))
    brand_combobox.set("Vyber značku")
    series_combobox = ctk.CTkComboBox(frame_second, values=[])
    series_combobox.set("Vyber modelovou řadu")
    model_combobox = ctk.CTkComboBox(frame_second, values=[])
    model_combobox.set("Vyber model")

    brand_combobox.configure(command=lambda choice: on_brand_selected(choice, series_combobox, devices_data))
    series_combobox.configure(command=lambda choice: on_series_selected(choice, model_combobox, devices_data, brand_combobox))

    label_part_name = ctk.CTkLabel(frame_second, text="Název dílu")
    entry_part_name = ctk.CTkEntry(frame_second)

    label_part_price = ctk.CTkLabel(frame_second, text="Cena dílu (nezobrazuje se v PDF)")
    entry_part_price = ctk.CTkEntry(frame_second)

    def update_price_from_code(event=None):
        code = entry_part_name.get()
        price = get_price(code)
        if price:
            entry_part_price.delete(0, tk.END)
            entry_part_price.insert(0, str(price))

    entry_part_name.bind("<FocusOut>", update_price_from_code)

    update_button = ctk.CTkButton(frame_second, text="Aktualizovat záznam",
                                  command=lambda: update_device_record(brand_combobox, series_combobox, model_combobox,
                                                                       entry_customer_name, entry_phone, entry_imei,
                                                                       entry_email, entry_part_name, entry_part_price))

    widgets_right = [
        brand_combobox, series_combobox, model_combobox,
        label_part_name, entry_part_name,
        label_part_price, entry_part_price,
        update_button
    ]

    for i, widget in enumerate(widgets_right):
        widget.grid(row=i, column=0, pady=5, padx=20, sticky="ew")

    # Třetí sloupec (vpravo)
    frame_third = ctk.CTkFrame(root, fg_color="gray10")
    frame_third.grid(row=1, column=2, padx=20, pady=20, sticky="nsew")
    frame_third.grid_columnconfigure(0, weight=1)

    label_device_desc = ctk.CTkLabel(frame_third, text="Popis zařízení:")
    label_device_desc.pack(pady=(10, 0), anchor="w")
    entry_device_description = ctk.CTkTextbox(frame_third, height=80)
    entry_device_description.pack(fill="both", expand=True, padx=5)

    label_repair_desc = ctk.CTkLabel(frame_third, text="Popis opravy:")
    label_repair_desc.pack(pady=(10, 0), anchor="w")
    entry_repair_description = ctk.CTkTextbox(frame_third, height=80)
    entry_repair_description.pack(fill="both", expand=True, padx=5)

    label_condition_desc = ctk.CTkLabel(frame_third, text="Stav zařízení při převzetí:")
    label_condition_desc.pack(pady=(10, 0), anchor="w")
    entry_condition_description = ctk.CTkTextbox(frame_third, height=80)
    entry_condition_description.pack(fill="both", expand=True, padx=5)

    # Spodní rámec
    frame_bottom = ctk.CTkFrame(root, fg_color="gray12")
    frame_bottom.grid(row=2, column=0, columnspan=3, padx=20, pady=10, sticky="ew")
    frame_bottom.grid_columnconfigure(1, weight=1)

    label_labor_price = ctk.CTkLabel(frame_bottom, text="Cena práce (Kč)")
    entry_labor_price = ctk.CTkEntry(frame_bottom)
    entry_labor_price.insert(0, "500")

    button_generate = ctk.CTkButton(frame_bottom, text="Vygenerovat zakázkový list",
                                    command=lambda: on_generate_button_click({
                                        "frame_top": frame_top,
                                        "label_order_number": label_order_number,
                                        "dropdown_category": dropdown_category,
                                        "frame_first": frame_first,
                                        "entry_customer_name": entry_customer_name,
                                        "entry_phone": entry_phone,
                                        "entry_imei": entry_imei,
                                        "entry_email": entry_email,
                                        "frame_second": frame_second,
                                        "entry_part_name": entry_part_name,
                                        "entry_part_price": entry_part_price,
                                        "brand_combobox": brand_combobox,
                                        "series_combobox": series_combobox,
                                        "model_combobox": model_combobox,
                                        "frame_third": frame_third,
                                        "entry_device_description": entry_device_description,
                                        "entry_repair_description": entry_repair_description,
                                        "entry_condition_description": entry_condition_description,
                                        "frame_bottom": frame_bottom,
                                        "entry_labor_price": entry_labor_price,
                                        "button_generate": button_generate,
                                    }))

    label_labor_price.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    entry_labor_price.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    button_generate.grid(row=0, column=2, padx=10, pady=10)

    return {
        "frame_top": frame_top,
        "label_order_number": label_order_number,
        "dropdown_category": dropdown_category,
        "frame_first": frame_first,
        "entry_customer_name": entry_customer_name,
        "entry_phone": entry_phone,
        "entry_imei": entry_imei,
        "entry_email": entry_email,
        "frame_second": frame_second,
        "entry_part_name": entry_part_name,
        "entry_part_price": entry_part_price,
        "brand_combobox": brand_combobox,
        "series_combobox": series_combobox,
        "model_combobox": model_combobox,
        "frame_third": frame_third,
        "entry_device_description": entry_device_description,
        "entry_repair_description": entry_repair_description,
        "entry_condition_description": entry_condition_description,
        "frame_bottom": frame_bottom,
        "entry_labor_price": entry_labor_price,
        "button_generate": button_generate,
    }
