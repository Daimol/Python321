
from functions.device_loader import load_devices
from functions.create_gui import create_gui
from functions.form_handler import on_generate_button_click


import customtkinter as ctk

def get_next_order_number():
    # Tato funkce by měla načítat číslo zakázky z nějakého souboru nebo databáze a inkrementovat ho
    # Příklad:
    current_order_number = 12345  # Načtení aktuálního čísla zakázky
    return current_order_number + 1

def update_order_label(label):
    next_number = get_next_order_number()
    label.configure(text=f"Zakázka: SE{next_number:08d}")

    def update_order_label(label):
        next_number = get_next_order_number()  # Tato funkce by měla vracet další číslo zakázky
        label.configure(text=f"Zakázka: SE{next_number:08d}")

    # Funkce pro vytvoření GUI
    def setup_gui(root, devices_data):
        # Vytvoření GUI a získání všech widgetů včetně čísla zakázky
        elements = create_gui(root, devices_data)

        # Aktualizace čísla zakázky
        update_order_label(elements["label_order_number"])



def start_app():
    """Hlavní funkce pro řízení aplikace."""

    # Načteme data zařízení
    devices_data = load_devices()

    # Inicializace hlavního okna
    root = ctk.CTk()
    root.title("Generátor zakázkového listu")
    root.geometry("1000x600")
    root.minsize(800, 500)
    ctk.set_appearance_mode("dark")

    # Vytvoření GUI
    elements = create_gui(root, devices_data)

    elements["button_generate"].configure(command=lambda: on_generate_button_click(elements))

    # Nastavení pozice okna na střed obrazovky
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 3) - (window_width // 2)
    y = (screen_height // 3) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Spuštění hlavní smyčky aplikace
    root.mainloop()
