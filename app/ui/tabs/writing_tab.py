from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QTextEdit, QPushButton, QPlainTextEdit
)


class WritingTab(QWidget):
    def __init__(self):
        super().__init__()

        root = QVBoxLayout(self)

        title = QLabel("Luyện viết (N3 trở xuống)")
        root.addWidget(title)

        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText("Nhập câu/đoạn tiếng Nhật ở đây… (ví dụ: 昨日、日本語を勉強しました。)")
        root.addWidget(self.input_text)

        row = QHBoxLayout()
        self.btn_check = QPushButton("Kiểm tra")
        self.btn_clear = QPushButton("Xóa")
        row.addWidget(self.btn_check)
        row.addWidget(self.btn_clear)
        row.addStretch()
        root.addLayout(row)

        self.output_box = QPlainTextEdit()
        self.output_box.setReadOnly(True)
        self.output_box.setPlaceholderText("Kết quả sẽ hiển thị ở đây…")
        root.addWidget(self.output_box)

        # Signals
        self.btn_check.clicked.connect(self.on_check_clicked)
        self.btn_clear.clicked.connect(self.on_clear_clicked)

    def on_check_clicked(self):
        text = self.input_text.toPlainText().strip()
        if not text:
            self.output_box.setPlainText("⚠️ Bạn chưa nhập câu nào.")
            return

        # MOCK (Ngày 4 mới gọi Groq)
        mock = (
            "✅ Đánh giá: (MOCK) Chưa chấm thật\n"
            "❌ Lỗi: (MOCK) Chưa phân tích thật\n"
            "✍️ Câu sửa: (MOCK) —\n"
            "📘 Giải thích: (MOCK) Ngày 4 sẽ tích hợp Groq để sửa chi tiết.\n"
        )
        self.output_box.setPlainText(mock)

    def on_clear_clicked(self):
        self.input_text.clear()
        self.output_box.clear()
