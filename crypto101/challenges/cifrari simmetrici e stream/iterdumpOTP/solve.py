from pwn import remote

#################################################################
#################################################################
##                                                             ##
##   SECTION START                                             ##
##                                                             ##
######                                                      #####

# Input the address and the port
address = "cyberchallenge-web-1.tail85307.ts.net"
port = 9006

# Choose your inputs
x0 = "0000000000000000"
x1 = "0000000000000001"

# Choose your strategy
def strategy(ct: str) -> int:
    key_xor = 0 ^ int(ct[0])
    return key_xor ^ int(ct[-1])

######                                                      #####
##                                                             ##
##   SECTION END                                               ##
##                                                             ##
#################################################################
#################################################################


def talk_to_server():
    io = remote(address, port)

    # Send the plaintexts
    io.recvuntil(b"Give me an x0: ")
    io.sendline(str(x0).encode())
    io.recvuntil(b"Give me an x1: ")
    io.sendline(str(x1).encode())

    # Get the challenge
    io.recvuntil(b"Here you go: ")
    challenge = io.recvline().decode().strip()
    cts = challenge.split(", ")

    # Guess
    io.recvuntil(b"Guess: ")
    guesses = list(map(strategy, cts))
    io.sendline(b", ".join(str(guess).encode() for guess in guesses))

    print(io.recvrepeat(timeout=0.5))


if __name__ == "__main__":
    talk_to_server()
