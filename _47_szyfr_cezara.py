# def generate_cipher(alphabet, key=2):
#     result = ''
#
#     word = list(alphabet)
#     for char in word:
#         if char != ' ':
#             result += chr((ord(char) + key))
#         else:
#             result += ' '
#     return result

def generate_cipher(alphabet, key=2):
    cipher = ''
    for letter in alphabet:
        new_idx = (alphabet.index(letter) + key) % len(alphabet)
        cipher += alphabet[new_idx]
    return cipher


print(generate_cipher('Attack at dawn', 2))
