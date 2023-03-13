from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

KEY = get_random_bytes(16)
FLAG = os.environ['FLAG']


def aes_ecb_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(plaintext)


def encryption_oracle(plaintext):
    plaintext = pad(plaintext + FLAG.encode(), 16)
    return aes_ecb_encrypt(plaintext, KEY).hex()
