import os
import re

def get_current_order_number():
    directory = "zakazky"
    if not os.path.exists(directory):
        return "00000001"

    pdf_files = [f for f in os.listdir(directory) if f.endswith(".pdf") and f.startswith("SE")]
    numbers = []

    for f in pdf_files:
        match = re.search(r"SE(\d{8})", f)
        if match:
            numbers.append(int(match.group(1)))

    if not numbers:
        return "00000001"

    max_number = max(numbers)
    return f"{max_number:08d}"

def get_new_pdf_filename():
    directory = "zakazky"
    if not os.path.exists(directory):
        os.makedirs(directory)

    pdf_files = [f for f in os.listdir(directory) if f.endswith(".pdf") and f.startswith("SE")]
    numbers = []

    for f in pdf_files:
        match = re.search(r"SE(\d{8})", f)
        if match:
            numbers.append(int(match.group(1)))

    next_number = max(numbers) + 1 if numbers else 1
    return os.path.join(directory, f"SE{next_number:08d}.pdf")