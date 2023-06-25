# Morse Code Converter

This repository contains two Python scripts that allow conversion between Morse code and text.

## morse_code_to_string.py

This script takes Morse code input from the user and converts it into text using a predefined dictionary. The Morse code dictionary (`MORSE_CODE_DICT`) maps Morse code symbols to corresponding alphabets and numbers. The script splits the input into words and characters, matches each character with its Morse code representation in the dictionary, and constructs the corresponding text. Finally, the converted text is printed as output.

To run the script, execute the following command:

```
python morse_code_to_string.py
```

## string_to_morse_code.py

This script takes a text input from the user and converts it into Morse code using a predefined dictionary. The Morse code dictionary (`MORSE_CODE_DICT`) maps alphabets and numbers to their corresponding Morse code representations. The script iterates through each character in the input text, checks if it is a space or an alphabet/number, and appends the corresponding Morse code representation to the output string. Finally, the converted Morse code is printed as output.

To run the script, execute the following command:

```
python string_to_morse_code.py
```

Feel free to use and modify these scripts to suit your needs. Happy coding!
