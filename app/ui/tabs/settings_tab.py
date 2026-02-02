from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton


class SettingsTab(QWidget):
    def __init__(self):
        super().__init__()

        root = QVBoxLayout(self)

        root.addWidget(QLabel("Thiết lập (Groq)"))

        root.addWidget(QLabel("Groq API Key (sẽ dùng ở Ngày 4):"))
        self.api_key = QLineEdit()
        self.api_key.setEchoMode(QLineEdit.Password)
        self.api_key.setPlaceholderText("gsk_... (không commit lên GitHub)")
        root.addWidget(self.api_key)

        root.addWidget(QLabel("Model:"))
        self.model = QComboBox()
        self.model.addItems([
            "llama-3.1-8b-instant",
            "llama-3.3-70b-versatile",
        ])
        root.addWidget(self.model)

        self.btn_save = QPushButton("Lưu (MOCK)")
        root.addWidget(self.btn_save)

        self.status = QLabel("Trạng thái: chưa lưu")
        root.addWidget(self.status)

        self.btn_save.clicked.connect(self.on_save)

        root.addStretch()

    def on_save(self):
        # Ngày 4-6 mới lưu thật vào SQLite/.env
        self.status.setText("Trạng thái: (MOCK) đã nhận API key & model")
