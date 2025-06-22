def apply_theme(widget):
    widget.setStyleSheet("""
        QLabel#headerLabel {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        QPushButton#generateButton {
            background-color: #1C658C;
            color: white;
            padding: 8px 16px;
            border-radius: 6px;
        }
        QPushButton#generateButton:hover {
            background-color: #398AB9;
        }
    """)
