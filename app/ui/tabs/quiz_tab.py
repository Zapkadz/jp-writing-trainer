from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QRadioButton,
    QButtonGroup, QPushButton, QGroupBox
)


class QuizTab(QWidget):
    def __init__(self):
        super().__init__()

        root = QVBoxLayout(self)

        title = QLabel("Trắc nghiệm ngữ pháp (1 đáp án đúng)")
        root.addWidget(title)

        # MOCK question (Ngày 3 sẽ lấy từ DB/JSON)
        self.question_text = "私は日本へ＿＿＿行きます。"
        self.correct_index = 1  # "に"

        self.lbl_question = QLabel(self.question_text)
        root.addWidget(self.lbl_question)

        box = QGroupBox("Chọn đáp án")
        box_layout = QVBoxLayout(box)

        self.group = QButtonGroup(self)
        self.choices = ["で", "に", "を", "が"]
        self.radios = []

        for i, c in enumerate(self.choices):
            rb = QRadioButton(c)
            self.group.addButton(rb, i)
            box_layout.addWidget(rb)
            self.radios.append(rb)

        root.addWidget(box)

        self.btn_submit = QPushButton("Nộp")
        root.addWidget(self.btn_submit)

        self.lbl_result = QLabel("Kết quả: —")
        root.addWidget(self.lbl_result)

        self.btn_submit.clicked.connect(self.on_submit)

    def on_submit(self):
        selected = self.group.checkedId()
        if selected == -1:
            self.lbl_result.setText("⚠️ Bạn chưa chọn đáp án.")
            return

        if selected == self.correct_index:
            self.lbl_result.setText("✅ Đúng! Giải thích (MOCK): '行く' đi với trợ từ に.")
        else:
            correct = self.choices[self.correct_index]
            self.lbl_result.setText(f"❌ Sai. Đáp án đúng là '{correct}'. Giải thích (MOCK): '行く' đi với に.")
