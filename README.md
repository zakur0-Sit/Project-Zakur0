# Project Zakur0

A versatile desktop application built with PySide6 that provides various text and image manipulation tools in a user-friendly interface.

## Features

### Text Tools
- **Case Converter**: Transform text between different case styles
  - Lower case
  - Upper case
  - Sentence case
  - Capitalize case
  
- **Encoder/Decoder**: Convert text between different formats
  - Text ↔ Binary
  - Text ↔ Hexadecimal
  - Text ↔ Octal

### Image Tools
- **Image Merge**: Combine multiple images (drag and drop support)
- **OCR** (Planned): Optical Character Recognition from images

### Converter Tools (Planned)
- Image format conversion
- Video conversion
- Audio conversion
- Document conversion

## Installation

### Prerequisites
- Python 3.7+
- PySide6

project_zakur0/
├── main.py                 # Application entry point
├── main_window.py          # Main window implementation
├── widgets/                # UI components
│   ├── home_widget.py
│   ├── case_convertor_widget.py
│   ├── encoder_decoder_widget.py
│   └── image_merge_widget.py
├── managers/               # UI management classes
│   ├── menubar_manager.py
│   └── toolbar_manager.py
├── logic/                  # Business logic
│   ├── case_convertor.py
│   └── encoder_decoder.py
├── resources/              # Application resources
│   └── icons/              # Toolbar icons
└── ui/                     # Styling
    └── style.qss           # Application stylesheet
