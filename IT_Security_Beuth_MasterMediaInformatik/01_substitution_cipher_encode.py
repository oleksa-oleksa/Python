import random

# German alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ä', 'ö', 'ü', 'ß']


# ================================================================
# Reads text from a file and writes the keyed text to another file

def check_german_letters(plain_text, alphabet):
    new_plain_text = ""
    for l in plain_text:
        for letter in alphabet:
            if letter == l.lower():
                new_plain_text = new_plain_text + letter;
    return new_plain_text


# german letters copy and mix
shuffled_abc = alphabet[:]
random.shuffle(shuffled_abc)

# create dict
dict_german = dict(zip(alphabet, shuffled_abc))

# Open and read sample text
f = open("data/plaintext_english.txt")
raw_text = ""
for line in f:
    raw_text += line.rstrip()
f.close()

# clear text
plain_text = check_german_letters(raw_text, alphabet)
print("Plain text: ========> ")
print(plain_text, "\n")

# text encode
ciphertext = ""
for c in plain_text:
    ciphertext = ciphertext + dict_german[c]
print("Secret text: ========> :")
print(ciphertext, "\n")

# write file with the text
f = open("encryptedtext.txt", "w")
f.write(ciphertext)
f.close()
