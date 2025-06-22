from PySide6.QtWidgets import QWidget, QFormLayout, QLineEdit

class OrderSection(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        self.desc_input = QLineEdit()
        self.layout.addRow("Popis zakázky:", self.desc_input)

    def get_order_description(self) -> str:
        return self.desc_input.text()
