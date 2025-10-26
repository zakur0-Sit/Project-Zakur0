from PySide6.QtWidgets import QMainWindow, QStackedWidget

from managers.menubar_manager import MenuBarManager
from managers.toolbar_manager import ToolBarManager

from widgets.home_widget import HomeWidget
from widgets.case_convertor_widget import CaseConvertorWidget
from widgets.encoder_decoder_widget import EncoderDecoderWidget
from widgets.image_merge_widget import ImageMergeWidget

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Project Zakur0")
        self.resize(900, 600)

        # Menubar
        self.menubar_manager = MenuBarManager(self)
        self.menubar_manager.create_menubar()

        # Toolbar
        self.toolbar_manager = ToolBarManager(self)
        self.toolbar_manager.create_all_toolbars()

        # stacked widget
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        self._create_widgets()

        self._connect_signals()
        self._load_styles()

        self.stacked_widget.setCurrentIndex(0)

    def _connect_signals(self):
        # connections
        toolbar = self.toolbar_manager

        toolbar.action_home.triggered.connect(self.show_home)
        toolbar.action_text_edit.triggered.connect(self.show_text_toolbar)
        toolbar.action_image_edit.triggered.connect(self.show_image_toolbar)
        toolbar.action_converter.triggered.connect(self.show_converter_toolbar)

        toolbar.text_converter.triggered.connect(self.show_case_converter)
        toolbar.action_text_edit.triggered.connect(self.show_case_converter)
        toolbar.encode_decode.triggered.connect(self.show_encoder_decoder)

        toolbar.image_merge.triggered.connect(self.show_image_merge)
        toolbar.action_image_edit.triggered.connect(self.show_image_merge)

    def _create_widgets(self):
        self.home_widget = HomeWidget(self.app)
        self.stacked_widget.addWidget(self.home_widget)

        self.case_converter_widget = CaseConvertorWidget(self.app)
        self.stacked_widget.addWidget(self.case_converter_widget)

        self.encoder_decoder_widget = EncoderDecoderWidget(self.app)
        self.stacked_widget.addWidget(self.encoder_decoder_widget)

        self.image_merge_widget = ImageMergeWidget(self.app)
        self.stacked_widget.addWidget(self.image_merge_widget)

    def show_home(self):
        self.toolbar_manager.hide_all_toolbars()
        self.stacked_widget.setCurrentIndex(0)

    def show_text_toolbar(self):
        self.toolbar_manager.show_specific_toolbar('text')

    def show_image_toolbar(self):
        self.toolbar_manager.show_specific_toolbar('image')

    def show_converter_toolbar(self):
        self.toolbar_manager.show_specific_toolbar('converter')


    def show_case_converter(self):
        self.stacked_widget.setCurrentIndex(1)

    def show_encoder_decoder(self):
        self.stacked_widget.setCurrentIndex(2)

    def show_image_merge(self):
        self.stacked_widget.setCurrentIndex(3)

    def _load_styles(self):
        try:
            with open("ui/style.qss", "r") as f:
                self.setStyleSheet(f.read())
        except FileNotFoundError:
            print("style.qss not found.")