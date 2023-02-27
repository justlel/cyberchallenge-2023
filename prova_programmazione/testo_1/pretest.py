#!/bin/env python3

import sys

# Se vuoi leggere/scrivere da file decommenta qua
fin = open("input.txt", "r")  # File di input fornito dalla piattaforma
fout = open("output.txt", "w")  # File di output fornito dalla piattaforma

# Se vuoi leggere/scrivere da linea di comando decommenta qua
# fin = sys.stdin  # File di input fornito dalla piattaforma
# fout = sys.stdout  # File di output fornito dalla piattaforma


def calcola_punteggio(correct, candidate):
    count = 0
    for i in range(len(correct)):
        if correct[i] == candidate[i]:
            count += 1
    return count


Q, N = map(int, fin.readline().strip().split(" "))
correct = fin.readline().strip()

for i in range(N):
    candidate = fin.readline().strip()
    print(calcola_punteggio(correct, candidate), file=fout)
