from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os


def draw_boxed_section(c, x, y, w, title, content):
    """Pomocná metoda pro kreslení sekcí s nadpisem a textem."""
    c.setFont("DejaVuSans", 11)
    c.drawString(x, y, title)
    c.setFont("DejaVuSans", 10)
    c.rect(x, y - 60, w, 50)
    text = c.beginText(x + 5, y - 15)
    for line in content.split("\n"):
        text.textLine(line)
    c.drawText(text)


class PDFGenerator:
    def __init__(self, font_path="fonts/DejaVuSans.ttf", logo_path="assets/logo.png"):
        self.font_path = font_path
        self.logo_path = logo_path
        self.register_fonts()

    def register_fonts(self):
        pdfmetrics.registerFont(TTFont("DejaVuSans", self.font_path))

    def generate_pdf(self, path, order_number, customer_data, device_data, service_data, company_data):
        c = canvas.Canvas(path, pagesize=A4)
        width, height = A4
        margin = 40

        c.setFont("DejaVuSans", 10)

        # Logo a název firmy
        if os.path.exists(self.logo_path):
            logo = ImageReader(self.logo_path)
            c.drawImage(logo, margin, height - 80, width=100, preserveAspectRatio=True, mask='auto')
        c.setFont("DejaVuSans", 16)
        c.drawRightString(width - margin, height - 50, company_data.get("name", "Název firmy"))

        # Údaje o zákazníkovi
        c.setFont("DejaVuSans", 10)
        c.drawString(margin, height - 120, "Zákazník:")
        y = height - 135
        for label, value in customer_data.items():
            c.drawString(margin + 10, y, f"{label}: {value}")
            y -= 15

        # Údaje o firmě
        c.drawRightString(width - margin, height - 120, "Servis:")
        y = height - 135
        for label, value in company_data.items():
            c.drawRightString(width - margin - 10, y, f"{label}: {value}")
            y -= 15

        # Číslo zakázky
        c.setFont("DejaVuSans", 12)
        c.setFillColor(colors.darkblue)
        c.drawCentredString(width / 2, height - 200, f"Zakázkový list č. {order_number}")
        c.setFillColor(colors.black)

        # Popis zařízení
        draw_boxed_section(c, margin, height - 240, width - 2 * margin, "Popis zařízení", device_data.get("desc", ""))

        # Popis opravy
        draw_boxed_section(c, margin, height - 340, width - 2 * margin, "Popis opravy", service_data.get("repair", ""))

        # Stav zařízení při převzetí
        draw_boxed_section(c, margin, height - 440, width - 2 * margin, "Stav zařízení při převzetí", service_data.get("condition", ""))

        # Cena práce
        c.setFont("DejaVuSans", 10)
        c.drawString(margin, height - 500, f"Cena práce: {service_data.get('price', '0')} Kč")

        # Datum
        c.drawRightString(width - margin, height - 500, f"Datum: {service_data.get('date', '')}")

        c.save()
