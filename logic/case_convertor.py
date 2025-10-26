import re

def sentence_case(text):
    text = text.lower()
    parts = re.split('([.!?]\\s*)', text)
    return ''.join(
        parts[i].strip().capitalize() + (parts[i + 1] if i + 1 < len(parts) else '')
        for i in range(0, len(parts), 2))

def lower_case(text):
    return text.lower()

def upper_case(text):
    return text.upper()

def capitalize_case(text):
    return text.capitalize()

# while True:
#     text = input("Enter text (or 'exit' to quit): ")
#
#     if text.lower() == 'exit':
#         break
#
#     case = input('Select case [1] Upper Case, [2] Lower Case, [3] Sentence Case, [4] Capitalize Case: ')
#     match case:
#         case '1':
#             print(upper_case(text))
#         case '2':
#             print(lower_case(text))
#         case '3':
#             print(sentence_case(text))
#         case '4':
#             print(capitalize_case(text))
#         case _:
#             print("Invalid option. Please select 1, 2, 3 or 4.")