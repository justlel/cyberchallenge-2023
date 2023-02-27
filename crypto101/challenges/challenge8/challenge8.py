#!/usr/bin/python

from string import ascii_lowercase
from pwn import *


def shifted(char, shift):
    return ascii_lowercase[(ascii_lowercase.index(char) + shift) % 26]

if __name__ == '__main__':
    c = remote('cyberchallenge-web-1.tail85307.ts.net', 9001)
    print(c.recv())
    t = tube()
    n = input()
    c.sendline(n.encode('utf-8'))
    print(c.recv())
    """
    for i in range(1, 26):
        print("\n", i)
        for letter in text.lower():
            if letter in ascii_lowercase:
                print(shifted(letter, i), end="")
            else:
                print(letter, end="")
    """