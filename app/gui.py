import tkinter as tk
import customtkinter as ctk
from app.handler import on_generate_button_click
from app.data_loader import load_devices

class ZakazkovyListApp:
    def __init__(self, root, devices_data):
        self.root = root
        self.devices_data = devices_data

        ctk.set_appearance_mode("dark")
        self.root.configure(fg_color="black")
        self.root.title("Zakázkový list - KRAKIT")

        self.root.grid_columnconfigure((0, 1, 2), weight=1)
        self.root.grid_rowconfigure(1, weight=1)

        self.create_top_frame()
        self.create_left_frame()
        self.create_middle_frame()
        self.create_right_frame()
        self.create_bottom_frame()

    def create_top_frame(self):
        self.frame_top = ctk.CTkFrame(self.root, fg_color="gray15")
        self.frame_top.grid(row=0, column=0, columnspan=3, padx=20, pady=(20, 10), sticky="ew")
        self.frame_top.grid_columnconfigure(0, weight=1)

        self.label_order_number = ctk.CTkLabel(self.frame_top, text="Číslo zakázky: 001", font=("Arial", 18, "bold"))
        self.label_order_number.grid(row=0, column=0, padx=20, pady=10, sticky="w")

    def create_left_frame(self):
        self.frame_first = ctk.CTkFrame(self.root, fg_color="gray10")
        self.frame_first.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        self.frame_first.grid_columnconfigure(0, weight=1)

        label_category = ctk.CTkLabel(self.frame_first, text="Typ zakázky:")
        label_category.grid(row=0, column=0, pady=(5, 0), padx=20, sticky="w")

        self.dropdown_category = ctk.CTkOptionMenu(self.frame_first, values=["zakázky", "instalace", "reklamace"])
        self.dropdown_category.set("zakázky")
        self.dropdown_category.grid(row=1, column=0, padx=20, pady=(0, 10), sticky="ew")

        self.entry_customer_name = self.create_labeled_entry(self.frame_first, "Jméno zákazníka", 2)
        self.entry_phone = self.create_labeled_entry(self.frame_first, "Telefonní číslo", 4)
        self.entry_imei = self.create_labeled_entry(self.frame_first, "IMEI", 6)
        self.entry_email = self.create_labeled_entry(self.frame_first, "E-mail", 8)

    def create_labeled_entry(self, parent, text, start_row):
        label = ctk.CTkLabel(parent, text=text)
        label.grid(row=start_row, column=0, pady=(5, 0), padx=20, sticky="w")
        entry = ctk.CTkEntry(parent)
        entry.grid(row=start_row + 1, column=0, padx=20, pady=(0, 10), sticky="ew")
        return entry

    def create_middle_frame(self):
        self.frame_second = ctk.CTkFrame(self.root, fg_color="gray10")
        self.frame_second.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")
        self.frame_second.grid_columnconfigure(0, weight=1)

        self.brand_combobox = ctk.CTkComboBox(self.frame_second, values=list(self.devices_data.keys()))
        self.brand_combobox.set("Vyber značku")
        self.brand_combobox.configure(command=self.on_brand_selected)
        self.brand_combobox.grid(row=0, column=0, pady=5, padx=20, sticky="ew")

        self.series_combobox = ctk.CTkComboBox(self.frame_second, values=[])
        self.series_combobox.set("Vyber modelovou řadu")
        self.series_combobox.configure(command=self.on_series_selected)
        self.series_combobox.grid(row=1, column=0, pady=5, padx=20, sticky="ew")

        self.model_combobox = ctk.CTkComboBox(self.frame_second, values=[])
        self.model_combobox.set("Vyber model")
        self.model_combobox.grid(row=2, column=0, pady=5, padx=20, sticky="ew")

        self.label_part_name = ctk.CTkLabel(self.frame_second, text="Název dílu")
        self.label_part_name.grid(row=3, column=0, pady=(10, 0), padx=20, sticky="w")

        self.entry_part_name = ctk.CTkEntry(self.frame_second)
        self.entry_part_name.grid(row=4, column=0, pady=5, padx=20, sticky="ew")
        self.entry_part_name.bind("<FocusOut>", self.update_price_from_name)

        self.label_part_price = ctk.CTkLabel(self.frame_second, text="Cena dílu (nezobrazuje se v PDF)")
        self.label_part_price.grid(row=5, column=0, pady=(10, 0), padx=20, sticky="w")

        self.entry_part_price = ctk.CTkEntry(self.frame_second)
        self.entry_part_price.grid(row=6, column=0, pady=5, padx=20, sticky="ew")

    def create_right_frame(self):
        self.frame_third = ctk.CTkFrame(self.root, fg_color="gray10")
        self.frame_third.grid(row=1, column=2, padx=20, pady=20, sticky="nsew")
        self.frame_third.grid_columnconfigure(0, weight=1)

        self.label_device_desc = ctk.CTkLabel(self.frame_third, text="Popis zařízení:")
        self.label_device_desc.pack(pady=(10, 0), anchor="w")

        self.entry_device_description = ctk.CTkTextbox(self.frame_third, height=80)
        self.entry_device_description.pack(fill="both", expand=True, padx=5)

        self.label_repair_desc = ctk.CTkLabel(self.frame_third, text="Popis opravy:")
        self.label_repair_desc.pack(pady=(10, 0), anchor="w")

        self.entry_repair_description = ctk.CTkTextbox(self.frame_third, height=80)
        self.entry_repair_description.pack(fill="both", expand=True, padx=5)

        self.label_condition_desc = ctk.CTkLabel(self.frame_third, text="Stav zařízení při převzetí:")
        self.label_condition_desc.pack(pady=(10, 0), anchor="w")

        self.entry_condition_description = ctk.CTkTextbox(self.frame_third, height=80)
        self.entry_condition_description.pack(fill="both", expand=True, padx=5)

    def create_bottom_frame(self):
        self.frame_bottom = ctk.CTkFrame(self.root, fg_color="gray12")
        self.frame_bottom.grid(row=2, column=0, columnspan=3, padx=20, pady=10, sticky="ew")
        self.frame_bottom.grid_columnconfigure(1, weight=1)

        self.label_labor_price = ctk.CTkLabel(self.frame_bottom, text="Cena práce (Kč)")
        self.label_labor_price.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.entry_labor_price = ctk.CTkEntry(self.frame_bottom)
        self.entry_labor_price.insert(0, "500")
        self.entry_labor_price.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.button_generate = ctk.CTkButton(self.frame_bottom, text="Vygenerovat zakázkový list",
                                             command=self.on_generate_click)
        self.button_generate.grid(row=0, column=2, padx=10, pady=10)

    # --- Metody pro zpracování akcí ---

    def on_brand_selected(self, choice):
        series = list(self.devices_data.get(choice, {}).keys())
        self.series_combobox.configure(values=series)
        self.series_combobox.set("Vyber modelovou řadu")
        self.model_combobox.configure(values=[])
        self.model_combobox.set("Vyber model")

    def on_series_selected(self, choice):
        brand = self.brand_combobox.get()
        models = self.devices_data.get(brand, {}).get(choice, [])
        self.model_combobox.configure(values=models)
        self.model_combobox.set("Vyber model")

    def update_price_from_name(self, event=None):
        code = self.entry_part_name.get()
        price = self.get_price(code)
        if price:
            self.entry_part_price.delete(0, tk.END)
            self.entry_part_price.insert(0, str(price))

    def get_price(self, code):
        # TODO: napojit na získání ceny dle kódu - třeba z jiného modulu
        # Prozatím dummy implementace:
        dummy_prices = {"dil1": 150, "dil2": 250, "dil3": 350}
        return dummy_prices.get(code.lower())

    def on_generate_click(self):
        data = {
            "frame_top": self.frame_top,
            "label_order_number": self.label_order_number,
            "dropdown_category": self.dropdown_category,
            "frame_first": self.frame_first,
            "entry_customer_name": self.entry_customer_name,
            "entry_phone": self.entry_phone,
            "entry_imei": self.entry_imei,
            "entry_email": self.entry_email,
            "frame_second": self.frame_second,
            "entry_part_name": self.entry_part_name,
            "entry_part_price": self.entry_part_price,
            "brand_combobox": self.brand_combobox,
            "series_combobox": self.series_combobox,
            "model_combobox": self.model_combobox,
            "frame_third": self.frame_third,
            "entry_device_description": self.entry_device_description,
            "entry_repair_description": self.entry_repair_description,
            "entry_condition_description": self.entry_condition_description,
            "frame_bottom": self.frame_bottom,
            "entry_labor_price": self.entry_labor_price,
            "button_generate": self.button_generate,
        }
        on_generate_button_click(data)

def run_app():
    devices_data = load_devices()
    root = ctk.CTk()
    app = ZakazkovyListApp(root, devices_data)
    root.mainloop()

if __name__ == "__main__":
    run_app()
