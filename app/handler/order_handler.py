import os
from app.core.pdf_generator import PDFGenerator

def generate_order_pdf(order_number, customer_data, device_data, service_data, company_data, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    filename = f"zakazkovy_list_{order_number}.pdf"
    output_path = os.path.join(output_dir, filename)

    pdf_gen = PDFGenerator()
    pdf_gen.generate_pdf(output_path, order_number, customer_data, device_data, service_data, company_data)

    return output_path
