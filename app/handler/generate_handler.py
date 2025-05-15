from tkinter import messagebox
from app.validation import validate_form
from app.pdf_generator import PDFGenerator

class GenerateHandler:
    def __init__(self, app_gui):
        self.app_gui = app_gui  # odkaz na instanci GUI pro přístup k datům a resetu

    def on_generate_click(self):
        # Získáme data z GUI pomocí metody get_form_data
        data = self.app_gui.get_form_data()

        # Validace
        if not validate_form(data["customer_name"], data["phone"], data["imei"], data["email"]):
            return

        try:
            # Tady by měl být tvůj kód pro získání order_code
            # třeba:
            order_code = self.get_formatted_order_number(data["category"])

            pdf = PDFGenerator(
                order_number=order_code,
                customer_name=data["customer_name"],
                phone=data["phone"],
                imei=data["imei"],
                email=data["email"],
                brand=data["brand"],
                model=data["model"],
                part_name=data["part_name"],
                part_price=data["part_price"],
                labor_price=data["labor_price"],
                device_description=data["device_description"],
                repair_description=data["repair_description"],
                condition_description=data["condition_description"],
                category=data["category"]
            )

            filename = pdf.generate_pdf()

            messagebox.showinfo("Hotovo", f"Zakázkový list byl úspěšně vygenerován:\n{filename}")

            # Vyčistíme formulář
            self.app_gui.reset_form()

        except Exception as e:
            messagebox.showerror("Chyba", f"Nastala chyba při generování PDF: {e}")

    def get_formatted_order_number(self, category):
        # Tady implementuj logiku generování čísla zakázky podle kategorie
        # Pro test dej třeba jednoduché číslo:
        return f"{category.upper()}-001"
