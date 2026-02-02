import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

def main():
    app = QApplication(sys.argv)
    w = QMainWindow()
    w.setWindowTitle("JP Writing Trainer")
    w.setCentralWidget(QLabel("Hello!"))
    w.resize(900, 600)
    w.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
