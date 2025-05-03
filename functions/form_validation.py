import re
from tkinter import messagebox

def validate_form(customer_name, phone, imei, email):
    errors = []

    # Validace jména
    if not customer_name:
        errors.append("Jméno zákazníka je povinné.")

    # Validace telefonního čísla
    if not phone or not re.match(r"^\+?\d{9,15}$", phone):  # jednoduchá validace pro telefon
        errors.append("Telefonní číslo je neplatné. Zkontrolujte formát.")

    # Validace IMEI (volitelný formát)
    if imei and not re.match(r"^\d{15}$", imei):  # 15 číslic pro IMEI
        errors.append("IMEI není platné, pokud je zadáno.")

    # Validace e-mailu
    if email and not re.match(r"[^@]+@[^@]+\.[^@]+", email):  # jednoduchý email formát
        errors.append("E-mail není platný.")

    # Pokud jsou chyby, zobrazí se pop-up okno
    if errors:
        error_message = "\n".join(errors)
        messagebox.showerror("Chyby ve formuláři", error_message)
        return False

    return True
