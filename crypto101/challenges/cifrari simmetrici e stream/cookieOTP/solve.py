#!/usr/bin/python

import pwn
import Crypto

def get_key(username, cookie):
    text = f"username={username}&admin=False".encode()
    key = bytearray()
    for i in range(len(text)):
        key.append(cookie[i] ^ text[i])
    return key


def encrypt_admin(username, key):
    text = f"username={username}&admin=True".encode()
    payload = bytearray()
    for i in range(len(text)):
        payload.append(text[i] ^ key[i])
    return payload


if __name__ == '__main__':
    c = pwn.connect("cyberchallenge-web-1.tail85307.ts.net", 9004)
    c.recv()
    c.sendline(b"lol")
    response = c.recvline().decode().replace("Here's your cookie, keep it safe! ", "")
    key = get_key("lol", bytes.fromhex(response))
    payload = encrypt_admin("lol", key).hex()
    print(payload)
    c.interactive()
