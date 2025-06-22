import re
from tkinter import messagebox

def validate_form(customer_name, phone, imei, email):
    errors = []

    # Validace jména
    if not customer_name.strip():
        errors.append("Jméno zákazníka je povinné.")

    # Validace telefonního čísla (jednoduchý formát)
    if not phone or not re.match(r"^\+?\d{9,15}$", phone):
        errors.append("Telefonní číslo je neplatné. Zkontrolujte formát.")

    # Validace IMEI s Luhn algoritmem (pokud je zadáno)
    if imei:
        if not re.match(r"^\d{15}$", imei):
            errors.append("IMEI musí obsahovat přesně 15 číslic.")
        elif not check_imei_luhn(imei):
            errors.append("IMEI není platné podle Luhn algoritmu.")

    # Validace e-mailu
    if email and not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        errors.append("E-mail není platný.")

    # Pokud jsou chyby, zobrazí se je v jednom okně
    if errors:
        messagebox.showerror("Chyby ve formuláři", "\n".join(errors))
        return False

    return True


def check_imei_luhn(imei):
    """
    Validuje IMEI pomocí Luhnova algoritmu.
    IMEI je 15-místné číslo, kde poslední číslice je kontrolní.
    """
    def digits_of(n):
        return [int(x) for x in str(n)]

    digits = digits_of(imei)
    odd_sum = sum(digits[-1::-2])
    even_sum = 0
    for digit in digits[-2::-2]:
        doubled = digit * 2
        even_sum += doubled if doubled < 10 else doubled - 9
    return (odd_sum + even_sum) % 10 == 0
