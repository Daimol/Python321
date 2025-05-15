import os
import customtkinter as ctk
from app.handler.generate_handler import GenerateHandler

class ZakazkovyListApp(ctk.CTkFrame):
    def __init__(self, root, devices_data):
        super().__init__(root)
        self.root = root
        self.devices_data = devices_data
        self.handler = GenerateHandler(self)

        # Nastavení ikony
        icon_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'icons', 'ikona.ico')
        try:
            self.root.iconbitmap(icon_path)
        except Exception as e:
            print(f"Nelze načíst ikonu: {e}")

        self.pack(fill="both", expand=True, padx=20, pady=20)

        self.root.title("KRAKIT")
        self.root.geometry("700x600")

        # Rámeček pro formulář
        self.form_frame = ctk.CTkFrame(self)
        self.form_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.form_frame.columnconfigure(1, weight=1)  # Druhý sloupec roztahovatelný

        # Label + Entry Jméno zákazníka
        ctk.CTkLabel(self.form_frame, text="Jméno zákazníka:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.entry_customer_name = ctk.CTkEntry(self.form_frame)
        self.entry_customer_name.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        # Telefon
        ctk.CTkLabel(self.form_frame, text="Telefon:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.entry_phone = ctk.CTkEntry(self.form_frame)
        self.entry_phone.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        # IMEI
        ctk.CTkLabel(self.form_frame, text="IMEI:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.entry_imei = ctk.CTkEntry(self.form_frame)
        self.entry_imei.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        # Email
        ctk.CTkLabel(self.form_frame, text="Email:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.entry_email = ctk.CTkEntry(self.form_frame)
        self.entry_email.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

        # Kategorie (ComboBox)
        ctk.CTkLabel(self.form_frame, text="Kategorie:").grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.dropdown_category = ctk.CTkComboBox(self.form_frame, values=["Zakázky", "Reklamace", "Servis"])
        self.dropdown_category.grid(row=4, column=1, sticky="ew", padx=5, pady=5)
        self.dropdown_category.set("Zakázky")

        # Popis zařízení (Text)
        ctk.CTkLabel(self.form_frame, text="Popis zařízení:").grid(row=5, column=0, sticky="nw", padx=5, pady=5)
        self.entry_device_description = ctk.CTkTextbox(self.form_frame, height=80)
        self.entry_device_description.grid(row=5, column=1, sticky="ew", padx=5, pady=5)

        # Popis opravy (Text)
        ctk.CTkLabel(self.form_frame, text="Popis opravy:").grid(row=6, column=0, sticky="nw", padx=5, pady=5)
        self.entry_repair_description = ctk.CTkTextbox(self.form_frame, height=80)
        self.entry_repair_description.grid(row=6, column=1, sticky="ew", padx=5, pady=5)

        # Tlačítko generovat
        self.button_generate = ctk.CTkButton(self, text="Generovat", command=self.handler.on_generate_click)
        self.button_generate.grid(row=7, column=0, pady=20)

        # Zajistit, že hlavní rámec i formulář se roztahují správně
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

    def get_form_data(self):
        return {
            "customer_name": self.entry_customer_name.get(),
            "phone": self.entry_phone.get(),
            "imei": self.entry_imei.get(),
            "email": self.entry_email.get(),
            "category": self.dropdown_category.get(),
            "device_description": self.entry_device_description.get("1.0", "end").strip(),
            "repair_description": self.entry_repair_description.get("1.0", "end").strip(),
        }

    def reset_form(self):
        self.entry_customer_name.delete(0, "end")
        self.entry_phone.delete(0, "end")
        self.entry_imei.delete(0, "end")
        self.entry_email.delete(0, "end")
        self.dropdown_category.set("Zakázky")
        self.entry_device_description.delete("1.0", "end")
        self.entry_repair_description.delete("1.0", "end")
