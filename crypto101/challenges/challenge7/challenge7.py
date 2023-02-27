#!/usr/bin/python

cipher = bytes.fromhex(
    '5e904cfb42a18e054f9b04a057ab81421b9c18b046a59b1f48914de312e58b011dc25bfe15e6d75f54941cb04abc8112569534')


def decipher_last_byte(key):
    key[2] = ord('}') ^ b'\xaa'[0] ^ cipher[-1]


def decipher_right(key, start):
    first = 'srdnlen{'.encode('utf-8')
    for i in range(start, len(key)-1):
        key[i] = first[i] ^ key[i - 1] ^ first[i + 1] ^ cipher[i - 1]


def decipher_left(key, start):
    first = 'srdnlen{'.encode('utf-8')
    for i in range(start, -1, -1):
        key[i] = first[i] ^ first[i + 1] ^ key[i + 1] ^ cipher[i]


def decipher_viscript():



if __name__ == '__main__':
    key = {k: '' for k in range(8)}
    # l'ultimo byte del testo viene criptato usando il terzo carattere della chiave (51 (len) === 3, mod 8).
    # inoltre, sappiamo che la cifratura avviene tramite lo XOR del testo cifrato (flag XOR key), con lo stesso testo
    # cifrato, ma shiftato di un carattere a sinistra. l'ultimo carattere, invece, corrisponde sempre a b'\xaa'.
    # sapendo che l'ultimo carattere del plaintext è '}', si ha che
    # '}' ^ key[2] ^ b'\xaa' = text[-1] -> key[2] = '}' ^ b'\xaa' ^ text[-1]
    decipher_last_byte(key)
    # ora che abbiamo il terzo carattere della chiave, possiamo sfruttare lo shift a sinistra per ottenere gli altri.
    # partendo dalla destra e dal carattere 'd', il 3°, si ha che:
    # 'd' ^ key[2] ^ 'n' (shiftato a sinistra) ^ key[3] = text[2] -> key[3] = 'd' ^ key[2] ^ 'n' ^ text[2]
    # più in generale, spostandosi a destra e considerando la prima parte della flag, first='srdnlen{'
    # key[i] = first[i] ^ key[i-1] ^ first[i+1] ^ text[i-1]
    decipher_right(key, 3)
    # stessa cosa per i primi due caratteri, ma all'incontrario:
    # 'r' ^ key[1] ^ 'd' ^ key[2] = text[1] -> key[1] = 'r' ^ 'd' ^ key[2] ^ text[1]
    # key[i] = first[i] ^ first[i+1] ^ key[i+1] ^ text[i]
    decipher_left(key, 1)
    print(key)
    # manca l'ultimo carattere, ma possiamo iniziare a decifrare

