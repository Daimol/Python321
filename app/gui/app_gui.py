import os
from app.handler.generate_handler import GenerateHandler
from PySide6.QtGui import QPixmap, QIcon
from app.services.company_info import get_data

from PySide6.QtWidgets import (
    QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QPushButton, QComboBox, QLineEdit, QTextEdit, QMessageBox
)
from app.gui.theme import apply_theme
from app.services.product_loader import load_all_products, get_brands, get_models_by_brand


PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LOGO_PATH = os.path.join(PROJECT_ROOT, "resources", "icons", "ikonaW.ico")

class ZakazkovyListApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Zakázkový list")
        self.setMinimumSize(1000, 700)
        self.setWindowIcon(QIcon(LOGO_PATH))
        self.data_dir = os.path.join(PROJECT_ROOT, "app", "data")
        os.makedirs(self.data_dir, exist_ok=True)
        self.all_products = load_all_products("product")
        self.products = []
        self._init_ui()
        apply_theme(self)

        self.data_dir = os.path.join(PROJECT_ROOT, "app", "data")
        os.makedirs(self.data_dir, exist_ok=True)

        # Tady je správné místo pro vytvoření instance handleru
        self.generate_handler = GenerateHandler(self.data_dir)

    def _init_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)

        # --- Top bar ---
        top_bar = QHBoxLayout()
        logo_label = QLabel()
        pixmap = QPixmap(LOGO_PATH)
        logo_label.setPixmap(pixmap)
        logo_label.setScaledContents(True)
        logo_label.setFixedSize(200, 150)
        logo_label.setContentsMargins(20, 20, 0, 0)
        top_bar.addWidget(logo_label)
        top_bar.addStretch()
        self.order_label = QLabel("Zakázka č. SE-001")
        top_bar.addWidget(self.order_label)
        top_bar.addStretch()
        main_layout.addLayout(top_bar)

        # --- Columns ---
        left_col = QVBoxLayout()
        left_col.addWidget(QLabel("Zákazník"))
        self.customer_name = QLineEdit()
        self.customer_name.setPlaceholderText("Jméno")
        left_col.addWidget(self.customer_name)
        self.customer_phone = QLineEdit()
        self.customer_phone.setPlaceholderText("Telefon")
        left_col.addWidget(self.customer_phone)
        self.customer_email = QLineEdit()
        self.customer_email.setPlaceholderText("Email")
        left_col.addWidget(self.customer_email)
        self.customer_adresa = QLineEdit()  # Přidané pole
        self.customer_adresa.setPlaceholderText("Adresa")
        left_col.addWidget(self.customer_adresa)

        left_col.addWidget(QLabel("Práce"))
        self.work_combo = QComboBox()
        self.work_combo.addItems(["Oprava displeje", "Výměna baterie", "Čištění"])
        left_col.addWidget(self.work_combo)

        self.price_label = QLabel("Cena práce + díly: 0 Kč")
        left_col.addWidget(self.price_label)

        center_col = QVBoxLayout()
        center_col.addWidget(QLabel("IMEI"))
        self.imei_edit = QLineEdit()
        center_col.addWidget(self.imei_edit)

        center_col.addWidget(QLabel("Zařízení"))
        self.device_combo = QComboBox()
        self.device_combo.addItems(self.all_products.keys())
        self.device_combo.currentTextChanged.connect(self.on_device_selected)
        center_col.addWidget(self.device_combo)

        center_col.addWidget(QLabel("Modelová řada"))
        self.series_combo = QComboBox()
        self.series_combo.currentTextChanged.connect(self.update_models)
        center_col.addWidget(self.series_combo)

        center_col.addWidget(QLabel("Model"))
        self.model_combo = QComboBox()
        center_col.addWidget(self.model_combo)

        center_col.addWidget(QLabel("Použité díly"))
        self.used_parts_edit = QTextEdit()
        center_col.addWidget(self.used_parts_edit)

        right_col = QVBoxLayout()
        right_col.addWidget(QLabel("Stav zařízení při převzetí"))
        self.condition_edit = QTextEdit()
        right_col.addWidget(self.condition_edit)

        right_col.addWidget(QLabel("Návrh opravy"))
        self.repair_edit = QTextEdit()
        right_col.addWidget(self.repair_edit)

        right_col.addWidget(QLabel("Příslušenství / doplňující info"))
        self.accessories_edit = QTextEdit()
        right_col.addWidget(self.accessories_edit)

        cols_layout = QHBoxLayout()
        cols_layout.addLayout(left_col)
        cols_layout.addLayout(center_col)
        cols_layout.addLayout(right_col)
        main_layout.addLayout(cols_layout)

        # --- Footer ---
        footer = QHBoxLayout()
        footer.addStretch()
        gen_btn = QPushButton("Generovat PDF")
        gen_btn.clicked.connect(self.on_generate_pdf)
        footer.addWidget(gen_btn)
        footer.addWidget(QPushButton("AI návrh"))
        footer.addWidget(QPushButton("Ověřit díly"))
        footer.addStretch()
        main_layout.addLayout(footer)

        self.on_device_selected(self.device_combo.currentText())

    def on_device_selected(self, device_name):
        self.products = self.all_products.get(device_name, [])
        self.series_combo.clear()
        self.series_combo.addItems(get_brands(self.products))
        self.update_models(self.series_combo.currentText())

    def update_models(self, brand):
        models = get_models_by_brand(self.products, brand)
        self.model_combo.clear()
        self.model_combo.addItems(models)

    def on_generate_pdf(self):
        # získání servisních dat ze služby
        company_data = get_data()

        gui_data = {
            "order_number": "SE-001",
            "customer_data": {
                "Jméno": self.customer_name.text(),
                "Telefon": self.customer_phone.text(),
                "Email": self.customer_email.text(),
                "Adresa": self.customer_adresa.text()
            },
            "device_data": {
                "desc": f"{self.device_combo.currentText()} {self.series_combo.currentText()} {self.model_combo.currentText()}",
                "imei": self.imei_edit.text()
            },
            "service_data": {
                "repair": self.repair_edit.toPlainText(),
                "condition": self.condition_edit.toPlainText(),
                "price": self.price_label.text().replace("Cena práce + díly: ", "").replace(" Kč", ""),
                # "date" se doplní v handleru
            },
            # místo pevného company_data je to teď z CompanyInfo
            "company_data": company_data
        }

        try:
            output_file = self.generate_handler.handle_generate(gui_data)
            QMessageBox.information(self, "Hotovo", f"PDF bylo vygenerováno: {output_file}")
        except Exception as e:
            QMessageBox.critical(self, "Chyba", f"Nastala chyba při generování PDF:\n{e}")
