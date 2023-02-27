#!/usr/bin/python
import random

decoded = bytes.fromhex('a789762ed8eaf24212ba038a86652a9e913ac911050d9f6d69fad7e0a63173560d029650575657585154515959')

def find_seed():
    return ''.join([chr(ord(x) ^ 97) for x in "PWVWXQTQYY"]) # "PWVWXQTQYY" è l'ultimo pezzo della stringa decoddata


if __name__ == '__main__':
    # l'ultima parte della stringa XORata è data dallo xor di ogni carattere della stringa contentente il timestamp
    # usato come seed con il numero '97'. il timestamp è sempre lungo 10 caratteri
    seed = find_seed()
    # inizializzando il seed random con quello trovato, possiamo ottenere la chiave usata nello xor
    # nota: la lunghezza della chiave (e del testo) è 35, perché la stringa decoddata ha 45 byte - 10 dati dallo xor del timestamp
    random.seed(seed)
    key = [random.randrange(256) for _ in range(35)]
    # a questo punto si effettua lo xor char a char tra il testo criptato (primi 25 char) e la chiave
    print(''.join([chr(decoded[i] ^ key[i]) for i in range(len(key))]))
    # flag: srdnlen{h3y_l4sc14_3ntr4r3_4sc4n10}
