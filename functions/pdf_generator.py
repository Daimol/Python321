
from functions.file_utils import get_new_pdf_filename
from fpdf import FPDF

def generate_pdf(customer_name, phone, imei, email, part_name, part_price, labor_price, brand, model):
    # Nastavení PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Načtení fontu DejaVu Sans (nahraď správnou cestou k souboru)
    pdf.add_font('DejaVu', '', 'fonts/DejaVuSans.ttf', uni=True)
    pdf.set_font('DejaVu', '', 12)

    # Přidání informací do PDF
    pdf.cell(200, 10, txt=f"Zakázkový list - {customer_name}", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(100, 10, txt=f"Jméno zákazníka: {customer_name}", ln=True)
    pdf.cell(100, 10, txt=f"Telefonní číslo: {phone}", ln=True)
    pdf.cell(100, 10, txt=f"IMEI: {imei}", ln=True)
    pdf.cell(100, 10, txt=f"E-mail: {email}", ln=True)
    pdf.cell(100, 10, txt=f"Název dílu: {part_name}", ln=True)
    pdf.cell(100, 10, txt=f"Cena dílu: {part_price} Kč", ln=True)
    pdf.cell(100, 10, txt=f"Cena práce: {labor_price} Kč", ln=True)
    pdf.cell(100, 10, txt=f"Značka: {brand}", ln=True)
    pdf.cell(100, 10, txt=f"Model: {model}", ln=True)

    # Získání unikátního názvu souboru
    pdf_filename = get_new_pdf_filename()

    # Uložení PDF
    pdf.output(pdf_filename)


