from PySide6.QtWidgets import QWidget, QTextEdit, QPushButton, QHBoxLayout, QVBoxLayout

from projects.ProjectZakur0.logic.case_convertor import lower_case, upper_case, sentence_case, capitalize_case

class CaseConvertorWidget(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app

        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("Enter text here...")

        lower_case_button = QPushButton("Lower Case")
        upper_case_button = QPushButton("Upper Case")
        sentence_case_button = QPushButton("Sentence Case")
        capitalize_case_button = QPushButton("Capitalize Case")
        clear_button = QPushButton("Clear")

        v_layout = QVBoxLayout(self)
        button_layout = QHBoxLayout()

        button_layout.addWidget(lower_case_button)
        button_layout.addWidget(upper_case_button)
        button_layout.addWidget(sentence_case_button)
        button_layout.addWidget(capitalize_case_button)
        button_layout.addWidget(clear_button)

        v_layout.addWidget(self.text_edit)
        v_layout.addLayout(button_layout)

        lower_case_button.clicked.connect(self.convert_to_lower_case)
        upper_case_button.clicked.connect(self.convert_to_upper_case)
        sentence_case_button.clicked.connect(self.convert_to_sentence_case)
        capitalize_case_button.clicked.connect(self.convert_to_capitalize_case)
        clear_button.clicked.connect(self.text_edit.clear)

    def convert_to_lower_case(self):
        original_text = self.text_edit.toPlainText()
        converted_text = lower_case(original_text)
        self.text_edit.setPlainText(converted_text)

    def convert_to_upper_case(self):
        original_text = self.text_edit.toPlainText()
        converted_text = upper_case(original_text)
        self.text_edit.setPlainText(converted_text)

    def convert_to_sentence_case(self):
        original_text = self.text_edit.toPlainText()
        converted_text = sentence_case(original_text)
        self.text_edit.setPlainText(converted_text)

    def convert_to_capitalize_case(self):
        original_text = self.text_edit.toPlainText()
        converted_text = capitalize_case(original_text)
        self.text_edit.setPlainText(converted_text)