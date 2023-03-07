from pwn import remote, connect

io = connect("cyberchallenge-web-1.tail85307.ts.net", 9008)


def get_cookie_true():
    io.sendline(b"Trueaaaaaaaa")
    io.recvuntil("safe! ")
    return io.recvline(False)


def build_payload(cookie):
    true = cookie[9:13]
    payload = cookie[:28] + true
    print(len(payload))
    return payload.hex()


"""
username=True&ad|min=False_______

username=Trueaaa|aaaaa&admin=True
"""


if __name__ == '__main__':
    cookie = bytes.fromhex(get_cookie_true().decode())
    print(cookie)
    p = build_payload(cookie)
    print(p)
    io.interactive()
