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
