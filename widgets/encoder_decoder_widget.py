from PySide6.QtWidgets import QWidget, QLabel, QComboBox, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout

from projects.ProjectZakur0.logic.encoder_decoder import text_hex, hex_text, text_binary, binary_text, text_octal, octal_text

class EncoderDecoderWidget(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle('Encoder/Decoder Widget')

        label = QLabel('Conversion type : ')
        self.combo = QComboBox()
        self.input_text = QTextEdit()
        self.output_text = QTextEdit()
        self.transform_button = QPushButton('Transform')
        self.clear_button = QPushButton('Clear')
        layout = QVBoxLayout(self)
        button_layout = QHBoxLayout()

        self.input_text.setPlaceholderText('Enter text here...')
        self.output_text.setPlaceholderText('The result will appear here...')
        self.output_text.setReadOnly(True)

        self.combo.addItems([
            'Text → Binary',
            'Binary → Text',
            'Text → Hex',
            'Hex → Text',
            'Text → Octal',
            'Octal → Text',
            ])

        button_layout.addWidget(self.transform_button)
        button_layout.addWidget(self.clear_button)

        layout.addWidget(label)
        layout.addWidget(self.combo)
        layout.addWidget(self.input_text)
        layout.addLayout(button_layout)
        layout.addWidget(self.output_text)

        self.text = self.input_text.toPlainText().strip()
        self.mode = self.combo.currentText()

        self.transform_button.clicked.connect(self.convert_text)
        self.clear_button.clicked.connect(self.clear_fields)

    def convert_text(self):
        text = self.input_text.toPlainText().strip()
        mode = self.combo.currentText()

        if not text:
            self.output_text.setPlainText('No text inputted. Please enter text first.')
            return

        try:
            match mode:
                case 'Text → Binary':
                    result = text_binary(text)
                case 'Binary → Text':
                    result = binary_text(text)
                case 'Text → Hex':
                    result = text_hex(text)
                case 'Hex → Text':
                    result = hex_text(text)
                case 'Text → Octal':
                    result = text_octal(text)
                case 'Octal → Text':
                    result = octal_text(text)
                case _:
                    result = 'Invalid conversion type selected.'
        except Exception as e:
            result = f'An error occurred: {str(e)}'

        self.output_text.setPlainText(result)

    def clear_fields(self):
        self.input_text.clear()
        self.output_text.clear()