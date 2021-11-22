MORSE_CODE = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    '&': '.-...',
    '@': '.--.-.',
    ':': '---...',
    ',': '--..--',
    '.': '.-.-.-',
    ''': '.----.',
    ''': '.-..-.',
    '?': '..--..',
    '/': '-..-.',
    '=': '-...-',
    '+': '.-.-.',
    '-': '-....-',
    '(': '-.--.',
    ')': '-.--.-',
    '!': '-.-.--',
}


class MorseCode:

    @staticmethod
    def encrypt(word):
        code = ''
        for letter in word:
            letter.upper()
            if letter == ' ':
                code += '/ '
            else:
                code += MORSE_CODE[letter] + ' '
        return code.rstrip()

    @staticmethod
    def decrypt(string):
        code = string.split(' ')
        print(code)
        decode = ''
        for letter in code:
            if letter == '/':
                decode += ' '
            for key, value in MORSE_CODE.items():
                if letter == value:
                    decode += key
        return decode


slowo = 'PYTHON 3.9'
kod = '.--. -.-- - .... --- -. / ...-- .-.-.- ----.'

print(MorseCode.encrypt(slowo))
print(MorseCode.decrypt(kod))
