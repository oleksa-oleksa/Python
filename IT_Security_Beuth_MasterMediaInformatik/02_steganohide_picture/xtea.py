import struct
from utils import *

# used http://code.activestate.com/recipes/496737/

XTEA_DELTA = 0x9e3779b9
MASK = 0xffffffff


def xor_block_enc(password, iv, content, rounds):
    enc = encipher(password, content, rounds)
    result = sxor(enc, iv)
    return result


def xor_block_dec(password, iv, content, rounds):
    unxor = sxor(content, iv)
    result = decipher(password, unxor, rounds)
    return result


def crypt(password, content, iv, rounds=32, mode='CFB', enc=True):
    '''
    :param password: hashed password of length 16
    :param content: content to be encrypted
    :param iv: generated seed for the key generator of length 8
    :param rounds: number of rounds (defaults to 32)
    :param mode: XTEA-Mode (CFB, ...)
    :param enc: encode or decode
    :return: the encrypted text
    '''

    assert (len(iv) == 8)
    assert (len(password) == 16)

    # we need: content % 8 == 0!
    roundedContent = int(8 * round(float(len(content))/8))

    result = []
    for i in range(roundedContent // BYTE_OFFSET):
        block = content[i * 8:i * 8 + 8]
        # block = content[i * 8:(i+1) * 8]

        # fill shorter blocks with spaces
        block = block.ljust(8)

        if enc:
            iv = xor_block_enc(password, iv, block, rounds)
            result.append(iv)
        else:
            result.append(xor_block_dec(password, iv, block, rounds))
            iv = block

    return b"".join(result)


def encipher(password, block, num_rounds):
    v0, v1 = struct.unpack("!2L", block)
    k = struct.unpack("!4L", password)

    sum_value = 0

    for r in range(num_rounds):
        v0 = (v0 + (((v1 << 4 ^ v1 >> 5) + v1) ^ (sum_value + k[sum_value & 3]))) & MASK
        sum_value = (sum_value + XTEA_DELTA) & MASK
        v1 = (v1 + (((v0 << 4 ^ v0 >> 5) + v0) ^ (sum_value + k[sum_value >> 11 & 3]))) & MASK
    return struct.pack("!2L", v0, v1)


def decipher(password, block, num_rounds):
    v0, v1 = struct.unpack("!2L", block)
    k = struct.unpack("!4L", password)

    sum_value = (XTEA_DELTA * num_rounds) & MASK

    for r in range(num_rounds):
        v1 = (v1 - (((v0 << 4 ^ v0 >> 5) + v0) ^ (sum_value + k[sum_value >> 11 & 3]))) & MASK
        sum_value = (sum_value - XTEA_DELTA) & MASK
        v0 = (v0 - (((v1 << 4 ^ v1 >> 5) + v1) ^ (sum_value + k[sum_value & 3]))) & MASK
    return struct.pack("!2L", v0, v1)
