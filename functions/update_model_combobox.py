# Globální proměnné pro vybrané hodnoty
selected_brand = ""
selected_series = ""
selected_model = ""


def update_model_combobox(choice, model_combobox, devices_data):

    models = devices_data.get(choice, [])
    model_combobox.configure(values=models)
    if models:
        model_combobox.set(models[0])
    else:
        model_combobox.set("")

def on_brand_selected(choice, series_combobox, devices_data):
    """
    Když se změní značka, aktualizuj modelové řady.
    """
    global selected_brand
    selected_brand = choice
    series = list(devices_data.get(choice, {}).keys())
    series_combobox.configure(values=series)
    if series:
        series_combobox.set(series[0])
    else:
        series_combobox.set("")

def on_series_selected(choice, model_combobox, devices_data, brand_combobox):
    """
    Když se změní modelová řada, aktualizuj modely.
    """
    global selected_series
    selected_series = choice
    brand = brand_combobox.get()
    models = devices_data.get(brand, {}).get(choice, [])
    model_combobox.configure(values=models)
    if models:
        model_combobox.set(models[0])
    else:
        model_combobox.set("")

# Funkce pro uložení vybraných hodnot
def save_selected_values(brand_combobox, series_combobox, model_combobox):
    global selected_brand, selected_series, selected_model
    selected_brand = brand_combobox.get()
    selected_series = series_combobox.get()
    selected_model = model_combobox.get()
    print(f"Vybráno: {selected_brand} / {selected_series} / {selected_model}")