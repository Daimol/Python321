import customtkinter as ctk
from app.gui.app_gui import ZakazkovyListApp

def start_app():
    devices_data = {}  # nebo načti data podle potřeby
    root = ctk.CTk()
    app = ZakazkovyListApp(root, devices_data)
    root.mainloop()

if __name__ == "__main__":
    start_app()
