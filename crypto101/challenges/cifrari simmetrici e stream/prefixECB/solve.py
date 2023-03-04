#!/usr/bin/python
import pwn



if __name__ == '__main__':
    c = pwn.connect("cyberchallenge-web-1.tail85307.ts.net", 9003)
    c.recv()
    # sappiamo che la flag inizia con "srdnlen{", quindi possiamo ottenere la cifratura
    # del messaggio "AAAAAAAsrdnlen{?", e bruteforzare l'ultimo carattere, via via fino a trovare la chiave
    flag = "srdnlen{"
    for i in list(range(7))[::-1]:
        base = ("A" * i) + flag
        c.sendline(base.encode())
        a = c.recv().decode()
        resp_enc = a.splitlines()[-2]
        print(resp_enc)
        for i in range(255):
            c.sendline((base + chr(256)).encode())
            enc_test = c.recv().decode().splitlines()[-2]
            print("a\n", enc_test)
            if enc_test in resp_enc:
                flag += chr(i)
                print(flag)