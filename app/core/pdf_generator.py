import os
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


class PDFGenerator:
    def __init__(self, theme, font_path=None, logo_path=None):
        PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

        if font_path is None:
            font_path = os.path.join(PROJECT_ROOT, "resources", "fonts", "DejaVuSans.ttf")
        if logo_path is None:
            logo_path = os.path.join(PROJECT_ROOT, "resources", "images", "logo.png")

        self.font_path = font_path
        self.logo_path = logo_path
        self.theme = theme

        self.register_fonts()

    def register_fonts(self):
        if not os.path.exists(self.font_path):
            raise FileNotFoundError(f"Font file not found: {self.font_path}")
        pdfmetrics.registerFont(TTFont(self.theme["font_name"], self.font_path))

    def draw_boxed_section(self, c, x, y, w, h, title, content, padding=15):
        # Barvy a velikosti z tématu
        title_font_size = self.theme["section_title_font_size"]
        title_color = colors.HexColor(self.theme["section_title_color"])
        content_font_size = self.theme["section_content_font_size"]
        content_color = colors.HexColor(self.theme["section_content_color"])
        box_fill_color = colors.HexColor(self.theme["section_background_color"])
        box_border_color = colors.HexColor(self.theme["section_border_color"])

        # Pozadí rámečku s zaoblením
        c.setFillColor(box_fill_color)
        c.roundRect(x, y - h, w, h, radius=8, fill=1, stroke=0)

        # Rámeček kolem boxu
        c.setStrokeColor(box_border_color)
        c.setLineWidth(1)
        c.roundRect(x, y - h, w, h, radius=8, fill=0, stroke=1)

        # Nadpis sekce (v horní části rámečku)
        c.setFont(self.theme["font_name"], title_font_size)
        c.setFillColor(title_color)
        text_width = c.stringWidth(title, self.theme["font_name"], title_font_size)
        title_x = x + (w / 2) - (text_width / 2)
        c.drawString(title_x, y - 25, title)

        # Text obsahu uvnitř rámečku (s odsazením)
        lines = content.split("\n")
        line_height = content_font_size + 2
        text_start_y = y - 50  # trochu níž pod nadpisem

        for i, line in enumerate(lines):
            line_x = x + padding
            line_y = text_start_y - i * line_height
            c.setFont(self.theme["font_name"], content_font_size)
            c.setFillColor(content_color)
            c.drawString(line_x, line_y, line)

    def generate_pdf(self, path, order_number, customer_data, device_data, service_data, company_data):
        c = canvas.Canvas(path, pagesize=A4)
        width, height = A4
        margin = 50

        # Logo nahoře uprostřed
        if os.path.exists(self.logo_path):
            logo = ImageReader(self.logo_path)
            c.drawImage(
                logo,
                (width - self.theme["logo_width"]) / 2,
                height - margin - self.theme["logo_height"],
                width=self.theme["logo_width"],
                height=self.theme["logo_height"],
                preserveAspectRatio=True,
                mask='auto'
            )
            logo_height = self.theme["logo_height"]
        else:
            logo_height = 0

        # Titulek (zakázka)
        c.setFont(self.theme["font_name"], self.theme["title_font_size"])
        c.setFillColor(colors.HexColor(self.theme["title_color"]))
        zakazka_y = height - margin - logo_height - 30
        c.drawCentredString(width / 2, zakazka_y, f"Zakázka č. {order_number}")
        c.setFillColor(colors.black)

        # Rozdělení stránky na dvě poloviny pro zákazníka a servis
        left_x = margin
        right_x = width / 2 + 20
        start_y = zakazka_y - 70
        box_width = (width / 2) - margin - 30
        box_height = 110

        # Zákazník
        customer_text = "\n".join(f"{k}: {v}" for k, v in customer_data.items())
        self.draw_boxed_section(c, left_x, start_y, box_width, box_height, "Zákazník", customer_text)

        # Servis (firma)
        service_lines = [
            f"Jméno: {company_data.get('Servis', '')}",
            f"Adresa: {company_data.get('Adresa', '')}",
            f"Telefon: {company_data.get('Telefon', '')}",
            f"Email: {company_data.get('Email', '')}"
        ]
        service_text = "\n".join(service_lines)
        self.draw_boxed_section(c, right_x, start_y, box_width, box_height, "Servis", service_text)

        # Popisy zařízení a služby níže, přes celou šířku
        y_pos = start_y - box_height - 40
        box_height_big = 90

        self.draw_boxed_section(c, margin, y_pos, width - 2 * margin, box_height_big, "Popis zařízení", device_data.get("desc", ""))
        y_pos -= box_height_big + 30
        self.draw_boxed_section(c, margin, y_pos, width - 2 * margin, box_height_big, "Popis opravy", service_data.get("repair", ""))
        y_pos -= box_height_big + 30
        self.draw_boxed_section(c, margin, y_pos, width - 2 * margin, box_height_big, "Stav zařízení při převzetí", service_data.get("condition", ""))

        # Cena a datum dole
        c.setFont(self.theme["font_name"], self.theme["price_font_size"])
        c.setFillColor(colors.HexColor(self.theme["price_color"]))

        price_text = f"{self.theme['price_label']}: {service_data.get('price', '0')} Kč"
        c.drawString(margin, 60, price_text)

        current_date = datetime.now().strftime("%d.%m.%Y %H:%M")
        c.drawRightString(width - margin, 60, f"Datum: {current_date}")

        c.save()
