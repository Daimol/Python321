import json
import os

def load_devices():
    script_dir = os.path.dirname(os.path.abspath(__file__))  # složka, kde je aktuální soubor
    devices_path = os.path.join(script_dir, "../data/devices.json")  # cesta k devices.json
    devices_path = os.path.normpath(devices_path)  # pro jistotu správné lomítka

    print("Načítám ze souboru:", devices_path)  # Debug info

    with open(devices_path, "r", encoding="utf-8") as f:
        return json.load(f)
