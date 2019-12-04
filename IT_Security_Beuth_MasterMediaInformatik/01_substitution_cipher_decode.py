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

# German alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ä', 'ö', 'ü', 'ß']

#countLetterEn = "etaoinshrdlcumwfgypbvkjxqz"

# ================================================================
# Reads text from a file and writes the keyed text to another file

import operator
import string
from collections import defaultdict
import enchant


def compute_char_frequency(text, c):
    return text.count(c)


def sort_and_reverse(detected_words, replace_word, decrypted_text):
    new_word = sorted(detected_words.items(), key=operator.itemgetter(1))
    print("New", new_word)
    new_word.reverse()
    return replace_words(new_word[0][0], replace_word, decrypted_text)


def replace_words(encrypted_word, new_word, decrypted_text):
    i = 0
    for old_char in encrypted_word:
        if old_char != new_word[i]:
            decrypted_text = decrypted_text.replace(new_word[i], ".")
            tmp = old_char
            decrypted_text = decrypted_text.replace(old_char, new_word[i])
            decrypted_text = decrypted_text.replace(".", tmp)
        i += 1
    return decrypted_text


def count_syllable(decrypted_text):
    return count_words_of_lenght_n(decrypted_text, 1)


def count_digrams(decrypted_text):
    return count_words_of_lenght_n(decrypted_text, 2)


def count_trigrams(decrypted_text):
    return count_words_of_lenght_n(decrypted_text, 3)


def count_quadrigrams(decrypted_text):
    return count_words_of_lenght_n(decrypted_text, 4)



def count_words_of_lenght_n(decrypted_text, n):
    count = defaultdict(int)
    for c in decrypted_text.split():
        if len(c) == n:
            count[c] += 1
    return count


def get_words_with_unknown_letter(found_chars):
    splitted_decrypted_text = string.split(decrypted_text, " ");
    unknown_letters = [];
    for token in splitted_decrypted_text:
        for char in token:
            if char not in foundChars:
                unknown_letters.append(token)
    unknown_letters = sorted(list(set(unknown_letters)))
    return unknown_letters


f = open("encryptedtext.txt")
ciphertext = ""
for line in f:
    ciphertext += line.rstrip()
f.close()
print("Ciphertext:")
print(ciphertext)


# DECODING

i = 0
countLetter = alphabet[:]  # copy
for letter in alphabet:
    countLetter[i] = compute_char_frequency(ciphertext, letter)
    i += 1

#Beziehung zwischen Buchstabe und Häufigkeit setzen
chars_frequency = dict(zip(alphabet, countLetter))

chars_frequency_sorted = sorted(chars_frequency.items(), key=operator.itemgetter(1))
chars_frequency_sorted.reverse()
print("Char frequency in encoded text:")
print(chars_frequency_sorted)

most_frequency_letter = [" "]

for item in letters_german:
    most_frequency_letter.append(item)

extracted_chars = []
for item in chars_frequency_sorted:
    extracted_chars.append(item[0][0])


code_dict = dict(zip(extracted_chars, most_frequency_letter))


decrypted_text = ""
for c in ciphertext:
    decrypted_text = decrypted_text + code_dict[c]

splitted_decrypted_text = decrypted_text.split(" ")
print("First match  dict -> encoded text:")
print(decrypted_text)

syllables = count_syllable(decrypted_text)
new_word = sorted(syllables.items(), key=operator.itemgetter(1))
if len(new_word) == 2:
    one_letter_words = "ia"

    i = 0
    for old in new_word:
        old = old[0][0]
        if old != one_letter_words[i]:
            decrypted_text = decrypted_text.replace(one_letter_words[i], ".")
            extracted_chars = old
            decrypted_text = decrypted_text.replace(old, one_letter_words[i])
            decrypted_text = decrypted_text.replace(".", extracted_chars)
        i += 1
print("Text after syllables detection")
print(decrypted_text)

detected_words = count_digrams(decrypted_text)
decrypted_text = sort_and_reverse(detected_words, "en", decrypted_text)
print("Text after digrams detection")
print(decrypted_text)

detected_words = count_trigrams(decrypted_text)
decrypted_text = sort_and_reverse(detected_words, "ich", decrypted_text)
print("Text after trigrams detection")
print(decrypted_text)

detected_words = count_quadrigrams(decrypted_text)
decrypted_text = sort_and_reverse(detected_words, "mich", decrypted_text)
print("Text after quadrigramss detection")
print(decrypted_text)

splitted_decrypted_text = string.split(decryptedText, " ")
found_chars = [' ', 'e', 't', 'h', 'w', 'a', 'o', 'f', 'i']

"""
print("Dictonary check:")
stopper = 0
for x in range(0, len(splitted_decrypted_text)):
    token = splittedDecryptedText[x]
    len_token = len(token)
    if len_token >= 2 and len_token <= 16:
        fobj = open("dict/" + str(lenToken) + "top.txt")
        foundWords = []
        maxCharsForAccord = (len(token)+1)/3*2
        for line in fobj:
            dictWord = line.rstrip()
            if set(dictWord) == set(token):
                foundWords = []
                break
            if dictWord != token:
                i = 0
                count = 0
                for char in token:
                    if dictWord[i] == char:
                        count += 1
                    i += 1
                if count >= maxCharsForAccord:
                    foundWords.append(dictWord)
        tmp = []
        for word in foundWords:
            for letter in word:
                matching = letter not in foundChars
                if matching:
                    tmp.append(word)
                    break
        foundWords = tmp
        if len(foundWords) == 1:
            decryptedText = replaceWords(token, foundWords[0], decryptedText)
            for letter in foundWords[0]:
                foundChars.append(letter)
            foundChars = list(set(foundChars))
        fobj.close()
    splittedDecryptedText = string.split(decryptedText, " ")
    stopper += 1
    if stopper == 50:
        break

print decryptedText


print "\nAusgabe nach PyEnchant-Check: "
wordsWithUnknownLetter = getWordsWithUnknownLetter(decryptedText, foundChars)
enchantUS = enchant.Dict("en_US")

#Alle Wörter rausschmeissen von den alle befindlichen Buchstaben bekannt sind
removeWords = []
for token in wordsWithUnknownLetter:
    enchantResult = enchantUS.suggest(token)
    for result in enchantResult:
        if str.lower(result) == token:
            for letter in token:
                if letter not in foundChars:
                    foundChars.append(letter)
            removeWords.append(token)
            continue
for word in removeWords:
    if word in wordsWithUnknownLetter:
        wordsWithUnknownLetter.remove(word)

wordsWithUnknownLetter = getWordsWithUnknownLetter(decryptedText, foundChars)
finished = False

#mit PyEnchant die letzten Wörter rausfinden und mit dem Text abgleichen
if len(wordsWithUnknownLetter) > 0:
    while finished == False:
        enchantResult = enchantUS.suggest(wordsWithUnknownLetter[0])
        before = wordsWithUnknownLetter[0];
        tmpRemove = []
        for result in enchantResult:
            if len(wordsWithUnknownLetter) > 0:
                if len(result) == len(wordsWithUnknownLetter[0]):
                    for letter in str.lower(result):
                        if letter not in foundChars:
                            foundChars.append(letter)
                            index = decryptedText.find(letter)
                            tmpDecryptedText = replaceWords(wordsWithUnknownLetter[0], result, decryptedText)
                            decryptedText[index]
                            if tmpDecryptedText[index] not in foundChars:
                                foundChars.append(decryptedText[index])
                                decryptedText = tmpDecryptedText
                                wordsWithUnknownLetter = getWordsWithUnknownLetter(decryptedText, foundChars)
                            if len(wordsWithUnknownLetter) == 0:
                                finished = True
        if len(wordsWithUnknownLetter) > 0:
            if before == wordsWithUnknownLetter[0]:
                tmpRemove.append(wordsWithUnknownLetter[0])
                wordsWithUnknownLetter.remove(wordsWithUnknownLetter[0])
                if len(wordsWithUnknownLetter) == 0:
                    finished = True

print decryptedText

fobj = open("plainText_decoded_01.txt")
plainText = ""
for line in fobj:
    plainText += line.rstrip()
fobj.close()

print "\nORIGINAL-TEXT:"
print plainText
"""