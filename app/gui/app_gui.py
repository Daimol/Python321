from app.services.product_loader import load_products, get_brands, get_models_by_brand

from PySide6.QtWidgets import (
    QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QPushButton, QComboBox, QLineEdit, QTextEdit
)


class ZakazkovyListApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Zakázkový list")
        self.setMinimumSize(1000, 700)

        # Načteme produkty
        self.products = load_products("product/apple.json")

        self._init_ui()

    def _init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # --- Top panel ---
        top_bar = QHBoxLayout()
        top_bar.addWidget(QLabel("[Logo]"))
        top_bar.addStretch()
        top_bar.addWidget(QLabel("Zakázka č. SE-001"))
        top_bar.addStretch()
        top_bar.addWidget(QLabel("[Logo]"))
        main_layout.addLayout(top_bar)

        columns_layout = QHBoxLayout()

        # Levý sloupec
        left_col = QVBoxLayout()
        left_col.addWidget(QLabel("Zákazník"))
        left_col.addWidget(QLineEdit("Jméno"))
        left_col.addWidget(QLineEdit("Telefon"))
        left_col.addWidget(QLineEdit("Email"))
        left_col.addWidget(QLabel("Zařízení"))
        left_col.addWidget(QComboBox())
        left_col.addWidget(QLabel("Práce"))
        left_col.addWidget(QComboBox())
        left_col.addWidget(QLabel("Cena práce + díly: 0 Kč"))

        # Střední sloupec
        center_col = QVBoxLayout()
        center_col.addWidget(QLabel("IMEI"))
        center_col.addWidget(QLineEdit())
        center_col.addWidget(QLabel("Značka"))

        self.brand_combo = QComboBox()
        self.brand_combo.addItems(get_brands(self.products))
        self.brand_combo.currentTextChanged.connect(self.update_models)
        center_col.addWidget(self.brand_combo)

        center_col.addWidget(QLabel("Modelová řada"))
        center_col.addWidget(QComboBox())  # Může být později propojeno
        center_col.addWidget(QLabel("Model"))

        self.model_combo = QComboBox()
        center_col.addWidget(self.model_combo)
        self.update_models(self.brand_combo.currentText())  # Inicializace

        center_col.addWidget(QLabel("Použité díly"))
        center_col.addWidget(QTextEdit())

        # Pravý sloupec
        right_col = QVBoxLayout()
        right_col.addWidget(QLabel("Stav zařízení při převzetí"))
        right_col.addWidget(QTextEdit())
        right_col.addWidget(QLabel("Návrh opravy"))
        right_col.addWidget(QTextEdit())
        right_col.addWidget(QLabel("Příslušenství / doplňující info"))
        right_col.addWidget(QTextEdit())

        columns_layout.addLayout(left_col)
        columns_layout.addLayout(center_col)
        columns_layout.addLayout(right_col)

        main_layout.addLayout(columns_layout)

        footer = QHBoxLayout()
        footer.addStretch()
        footer.addWidget(QPushButton("Generovat PDF"))
        footer.addWidget(QPushButton("AI návrh"))
        footer.addWidget(QPushButton("Ověřit díly"))
        footer.addStretch()
        main_layout.addLayout(footer)

    def update_models(self, selected_brand):
        models = get_models_by_brand(self.products, selected_brand)
        self.model_combo.clear()
        self.model_combo.addItems(models)
