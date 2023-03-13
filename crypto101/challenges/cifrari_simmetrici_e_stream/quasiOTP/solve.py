from pwn import remote
from utils import strxor

#################################################################
#################################################################
##                                                             ##
##   SECTION START                                             ##
##                                                             ##
######                                                      #####

# Input the address and the port
address = "cyberchallenge-web-1.tail85307.ts.net"
port = 9002

# Choose your inputs
x0 = "0000000000000000"
x1 = "0000000000000001"

# Choose your strategy
# :P
def strategy(ct: str) -> int:
    key = []
    for i, bit in enumerate(ct[:-1]):
        key.append(strxor(x0[i], bit))
    last_bit = key[0]
    for keyb in key[1:]:
        last_bit = strxor(last_bit, keyb)
    return strxor(ct[-1], last_bit)[0]

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
