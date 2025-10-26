from PySide6.QtWidgets import QVBoxLayout, QWidget, QPushButton, QLabel


class ImageMergeWidget(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app

        layout = QVBoxLayout(self)
        button = QPushButton("Merge")
        self.drop_area = QLabel("Drop Images Here")
        self.drop_area.setAcceptDrops(True)

        layout.addWidget(self.drop_area)
        layout.addWidget(button)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()