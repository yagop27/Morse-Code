morse_alphabet = {'a': '*-', 'b': '-***', 'c': '-*-*', 'd': '-**', 'e': '*', 'f': '**-*',
                  'g': '--*', 'h': '****', 'i': '**', 'j': '*---', 'k': '-*-', 'l': '*-**',
                  'm': '--', 'n': '-*', 'o': '---', 'p': '*--*', 'q': '--*-', 'r': '*-*',
                  's': '***', 't': '-', 'u': '**-', 'v': '***-', 'w': '*--', 'x': '-**-',
                  'y': '-*--', 'z': '--**', '0': '-----', '1': '*----', '2': '**---',
                  '3': '***--', '4': '****-', '5': '*****', '6': '-****', '7': '--***',
                  '8': '---**', '9': '----*', '.': '*-*-*-', ',': '--**--', '?': '**--**'}


def morse_converter(string: str) -> str:
    try:
        # Converting the characters in morse code into a list
        morse_code = ['/ 'if char == ' ' else morse_alphabet[char] + ' ' for char in string.lower()]
    except KeyError:
        print('There are invalid characters in the string.')
        return morse_converter(input('Type in the text you want to convert into morse code: '))
    return ''.join(morse_code)  # Transforming the list into a string


print(morse_converter(input('Type in the text you want to convert into morse code: ')))
