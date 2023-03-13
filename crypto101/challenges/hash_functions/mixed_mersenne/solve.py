from pwn import remote

io = remote("cyberchallenge-web-1.tail85307.ts.net", 9015)

def get_numbers():
    return [int(io.recvline(False).decode().replace("|  ", '')) for _ in range(4)]

def get_cracker_feeds(numbers):
    feeds = []
    for number in numbers:
        binary = bin(number)[2:]
        print(binary)
        for i in range(len(binary) // 32):
            feeds.append(binary[i:i+32])
        if len(binary) % 32 > 0:
            feeds.append(binary[-(len(binary) % 32):])
    return feeds


if __name__ == '__main__':
    io.recvuntil(b"ones:\n")
    n = get_numbers()
    print(get_cracker_feeds(n))
