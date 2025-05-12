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
        self.pdf.set_font('DejaVu', '', 14)
        self.pdf.cell(0, 10, "Servisní protokol", ln=True, align='C')
        self.pdf.set_font('DejaVu', '', 12)
        self.pdf.cell(0, 10, f"Číslo zakázky: {self.order_number}", ln=True, align='C')
        self.pdf.ln(5)

    def _add_customer_and_company_info(self):
        # Levý sloupec – info o firmě
        self.pdf.set_xy(10, 40)
        self.pdf.multi_cell(90, 8, "KRAKIT\nEmail: info@krakit.cz\nTel: +420 123 456 789")

        # Pravý sloupec – info o zákazníkovi
        self.pdf.set_xy(110, 40)
        self.pdf.multi_cell(90, 8, f"Zákazník:\n{self.customer_name}\nTel: {self.phone}\nEmail: {self.email}\nIMEI: {self.imei}")

        self.pdf.ln(5)

    def _add_device_info(self):
        self.pdf.ln(5)
        self.pdf.set_font('DejaVu', 'B', 12)
        self.pdf.cell(0, 10, "Zařízení:", ln=True)
        self.pdf.set_font('DejaVu', '', 12)
        self.pdf.multi_cell(0, 8, f"{self.brand} {self.model}\n{self.device_description}")

    def _add_condition_and_repair_info(self):
        self.pdf.ln(2)
        self.pdf.set_font('DejaVu', 'B', 12)
        self.pdf.cell(0, 10, "Popis závady a opravy:", ln=True)
        self.pdf.set_font('DejaVu', '', 12)
        self.pdf.multi_cell(0, 8, f"{self.repair_description}\n\nStav zařízení:\n{self.condition_description}")

    def _add_prices(self):
        self.pdf.ln(2)
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

        filename = get_new_pdf_filename(self.order_number, self.customer_name, self.category)
        self.pdf.output(filename)
        return filename
