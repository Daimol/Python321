import os
import datetime
from app.core.pdf_generator import PDFGenerator
from app.core.theme.base_theme import base_theme

class GenerateHandler:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.pdfgen = PDFGenerator(theme=base_theme)

    def handle_generate(self, gui_data):
        # Doplníme datum do servisních dat
        gui_data.setdefault("service_data", {})
        gui_data["service_data"]["date"] = datetime.date.today().isoformat()

        # Vytvoříme cestu k souboru podle order_number
        order_num = gui_data.get("order_number", "unknown")
        filename = f"zakazkovy_list_{order_num}.pdf"
        path = os.path.join(self.data_dir, filename)

        # Vygenerujeme PDF s předanými daty
        self.pdfgen.generate_pdf(
            path=path,
            order_number=order_num,
            customer_data=gui_data.get("customer_data", {}),
            device_data=gui_data.get("device_data", {}),
            service_data=gui_data.get("service_data", {}),
            company_data=gui_data.get("company_data", {})
        )
        return path
