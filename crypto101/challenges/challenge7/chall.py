import os
from secret import FLAG

assert FLAG.startswith(b"srdnlen{")
assert FLAG.endswith(b"}")
assert len(FLAG) == 51


def xor(key, data):
    return bytes(x ^ y for x, y in zip(key * len(data), data))


def viscrypt(data):
    return xor(data, data[1:] + b"\xaa")


def round(key, rawdata):
    return viscrypt(xor(key, rawdata))


key = os.urandom(8)

pt = FLAG
ct = round(key, pt)

with open("ciphertext.txt", "w") as f:
    f.write(ct.hex())
