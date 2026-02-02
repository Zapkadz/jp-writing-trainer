from PySide6.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout,
    QListWidget, QTextBrowser, QLabel
)


class GrammarTab(QWidget):
    def __init__(self):
        super().__init__()

        root = QHBoxLayout(self)

        left = QVBoxLayout()
        left.addWidget(QLabel("Danh sách ngữ pháp (MOCK)"))

        self.list_widget = QListWidget()
        self.list_widget.addItems(["～ように", "～ために", "～ことになる", "～ながら"])
        left.addWidget(self.list_widget)

        root.addLayout(left, 2)

        right = QVBoxLayout()
        right.addWidget(QLabel("Chi tiết"))
        self.detail = QTextBrowser()
        self.detail.setHtml("<b>Chọn một mục bên trái</b>")
        right.addWidget(self.detail)

        root.addLayout(right, 5)

        self.list_widget.currentTextChanged.connect(self.on_select)

    def on_select(self, text: str):
        # MOCK details (Ngày 3 sẽ lấy từ SQLite)
        if text == "～ように":
            html = (
                "<h3>～ように</h3>"
                "<p><b>Nghĩa:</b> để… (mục đích, thường với điều khó kiểm soát)</p>"
                "<p><b>Ví dụ:</b> 忘れないようにメモします。</p>"
            )
        elif text == "～ために":
            html = (
                "<h3>～ために</h3>"
                "<p><b>Nghĩa:</b> để… (mục đích, chủ động)</p>"
                "<p><b>Ví dụ:</b> 日本へ留学するために日本語を勉強しています。</p>"
            )
        elif text == "～ことになる":
            html = (
                "<h3>～ことになる</h3>"
                "<p><b>Nghĩa:</b> trở thành… / được quyết định là…</p>"
                "<p><b>Ví dụ:</b> 来月から日本で働くことになりました。</p>"
            )
        else:  # ～ながら
            html = (
                "<h3>～ながら</h3>"
                "<p><b>Nghĩa:</b> vừa… vừa…</p>"
                "<p><b>Ví dụ:</b> 音楽を聞きながら勉強します。</p>"
            )
        self.detail.setHtml(html)
