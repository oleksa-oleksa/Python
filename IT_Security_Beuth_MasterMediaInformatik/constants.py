# INPUT_FILENAME = "data/plaintext_german.txt"
# OUPUT_FILENAME = "data/cipertext_german.txt"
INPUT_FILENAME = "data/plaintext_english.txt"
OUPUT_FILENAME = "data/cipertext_english.txt"

FREQUENT_LETTERS_DE = ['e', 'n', 'i', 'r', 's', 't', 'a', 'd', 'h', 'u', 'l', 'c', 'g', 'm', 'o', 'b',
                    'w', 'f', 'k', 'z', 'v', 'p', 'ü', 'ä', 'ß', 'ö', 'j', 'x', 'y', 'q']

FREQUENT_LETTERS = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u', 'm', 'w',
                        'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z']

# German alphabet
ALPHABET_DE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ä', 'ö', 'ü', 'ß']

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

LETTER_PERCENTAGE_DE = {'e': 16.93, 'n': 10.53, 'i': 8.02, 'r': 6.89, 's': 6.42, 't': 5.79, 'a': 5.58, 'd': 4.98,
                     'h': 4.98, 'u': 3.83, 'l': 3.60, 'c': 3.16, 'g': 3.02, 'm': 2.55, 'o': 2.24, 'b': 1.96,
                     'w': 1.78, 'f': 1.49, 'k': 1.32, 'z': 1.21, 'v': 0.84, 'p': 0.67, 'ü': 0.65, 'ä': 0.54,
                     'ß': 0.37, 'ö': 0.30, 'j': 0.24, 'x': 0.05, 'y': 0.05, 'q': 0.02}


LETTER_PERCENTAGE = {'e': 12.702, 't': 9.056, 'a': 8.167, 'o': 7.507, 'i': 6.966,
                     'n': 6.749, 's': 6.327, 'h': 6.094, 'r': 5.987, 'd': 4.253,
                     'l': 4.025, 'c': 2.782, 'u': 2.758, 'm': 2.406, 'w': 2.360,
                     'f': 2.228, 'g': 2.015, 'y': 1.974, 'p': 1.929, 'b': 1.492,
                     'v': 0.978, 'k': 0.772, 'j': 0.153, 'x': 0.150, 'q': 0.095, 'z': 0.074}


# https://www.sttmedia.com/syllablefrequency-german
TWO_LETTER_WORDS_DE = ['in', 'zu', 'er', 'es', 'so', 'an', 'im', 'um', 'da', 'du', 'wo', 'ja']

THREE_LETTER_WORDS_DE = ['die', 'der', 'und', 'den', 'das', 'von', 'sie',
                      'ist', 'des', 'sich', 'mit', 'dem', 'dass', 'ein', 'ich',
                      'auf',  'als', 'wie', 'für', 'man', 'aus', 'nur', 'war', 'bei',
                      'hat', 'wir', 'was', 'zur', 'mir', 'ihm', 'ihr', 'nun', 'bis']


ONE_LETTER_WORDS = ['a', 'i']

TWO_LETTER_WORDS = ['he', 'at', 'it', 'if', 'in', 'is',
                    'on', 'to', 'do', 'go', 'of', 'an',
                    'so', 'of', 'up', 'as', 'my', 'me',
                    'be', 'as', 'or', 'we', 'by', 'no', 'am', 'us']

THREE_LETTER_WORDS = ['the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'any',
                      'can', 'had', 'her', 'was', 'one', 'our', 'out', 'day', 'get',
                      'has', 'him', 'his', 'how', 'man', 'new', 'now', 'old', 'see', 'two',
                      'way', 'who', 'boy', 'did', 'its', 'let', 'put', 'say', 'too', 'use']
