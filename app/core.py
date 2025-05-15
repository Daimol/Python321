import customtkinter as ctk
from app.gui.app_gui import ZakazkovyListApp
from app.data_loader import load_devices

def start_app():
    root = ctk.CTk()
    devices_data = load_devices()
    _app = ZakazkovyListApp(root, devices_data)
    root.mainloop()
