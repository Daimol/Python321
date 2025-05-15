import os
import json

def load_devices():
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'devices.json')
    with open(file_path, encoding='utf-8') as f:
        return json.load(f)
