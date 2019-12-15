import random

from utils import get_alphabet, read_file_to_string, write_string_to_file
from constants import INPUT_FILENAME, OUPUT_FILENAME, ALPHABET

extra_symbols = [',', '.', ':', '-', '#', '!', '?', '€', '$', ';', "'", '"', '(', ')', '=']

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ä', 'ö', 'ü', 'ß']


def remove_extra_symbols(text):
    ret = []
    for c in text:
        if c not in extra_symbols:
            ret.append(c)
    return ''.join(ret)


def encrypt(plain):
    #alphabet = get_alphabet()
    key = ALPHABET[:]
    random.shuffle(key)
    encryption = dict(zip(alphabet, key))

    #build an encrypted string
    ciphertext = ''
    for letter in plain:
        try:
            ciphertext += encryption[letter]
        except:
            ciphertext += letter

    return ciphertext


# read the plaintext file
PLAINTEXT = read_file_to_string(INPUT_FILENAME)
PLAINTEXT = remove_extra_symbols(PLAINTEXT)
print('\n plain text: \n', PLAINTEXT)


# encrypt
CRYPTED_TEXT = encrypt(PLAINTEXT.lower())

print('\n encrypted text: \n', CRYPTED_TEXT)
write_string_to_file(OUPUT_FILENAME, CRYPTED_TEXT)
