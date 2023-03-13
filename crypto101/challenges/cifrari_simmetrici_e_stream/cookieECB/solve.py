from pwn import remote, connect
from Crypto.Util.Padding import pad

io = connect("cyberchallenge-web-1.tail85307.ts.net", 9008)


def get_cookie_true():
    io.sendline(7 * b'a' + pad(b'True', 16) + 9 * b'a')
    io.recvuntil("safe! ")
    return io.recvline(False)


def build_payload(cookie):
    iv = cookie[:16]
    first_block = cookie[16:32]
    payload = cookie[:28] + true
    print(len(payload))
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
