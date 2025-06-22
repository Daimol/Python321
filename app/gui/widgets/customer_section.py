from PySide6.QtWidgets import QWidget, QFormLayout, QLineEdit

class CustomerSection(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        self.name_input = QLineEdit()
        self.layout.addRow("Zákazník:", self.name_input)

    def get_customer_name(self) -> str:
        return self.name_input.text()
