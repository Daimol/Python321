from functions.device_loader import load_devices
from functions.create_gui import create_gui
from functions.form_handler import on_generate_button_click
import customtkinter as ctk




def start_app():
    """Hlavní funkce pro řízení aplikace."""

    # Načteme data zařízení
    devices_data = load_devices()

    # Inicializace hlavního okna
    root = ctk.CTk()
    root.title("Generátor zakázkového listu")
    root.geometry("1000x800")
    root.minsize(800, 550)
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
