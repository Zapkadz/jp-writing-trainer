from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QTextEdit, QPushButton, QPlainTextEdit, QComboBox
)
from PySide6.QtCore import Qt
import random


EXERCISES = [
    {
        "id": 1,
        "vi": "Hôm qua tôi đã học tiếng Nhật ở nhà.",
        "ja": "昨日、家で日本語を勉強しました。",
        "notes": "N3-: trạng từ thời gian + địa điểm + を + động từ"
    },
    {
        "id": 2,
        "vi": "Tôi học tiếng Nhật để đi du học Nhật Bản.",
        "ja": "日本へ留学するために日本語を勉強しています。",
        "notes": "N3: ～ために (mục đích)"
    },
    {
        "id": 3,
        "vi": "Tôi ghi chú để không quên.",
        "ja": "忘れないようにメモします。",
        "notes": "N3: ～ように (mục đích/để không…)"
    }
]


class WritingTab(QWidget):
    def __init__(self):
        super().__init__()

        root = QVBoxLayout(self)

        header = QHBoxLayout()
        header.addWidget(QLabel("Chế độ:"))

        self.mode = QComboBox()
        self.mode.addItems(["VN → JP (Viết tiếng Nhật)", "JP → VN (Dịch tiếng Việt)"])
        header.addWidget(self.mode)

        self.btn_new = QPushButton("Câu mới")
        header.addWidget(self.btn_new)

        header.addStretch()
        root.addLayout(header)

        self.lbl_prompt_title = QLabel("Câu gốc:")
        root.addWidget(self.lbl_prompt_title)

        self.prompt_box = QPlainTextEdit()
        self.prompt_box.setReadOnly(True)
        self.prompt_box.setMaximumHeight(90)
        root.addWidget(self.prompt_box)

        root.addWidget(QLabel("Bài làm của bạn:"))
        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText("Nhập câu bạn viết/dịch ở đây…")
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
        self.output_box.setPlaceholderText("Kết quả phân tích sẽ hiển thị ở đây…")
        root.addWidget(self.output_box)

        # state
        self.current = None
        self.load_new_exercise()

        # signals
        self.btn_new.clicked.connect(self.load_new_exercise)
        self.mode.currentIndexChanged.connect(lambda _: self.load_new_exercise())
        self.btn_check.clicked.connect(self.on_check_clicked)
        self.btn_clear.clicked.connect(self.on_clear_clicked)

    def load_new_exercise(self):
        self.current = random.choice(EXERCISES)
        is_vi2ja = self.mode.currentIndex() == 0

        if is_vi2ja:
            self.prompt_box.setPlainText(self.current["vi"])
            self.input_text.setPlaceholderText("Hãy viết lại câu trên bằng tiếng Nhật…")
        else:
            self.prompt_box.setPlainText(self.current["ja"])
            self.input_text.setPlaceholderText("Hãy dịch câu trên sang tiếng Việt (sát nghĩa, đúng ngữ cảnh)…")

        self.output_box.clear()

    def on_check_clicked(self):
        answer = self.input_text.toPlainText().strip()
        if not answer:
            self.output_box.setPlainText("⚠️ Bạn chưa nhập bài làm.")
            return

        is_vi2ja = self.mode.currentIndex() == 0

        # MOCK output (Ngày 4 mới gọi Groq)
        if is_vi2ja:
            mock = (
                f"🧩 Bài: VN→JP | id={self.current['id']}\n"
                f"📌 Gợi ý ngữ pháp: {self.current['notes']}\n\n"
                "✅ Đánh giá: (MOCK)\n"
                "❌ Lỗi: (MOCK) chưa phân tích\n"
                "✍️ Câu sửa: (MOCK)\n"
                "📘 Giải thích: (MOCK) Ngày 4 sẽ dùng Groq để sửa chi tiết + gợi ý câu tương tự.\n"
            )
        else:
            mock = (
                f"🧩 Bài: JP→VN | id={self.current['id']}\n"
                f"📌 Gợi ý ngữ pháp: {self.current['notes']}\n\n"
                "✅ Đánh giá: (MOCK)\n"
                "🧠 Tách câu: (MOCK) chủ ngữ / trợ từ / động từ / bổ ngữ...\n"
                "📘 Giải thích: (MOCK) Ngày 4 sẽ dùng Groq để phân tích cấu trúc và góp ý dịch.\n"
            )

        self.output_box.setPlainText(mock)

    def on_clear_clicked(self):
        self.input_text.clear()
        self.output_box.clear()
