import customtkinter as ctk
from functions.device_loader import load_devices
from functions.create_gui import create_gui
from functions.form_handler import on_generate_button_click

class ZakazkovyListApp:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        self.devices_data = load_devices()

        self.root = ctk.CTk()
        self.root.title("Generátor zakázkového listu")
        self.root.geometry("1000x800")
        self.root.minsize(800, 550)

        self.elements = create_gui(self.root, self.devices_data)
        self.elements["button_generate"].configure(command=self.on_generate_button_click)

        self.center_window()

    def center_window(self):
        self.root.update_idletasks()  # aktualizuje info o okně
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 3) - (window_width // 2)
        y = (screen_height // 3) - (window_height // 2)
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def on_generate_button_click(self):
        on_generate_button_click(self.elements)

    def run(self):
        self.root.mainloop()


def start_app():
    app = ZakazkovyListApp()
    app.run()
