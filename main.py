import customtkinter as ctk
from functions.device_loader import load_devices
from functions.gui_elements import create_left_frame, create_right_frame, create_bottom_frame
from functions.form_handler import on_generate_button_click

# Načti data zařízení
devices_data = load_devices()

# Vytvoření GUI
root = ctk.CTk()
root.title("Generátor zakázkového listu")
root.geometry("1000x600")
root.eval('tk::PlaceWindow . center')

frame_left, entry_customer_name, entry_phone, entry_imei, entry_email = create_left_frame(root)

frame_right, entry_part_name, entry_part_price, brand_combobox, series_combobox, model_combobox = create_right_frame(root, devices_data)

frame_bottom, entry_labor_price, button_generate = create_bottom_frame(root)

# Přidání akce na tlačítko pro generování PDF
button_generate.configure(command=lambda: on_generate_button_click(entry_customer_name, entry_phone, entry_imei, entry_email,
                                                                  entry_part_name, entry_part_price, entry_labor_price,
                                                                  brand_combobox, model_combobox))

root.mainloop()
