import string

from pwn import remote

# il problema è fondamentalmente lo stesso dell'ECB precedente, solo che c'è la possibilità che al testo cifrato
# sia stata aggiunta una 'A' all'inizio. se il primo carattere trovato è una A, basta riavviare il processo


address = "100.77.86.61"
port = 9007

chars = string.ascii_letters + string.digits + string.punctuation

io = remote(address, port)


def solve(npad: int, flag: bytes):
    padding = b"a" * npad
    io.sendline(padding)

    line_guesses = []

    while len(line_guesses) < 2:
        io.recvuntil(b"day :)\n")
        line_guess = io.recvline(False)[:32]  # primi 32 bytes ; 2 blocchi da 16 bytes
        if line_guess not in line_guesses:
            line_guesses.append(line_guess)
        if len(line_guesses) < 2:
            io.sendline(padding)

    list_chars = []

    for c in chars:
        char = c.encode()
        io.sendline(padding + flag + char)

        line_checkings = []

        while len(line_checkings) < 2:
            io.recvuntil(b"day :)\n")
            line_checking = io.recvline(False)[:64]  # primi 32 bytes ; 2 blocchi da 16 bytes
            if line_checking not in line_checkings:
                line_checkings.append(line_checking)
            if len(line_checkings) < 2:
                io.sendline(padding + flag + char)

        for line_checking in line_checkings:
            if line_checking in line_guesses:
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