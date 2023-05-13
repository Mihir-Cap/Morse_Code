MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', 
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.'
}

def string_to_morse_code(text):
    morse_code = ''
    for char in text.upper():
        if char == ' ':
            morse_code += ' '
        else:
            morse_code += MORSE_CODE_DICT[char] + ' '
    return morse_code

# Take input string from user
text = input('Enter text to convert to Morse code: ')

# Convert input string to Morse code and print result
morse_code = string_to_morse_code(text)
print(morse_code)
