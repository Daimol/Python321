# app/services/pdf_service.py
from app.handler.order_handler import generate_order_pdf

def create_order_pdf(order_number, customer_data, device_data, service_data, company_data, output_dir):
    # Tady můžeš případně doplnit předzpracování dat
    output_file = generate_order_pdf(
        order_number,
        customer_data,
        device_data,
        service_data,
        company_data,
        output_dir
    )
    return output_file