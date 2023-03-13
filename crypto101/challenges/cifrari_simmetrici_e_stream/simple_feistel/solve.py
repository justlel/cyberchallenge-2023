#!/usr/bin/python

flag = "001100111010001001100110110111010010000101001010000011110101100101110011010110001110000100011101000111010011110000110111000000101001111000101111000111010011110110011010001011010000110011001000000000110001000010100011000000101000011011100001000111000010100010010100011001000110010111011011"
K = 2
key = "01011010"

S1 = {
    '0': {
        '000': '101', '001': '010', '010': '001', '011': '110',
        '100': '011', '101': '100', '110': '111', '111': '000'
    },
    '1': {
        '000': '001', '001': '100', '010': '110', '011': '010',
        '100': '000', '101': '111', '110': '101', '111': '011'
    }
}

S2 = {
    '0': {
        '000': '100', '001': '000', '010': '110', '011': '101',
        '100': '111', '101': '001', '110': '011', '111': '010'
    },
    '1': {
        '000': '101', '001': '011', '010': '000', '011': '111',
        '100': '110', '101': '010', '110': '001', '111': '100'
    }
}


def divide_blocks(text):
    return [text[i*12:(i+1)*12] for i in range(len(text) // 12)]

def binary_strxor(text1, text2):
    return "".join(str(int(text1[i]) ^ int(text2[i])) for i in range(len(text1)))

def get_8_bit_key(key, j, k, K):
    start = (j*K + k) % len(key)
    return key[start:] + key[:start]

def apply_sbox(box, text):
    return box[text[0]][text[1:]]

def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))


def decipher(blocks):
    deciphered = ""
    for j, block in enumerate(blocks):
        print(block)
        # splitto il blocco da 12 in due da 6
        R, L = block[:len(block)//2], block[len(block)//2:]
        for k in range(K-1, -1, -1):
            # incremento la lunghezza di R a 8 bit
            R_extended = R[:2] + R[3] + R[2] + R[3] + R[2] + R[4:]
            # calcolo gli 8 bit della chiave
            key_8_bit = get_8_bit_key(key, j, k, K)
            # xor con la chiave e divisione in due parti
            A = binary_strxor(R_extended, key_8_bit)
            A1, A2 = A[:4], A[4:]
            # applicazione delle substitution boxes
            C = apply_sbox(S1, A1) + apply_sbox(S2, A2)
            # xor tra C e L
            D = binary_strxor(C, L)
            # L->R, R->D
            L, R = R, D
        deciphered += R + L
    print(deciphered)
    print(decode_binary_string(deciphered))


if __name__ == '__main__':
    blocks = divide_blocks(flag)
    decipher(blocks)
