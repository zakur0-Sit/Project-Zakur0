from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class HomeWidget(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Home - Project Zakuro")

        label = QLabel("Welcome to Project Zakur0!")
        layout = QVBoxLayout(self)

        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        self.setLayout(layout)