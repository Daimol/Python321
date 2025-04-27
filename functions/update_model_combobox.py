def update_model_combobox(brand, devices_data, model_combobox):
    """Aktualizuje modely v comboboxu na základě vybrané značky."""
    models = devices_data.get(brand, [])
    model_combobox.set_values(models)
