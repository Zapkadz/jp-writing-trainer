from PySide6.QtWidgets import QMainWindow, QTabWidget

from app.ui.tabs.writing_tab import WritingTab
from app.ui.tabs.quiz_tab import QuizTab
from app.ui.tabs.grammar_tab import GrammarTab
from app.ui.tabs.settings_tab import SettingsTab


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JP Writing Trainer")
        self.resize(1000, 700)

        tabs = QTabWidget()
        tabs.addTab(WritingTab(), "Writing")
        tabs.addTab(QuizTab(), "Quiz")
        tabs.addTab(GrammarTab(), "Grammar")
        tabs.addTab(SettingsTab(), "Settings")

        self.setCentralWidget(tabs)
