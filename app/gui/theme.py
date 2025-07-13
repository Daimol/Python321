from PySide6.QtCore import QPropertyAnimation

def apply_theme(widget):
    widget.setStyleSheet("""
        /* --- Common font & background --- */
        QWidget {
            background-color: #121212;
            color: #E0E0E0;
            font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
            font-size: 14px;
        }

        /* --- Header label --- */
        QLabel#headerLabel {
            font-size: 28px;
            font-weight: 700;
            color: #FFFFFF;
            margin-bottom: 24px;
        }

        /* --- Push Button --- */
        QPushButton#generateButton {
            background: qlineargradient(
                x1:0, y1:0, x2:0, y2:1,
                stop:0 #3A8DFF, stop:1 #0052CC
            );
            color: white;
            border-radius: 8px;
            padding: 12px 24px;
            font-weight: 600;
            box-shadow: 0 4px 8px rgba(58, 141, 255, 0.6);
            border: none;
            transition: all 0.3s ease;
        }
        QPushButton#generateButton:hover {
            background: qlineargradient(
                x1:0, y1:0, x2:0, y2:1,
                stop:0 #1C6CF0, stop:1 #003EA6
            );
            box-shadow: 0 6px 14px rgba(28, 108, 240, 0.9);
        }
        QPushButton#generateButton:pressed {
            background: #003EA6;
            box-shadow: none;
            padding-top: 14px;
            padding-bottom: 10px;
        }

        /* --- Line Edit --- */
        QLineEdit {
            background-color: #1E1E1E;
            border: 2px solid #3A8DFF;
            border-radius: 6px;
            padding: 8px;
            color: #E0E0E0;
            font-size: 14px;
            selection-background-color: #3A8DFF;
            selection-color: #fff;
        }
        QLineEdit:focus {
            border-color: #1C6CF0;
            background-color: #272727;
        }

        /* --- ComboBox --- */
        QComboBox {
            background-color: #1E1E1E;
            border: 2px solid #3A8DFF;
            border-radius: 6px;
            padding: 6px 12px;
            color: #E0E0E0;
            font-size: 14px;
        }
        QComboBox:hover {
            border-color: #1C6CF0;
        }
        QComboBox:focus {
            border-color: #1C6CF0;
            background-color: #272727;
        }
        QComboBox::drop-down {
            border: none;
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 20px;
            background: transparent;
        }
        QComboBox::down-arrow {
            image: url(:/icons/arrow_down_white.png); /* Pokud máš ikonku, jinak můžeš nechat default */
            width: 14px;
            height: 14px;
        }

        /* --- Scrollbar styl --- */
        QScrollBar:vertical {
            background: #1E1E1E;
            width: 12px;
            margin: 0px 0px 0px 0px;
            border-radius: 6px;
        }
        QScrollBar::handle:vertical {
            background: #3A8DFF;
            min-height: 20px;
            border-radius: 6px;
        }
        QScrollBar::handle:vertical:hover {
            background: #1C6CF0;
        }
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            height: 0;
        }
    """)


def animate_button(button):
    """
    Přidá lehkou animaci na změnu velikosti tlačítka při hoveru.
    """
    animation = QPropertyAnimation(button, b"geometry")
    animation.setDuration(200)

    def on_enter():
        rect = button.geometry()
        animation.stop()
        animation.setStartValue(rect)
        animation.setEndValue(rect.adjusted(-5, -3, 5, 3))
        animation.start()

    def on_leave():
        rect = button.geometry()
        animation.stop()
        animation.setStartValue(rect)
        animation.setEndValue(rect.adjusted(5, 3, -5, -3))
        animation.start()

    button.enterEvent = lambda event: (on_enter(), button.enterEvent(event) if callable(getattr(button, "enterEvent", None)) else None)
    button.leaveEvent = lambda event: (on_leave(), button.leaveEvent(event) if callable(getattr(button, "leaveEvent", None)) else None)
