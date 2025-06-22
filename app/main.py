from PySide6.QtWidgets import QApplication
from app.gui.app_gui import ZakazkovyListApp
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ZakazkovyListApp()
    window.show()
    sys.exit(app.exec())

