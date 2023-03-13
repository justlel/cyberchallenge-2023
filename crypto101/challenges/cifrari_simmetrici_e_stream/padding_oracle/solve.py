#!/usr/bin/python3

from pwn import connect


block_size = 16
io = connect("cyberchallenge-web-1.tail85307.ts.net", 9005)


def get_flag_cipher():
    io.recvuntil(b"Hello! Here's an encrypted flag\n")
    return io.recvline(False).decode()


def split_into_blocks(cipher, size):
    return [cipher[i*size:(i+1)*size] for i in range(size)]


def padding_ok(iv, block):
    io.sendline((iv + block).hex().encode())
    line = io.recvline().decode()
    return "Padding is incorrect." not in line


def single_block_attack(block):
    """Returns the decryption of the given ciphertext block"""

    # zeroing_iv starts out nulled. each iteration of the main loop will add
    # one byte to it, working from right to left, until it is fully populated,
    # at which point it contains the result of DEC(ct_block)
    zeroing_iv = [0] * block_size

    for pad_val in range(1, block_size+1):
        padding_iv = [pad_val ^ b for b in zeroing_iv]

        for candidate in range(256):
            padding_iv[-pad_val] = candidate
            iv = bytes(padding_iv)
            if padding_ok(iv, block):
                if pad_val == 1:
                    # make sure the padding really is of length 1 by changing
                    # the penultimate block and querying the oracle again
                    padding_iv[-2] ^= 1
                    iv = bytes(padding_iv)
                    if not padding_ok(iv, block):
                        continue  # false positive; keep searching
                break
        else:
            raise Exception("no valid padding byte found (is the oracle working correctly?)")

        zeroing_iv[-pad_val] = candidate ^ pad_val
        print(zeroing_iv)

    return zeroing_iv


if __name__ == '__main__':
    flag = bytes.fromhex(get_flag_cipher())
    blocks = [flag[i:i+block_size] for i in range(0, len(flag), block_size)]
    result = b''

    # loop over pairs of consecutive blocks performing CBC decryption on them
    iv = blocks[0]
    for ct in blocks[-1:1:-1]:
        dec = single_block_attack(ct)
        pt = bytes(iv_byte ^ dec_byte for iv_byte, dec_byte in zip(iv, dec))
        result += pt
        iv = ct
    print(result)
