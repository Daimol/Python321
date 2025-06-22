from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Signal

class GenerateButton(QPushButton):
    clicked_custom = Signal()

    def __init__(self, parent=None):
        super().__init__("Generovat", parent)
        self.setObjectName("generateButton")
        self.clicked.connect(self._on_clicked)

    def _on_clicked(self):
        self.clicked_custom.emit()
