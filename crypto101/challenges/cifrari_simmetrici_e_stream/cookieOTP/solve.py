#!/usr/bin/python

import pwn
from Crypto.Util.strxor import strxor

def get_key(username, cookie):
    text = f"username={username}&admin=False".encode()
    return strxor(text, cookie)


def encrypt_admin(username, key):
    text = f"username={username}&admin=True".encode()
    return strxor(text, key)


if __name__ == '__main__':
    c = pwn.connect("cyberchallenge-web-1.tail85307.ts.net", 9004)
    c.recv()
    c.sendline(b"lol")
    response = c.recvline().decode().replace("Here's your cookie, keep it safe! ", "")
    key = get_key("lol", bytes.fromhex(response))
    print(key)
    print(encrypt_admin("loll", key).hex())
    c.interactive()
