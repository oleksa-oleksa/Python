import random

"""
This tool solves monoalphabetic substitution ciphers, also known as cryptograms.
These are ciphers where each letter of the clear text is replaced by a corresponding
letter of the cipher alphabet.

Using the paper: https://www.aclweb.org/anthology/C14-1218.pdf
"""

# The first step is to calculate the frequency distribution of the letters in the cipher text.
# Lists are sorted by the frequencies of the letters
frequency_german = [16.93, 10.53, 8.02, 6.89, 6.42, 5.79, 5.58, 4.98, 4.98, 3.83, 3.60, 3.16, 3.02, 2.55, 2.24, 1.96,
                    1.78, 1.49, 1.32, 1.21, 0.84, 0.67, 0.65, 0.54, 0.37, 0.30, 0.24, 0.05, 0.05, 0.02]
letters_german = ['E', 'N', 'I', 'R', 'S', 'T', 'A', 'D', 'H', 'U', 'L', 'C', 'G', 'M', 'O', 'B',
                  'W', 'F', 'K', 'Z', 'V', 'P', 'Ü', 'Ä', 'ß', 'Ö', 'J', 'X', 'Y', 'Q']


# ================================================================
# Reads text from a file and writes the keyed text to another file

def check_german_letters(plain_text, alphabet):
    new_plain_text = ""
    for l in plain_text:
        for letter in alphabet:
            if letter == l.lower():
                new_plain_text = new_plain_text + letter;
    return new_plain_text


# German alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
       'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ä', 'ö', 'ü', 'ß']

# german letters copy and mix
shuffled_abc = alphabet[:]
random.shuffle(shuffled_abc)

# create dict
wb = dict(zip(alphabet, shuffled_abc))

# Open and read sample text
f = open("plainText_sample1.txt")
raw_text = ""
for line in f:
    raw_text += line.rstrip()
f.close()

# clear text
plain_text = check_german_letters(raw_text, alphabet)
print("I have read the text:")
print(plain_text)

# text decode
cipherText = ""
for c in plain_text:
    cipherText = cipherText+wb[c]
print cipherText
#verschlüselten Text in Datei schreiben
f = open("encryptedText.txt", "w")
f.write(cipherText)
f.close()
