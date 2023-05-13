MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', 
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', 
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', 
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', 
    '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', 
    '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', 
    '---..': '8', '----.': '9'
}

def morse_code_to_string(code):
    words = code.split('  ')  # Split into words
    text = ''
    for word in words:
        chars = word.split(' ')  # Split into characters
        for char in chars:
            if char in MORSE_CODE_DICT:
                text += MORSE_CODE_DICT[char]
        text += ' '  # Add space between words
    return text.strip()  # Remove leading/trailing spaces

# Take Morse code input from user
code = input('Enter Morse code to convert to text: ')

# Convert Morse code to text and print result
text = morse_code_to_string(code)
print(text)
