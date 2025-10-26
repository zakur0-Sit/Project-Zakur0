import os

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon


class ToolBarManager:
    def __init__(self, main_window):
        self.main_window = main_window

    def create_all_toolbars(self):
        self._create_main_toolbar()
        self._create_text_toolbar()
        self._create_image_toolbar()
        self._create_convertor_toolbar()

    def _create_main_toolbar(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        home_icon = os.path.join(base_dir, '../resources/icons/home.png')
        text_icon = os.path.join(base_dir, '../resources/icons/text.png')
        image_icon = os.path.join(base_dir, '../resources/icons/image.png')
        converter_icon = os.path.join(base_dir, '../resources/icons/converter.png')

        self.main_toolbar = self.main_window.addToolBar('Main Toolbar')
        self.main_toolbar.setObjectName('main_toolbar')
        self.main_toolbar.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.main_toolbar.setOrientation(Qt.Vertical)
        self.main_toolbar.setMovable(False)
        self.main_toolbar.setFloatable(False)

        self.action_home = QAction(QIcon(home_icon), 'Home', self.main_window)
        self.action_text_edit = QAction(QIcon(text_icon), 'Text', self.main_window)
        self.action_image_edit = QAction(QIcon(image_icon), 'Image', self.main_window)
        self.action_converter = QAction(QIcon(converter_icon), 'Converter', self.main_window)

        self.main_toolbar.setIconSize(QSize(32, 32))

        self.main_toolbar.addAction(self.action_home)
        self.main_toolbar.addAction(self.action_text_edit)
        self.main_toolbar.addAction(self.action_image_edit)
        self.main_toolbar.addAction(self.action_converter)

        self.main_window.addToolBar(Qt.LeftToolBarArea, self.main_toolbar)

    def _create_text_toolbar(self):
        self.text_toolbar = self.main_window.addToolBar('Text Editing Tools')
        self.text_toolbar.setOrientation(Qt.Vertical)
        self.text_toolbar.setMovable(False)
        self.text_toolbar.setFloatable(False)

        self.text_converter = QAction("Text Converter", self.main_window)
        self.text_converter.setToolTip("Text Converter")

        self.encode_decode = QAction("Encode/Decode", self.main_window)
        self.encode_decode.setToolTip("Encode/Decode Text")

        self.text_toolbar.addAction(self.text_converter)
        self.text_toolbar.addAction(self.encode_decode)

        self.main_window.addToolBar(Qt.RightToolBarArea, self.text_toolbar)
        self.text_toolbar.setVisible(False)

    def _create_image_toolbar(self):
        self.image_toolbar = self.main_window.addToolBar("Image Editing Tools")
        self.image_toolbar.setOrientation(Qt.Vertical)
        self.image_toolbar.setMovable(False)
        self.image_toolbar.setFloatable(False)

        self.image_merge = QAction("Merge", self.main_window)
        self.image_merge.setToolTip("Image Merge")

        self.image_ocr = QAction("OCR", self.main_window)
        self.image_ocr.setToolTip("Image OCR")

        self.image_toolbar.addAction(self.image_merge)
        self.image_toolbar.addAction(self.image_ocr)

        self.main_window.addToolBar(Qt.RightToolBarArea, self.image_toolbar)
        self.image_toolbar.setVisible(False)

    def _create_convertor_toolbar(self):
        self.converter_toolbar = self.main_window.addToolBar("Converter Tools")
        self.converter_toolbar.setOrientation(Qt.Vertical)
        self.converter_toolbar.setMovable(False)
        self.converter_toolbar.setFloatable(False)

        self.convert_image = QAction("Image", self.main_window)
        self.convert_image.setToolTip("Image Converter")

        self.convert_video = QAction("Video", self.main_window)
        self.convert_video.setToolTip("Video Converter")

        self.convert_audio = QAction("Audio", self.main_window)
        self.convert_audio.setToolTip("Audio Converter")

        self.convert_document = QAction("Document", self.main_window)
        self.convert_document.setToolTip("Document Converter")

        self.converter_toolbar.addAction(self.convert_image)
        self.converter_toolbar.addAction(self.convert_video)
        self.converter_toolbar.addAction(self.convert_audio)
        self.converter_toolbar.addAction(self.convert_document)

        self.main_window.addToolBar(Qt.RightToolBarArea, self.converter_toolbar)
        self.converter_toolbar.setVisible(False)

    def hide_all_toolbars(self):
        self.text_toolbar.setVisible(False)
        self.image_toolbar.setVisible(False)
        self.converter_toolbar.setVisible(False)

    def show_specific_toolbar(self, toolbar: str):
        self.hide_all_toolbars()

        if toolbar == 'text':
            self.text_toolbar.setVisible(True)
        elif toolbar == 'image':
            self.image_toolbar.setVisible(True)
        elif toolbar == 'converter':
            self.converter_toolbar.setVisible(True)