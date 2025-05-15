from fpdf import FPDF
from functions.file_utils import get_new_pdf_filename


class PDFGenerator:
    def __init__(self, order_number, customer_name, phone, imei, email,
                 brand, model, part_name, part_price, labor_price,
                 device_description, repair_description, condition_description,
                 category="zakazky"):
        self.order_number = order_number
        self.customer_name = customer_name
        self.phone = phone
        self.imei = imei
        self.email = email
        self.brand = brand
        self.model = model
        self.part_name = part_name
        self.part_price = part_price
        self.labor_price = labor_price
        self.device_description = device_description
        self.repair_description = repair_description
        self.condition_description = condition_description
        self.category = category
        self.pdf = FPDF()
        self._setup_pdf()

    def _setup_pdf(self):
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.pdf.add_page()
        self.pdf.add_font('DejaVu', '', 'fonts/DejaVuSans.ttf', uni=True)
        self.pdf.set_font('DejaVu', '', 12)

    def _add_header(self):
        # Logo a název firmy v hlavičce
        try:
            self.pdf.image("assets/logo.png", 10, 10, 40)  # Přizpůsob rozměry
        except:
            pass  # Pokud není logo k dispozici

        self.pdf.set_xy(55, 10)
        self.pdf.set_font('DejaVu', '', 16)
        self.pdf.cell(0, 10, "KRAKIT – Servisní protokol", ln=True)

        self.pdf.set_font('DejaVu', '', 12)
        self.pdf.set_xy(55, 18)
        self.pdf.cell(0, 10, f"Číslo zakázky: {self.order_number}", ln=True)
        self.pdf.ln(10)

    def _add_customer_and_company_info(self):
        # Levý sloupec – Zákazník
        self.pdf.set_xy(10, 35)
        self.pdf.set_font('DejaVu', '', 12)
        self.pdf.multi_cell(90, 8,
            f"Zákazník:\n{self.customer_name}\nTel: {self.phone}\nEmail: {self.email}\nIMEI: {self.imei}",
            border=1)

        # Pravý sloupec – Firma
        self.pdf.set_xy(110, 35)
        self.pdf.multi_cell(90, 8,
            "Servis:\nKRAKIT\nEmail: info@krakit.cz\nTel: +420 123 456 789\nIČO: 12345678\nAdresa: Servisní 12, Praha",
            border=1)

    def _add_device_info(self):
        self.pdf.ln(10)
        self.pdf.set_font('DejaVu', '', 12)
        self.pdf.cell(0, 10, "Zařízení:", ln=True)
        self.pdf.multi_cell(0, 8, f"{self.brand} {self.model}\n{self.device_description}", border=1)

    def _add_condition_and_repair_info(self):
        self.pdf.ln(5)
        self.pdf.set_font('DejaVu', '', 12)
        self.pdf.cell(0, 10, "Popis opravy:", ln=True)
        self.pdf.multi_cell(0, 8, self.repair_description, border=1)

        self.pdf.ln(5)
        self.pdf.cell(0, 10, "Stav zařízení při převzetí:", ln=True)
        self.pdf.multi_cell(0, 8, self.condition_description, border=1)

    def _add_prices(self):
        self.pdf.ln(5)
        self.pdf.set_font('DejaVu', '', 12)
        self.pdf.cell(0, 10, f"Cena práce: {self.labor_price} Kč", ln=True)

    def _add_footer(self):
        self.pdf.ln(20)
        self.pdf.cell(90, 10, "Předal:", border="T")
        self.pdf.cell(10)
        self.pdf.cell(90, 10, "Převzal:", border="T")

    def generate_pdf(self):
        self._add_header()
        self._add_customer_and_company_info()
        self._add_device_info()
        self._add_condition_and_repair_info()
        self._add_prices()
        self._add_footer()

        filename = get_new_pdf_filename(self.order_number)
        self.pdf.output(filename)
        return filename
