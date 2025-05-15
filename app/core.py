from app.gui import ZakazkovyListApp
from app.data_loader import load_devices
import customtkinter as ctk

def start_app():
    devices_data = load_devices()
    root = ctk.CTk()
    app = ZakazkovyListApp(root, devices_data)
    root.mainloop()
