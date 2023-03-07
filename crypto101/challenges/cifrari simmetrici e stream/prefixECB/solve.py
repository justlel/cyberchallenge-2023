import string

from pwn import remote

address = "100.77.86.61"
port = 9003

chars = string.ascii_letters + string.digits + string.punctuation

io = remote(address, port)


def solve(npad: int, flag: bytes):
    padding = b"a" * npad
    io.sendline(padding)

    io.recvuntil(b"day :)\n")

    line_guess = io.recvline(False)[:2 * 32]  # primi 32 bytes ; 2 blocchi da 16 bytes

    list_chars = []

    for c in chars:
        char = c.encode()
        io.sendline(padding + flag + char)
        io.recvuntil(b"day :)\n")
        line_checking = io.recvline(False)[:64]  # primi 32 bytes ; 2 blocchi da 16 bytes

        if line_checking == line_guess:
            list_chars += [char]
            return char


def talk_to_server():
    flag = b""
    for i in range(31, -1, -1):
        char = solve(i, flag)
        flag += char
        print(flag)

        if char == b"}":
            break

    io.interactive()
    io.close()


if __name__ == "__main__":
    talk_to_server()