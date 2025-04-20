from fpdf import FPDF
import datetime
import customtkinter as ctk
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class ServisApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Formulář pro servis mobilů")
        self.geometry("600x600")

        # ==== Zákaznické údaje ====
        self.label_name = ctk.CTkLabel(self, text="Jméno zákazníka:")
        self.label_name.pack(pady=(10, 0))
        self.entry_name = ctk.CTkEntry(self, placeholder_text="Např. Jan Novák")
        self.entry_name.pack(pady=5, fill="x", padx=20)

        self.label_phone = ctk.CTkLabel(self, text="Telefon:")
        self.label_phone.pack()
        self.entry_phone = ctk.CTkEntry(self, placeholder_text="Např. 777 123 456")
        self.entry_phone.pack(pady=5, fill="x", padx=20)

        self.label_email = ctk.CTkLabel(self, text="Email:")
        self.label_email.pack()
        self.entry_email = ctk.CTkEntry(self, placeholder_text="Např. jan@email.cz")
        self.entry_email.pack(pady=5, fill="x", padx=20)

        # ==== Zařízení ====
        self.label_device = ctk.CTkLabel(self, text="Zařízení:")
        self.label_device.pack()
        self.device_options = ["iPhone 12", "iPhone 13", "Samsung S21", "Xiaomi Redmi Note 10"]
        self.device_combobox = ctk.CTkComboBox(self, values=self.device_options)
        self.device_combobox.pack(pady=5, fill="x", padx=20)

        # ==== Popis závady ====
        self.label_issue = ctk.CTkLabel(self, text="Popis závady:")
        self.label_issue.pack()
        self.entry_issue = ctk.CTkTextbox(self, height=80)
        self.entry_issue.pack(pady=5, fill="x", padx=20)

        # ==== Nabídka oprav ====
        self.label_repair = ctk.CTkLabel(self, text="Vyber opravu:")
        self.label_repair.pack()
        self.repairs = {
            "Výměna displeje": 2500,
            "Výměna baterie": 1200,
            "Čištění po zatečení": 800,
            "Diagnostika": 300,
        }
        self.repair_combobox = ctk.CTkComboBox(self, values=list(self.repairs.keys()))
        self.repair_combobox.pack(pady=5, fill="x", padx=20)

        # ==== Cena opravy ====
        self.label_price = ctk.CTkLabel(self, text="Cena opravy:")
        self.label_price.pack(pady=5)
        self.entry_price = ctk.CTkEntry(self)
        self.entry_price.pack(pady=5, fill="x", padx=20)

        # ==== Tlačítko ====
        self.submit_button = ctk.CTkButton(self, text="💾 Uložit a exportovat do PDF", command=self.save_data)
        self.submit_button.pack(pady=20)

        # Aktualizace ceny podle vybraného úkonu
        self.repair_combobox.bind("<Configure>", self.update_price)

    def update_price(self, event=None):
        # Získáme vybraný úkon
        repair = self.repair_combobox.get()
        # Získáme cenu z dictionary
        price = self.repairs.get(repair, 0)
        # Aktualizujeme cenu v Entry
        self.entry_price.delete(0, ctk.END)
        self.entry_price.insert(0, str(price))

    def save_data(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        device = self.device_combobox.get()
        issue = self.entry_issue.get("1.0", "end").strip()
        repair = self.repair_combobox.get()
        price = self.entry_price.get()  # Cena bude teď z Entry, takže je editovatelná

        # Ujistíme se, že cena je číslo
        try:
            price = float(price)
        except ValueError:
            print("Neplatná cena")
            return

        self.save_to_pdf(name, phone, email, device, issue, repair, price)

    def save_to_pdf(self, name, phone, email, device, issue, repair, price, ):
        now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"zakazka_{now}.pdf"

        pdf = FPDF()
        pdf.add_page()

        # Cesta k fontům
        font_path = os.path.join(os.path.dirname(__file__), "fonts","DejaVuSans.ttf")
        bold_font_path = os.path.join(os.path.dirname(__file__), "fonts","DejaVuSans-Bold.ttf")
        logo_path = os.path.join(os.path.dirname(__file__), "logo","logo.png")

        # Přidání fontů s plnou cestou
        pdf.add_font("DejaVu", "", font_path, uni=True)
        pdf.add_font("DejaVu", "B", bold_font_path, uni=True)

        # Nastavení písma
        try:
            pdf.set_font("DejaVu", "B", 16)
        except Exception as e:
            print(f"Chyba při nastavování písma: {e}")

        # Záhlaví
        pdf.cell(200, 10, "Servisní zakázka", ln=True, align="C")

        pdf.image(logo_path, x=60, y=40, w=90)  # Změňte pozici a velikost dle potřeby

        pdf.ln(80)  # Zajištění odstupu pod logem pro text

        pdf.set_font("DejaVu", "", 12)
        pdf.ln(10)
        pdf.cell(100, 10, f"Jméno zákazníka: {name}", ln=True)
        pdf.cell(100, 10, f"Telefon: {phone}", ln=True)
        pdf.cell(100, 10, f"Email: {email}", ln=True)
        pdf.cell(100, 10, f"Zařízení: {device}", ln=True)
        pdf.multi_cell(0, 10, f"Popis závady: {issue}")
        pdf.cell(100, 10, f"Oprava: {repair}", ln=True)
        pdf.cell(100, 10, f"Cena: {price} Kč", ln=True)

        pdf.output(filename)
        print(f"✅ PDF vytvořeno: {filename}")


if __name__ == "__main__":
    app = ServisApp()
    app.mainloop()
