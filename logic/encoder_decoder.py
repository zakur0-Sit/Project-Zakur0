
def text_binary(text):
    binary_str = ''
    for char in text:
        binary_char = format(ord(char), '08b')
        binary_str += binary_char + ' '

    return binary_str

def binary_text(binary_str):
    try:
        chars = binary_str.split()
        text = ''
        for binary_char in chars:
            text += chr(int(binary_char, 2))
    except ValueError:
        return 'Invalid binary input.'

    return text

def text_hex(text):
    hex_str = ''
    for char in text:
        hex_char = format(ord(char), '02x')
        hex_str += hex_char + ' '

    return hex_str

def hex_text(hex_str):
    try:
        hex_str = hex_str.replace(' ', '')
        bytes_obj = bytes.fromhex(hex_str)
        text = bytes_obj.decode('utf-8', errors='ignore')
    except ValueError:
        return 'Invalid hexadecimal input.'

    return text

def text_octal(text):
    octal_str = ''
    for char in text:
        octal_char = format(ord(char), '03o')
        octal_str += octal_char + ' '

    return octal_str

def octal_text(octal_str):
    try:
        parts = octal_str.split()
        text = ''
        for part in parts:
            text += chr(int(part, 8))
    except ValueError:
        return 'Invalid octal input.'

    return text