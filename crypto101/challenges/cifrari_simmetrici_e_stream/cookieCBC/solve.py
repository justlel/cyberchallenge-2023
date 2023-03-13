from pwn import remote, connect
from Crypto.Util.Padding import pad

io = connect("cyberchallenge-web-1.tail85307.ts.net", 9010)


sent = 7 * b'a' + pad(b'True', 16) + 9 * b'a'


def get_cookie_true():
    io.sendline(sent)
    io.recvuntil(b"safe! ")
    return io.recvline(False)


def xor_blocks(block1, block2):
    return bytearray([block1[i] ^ block2[i] for i in range(len(block2))])


def build_payload(cookie):
    iv = cookie[:16]
    first_block = cookie[16:32]
    true_block = cookie[32:48]
    admin_block = cookie[48:64]
    false_block = cookie[64:]
    true_block_deciphered = xor_blocks(true_block, xor_blocks(iv, first_block))
    true_block_payloaded = xor_blocks(sent, xor_blocks(b"aaaaaaaaa&admin=", admin_block))
    payload = iv + first_block + true_block + true_block_payloaded + false_block
    return payload.hex()


"""
username=aaaaaaa|True____________|aaaaaaaaa&admin=|False__...
"""


if __name__ == '__main__':
    cookie = bytes.fromhex(get_cookie_true().decode())
    print(cookie)
    p = build_payload(cookie)
    print(p)
    io.interactive()
