import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFont, QFontDatabase

from app.ui.main_window import MainWindow


def set_best_font(app: QApplication) -> str | None:
    # Danh sách font ưu tiên (có font nào thì dùng font đó)
    candidates = [
    "Noto Sans",        # ưu tiên tiếng Việt
    "DejaVu Sans",
    "Noto Sans CJK JP", # fallback tiếng Nhật
    "IPAexGothic",
]


    available = set(QFontDatabase.families())
    for name in candidates:
        if name in available:
            app.setFont(QFont(name, 11))
            return name
    return None


def main():
    app = QApplication(sys.argv)

    chosen = set_best_font(app)
    print("Using font:", chosen)

    w = MainWindow()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
