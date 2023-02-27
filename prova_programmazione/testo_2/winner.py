#!/bin/env python3

import sys
from collections import OrderedDict

# Se vuoi leggere/scrivere da file decommenta qua
fin = open("input/winner-input-1.txt", "r")  # File di input fornito dalla piattaforma
fout = open("output.txt", "w")  # File di output fornito dalla piattaforma

# Se vuoi leggere/scrivere da linea di comando decommenta qua
#fin = sys.stdin  # File di input fornito dalla piattaforma
#fout = sys.stdout  # File di output fornito dalla piattaforma


def calcola_classifica(M, N, S, tasks, submissions):
    # creo una tabella con le informazioni dei giocatori
    players = {player_id: {'points': 0, 'time': 0, 'solved': []} for player_id in range(1,M+1)}
    for submission in submissions:
        player, task, submitted, timestamp = submission
        if submitted == tasks[task-1][0] and task not in players[player]['solved']:
            players[player]['points'] += tasks[task-1][1]
            players[player]['time'] += timestamp
            players[player]['solved'].append(task)
    sorted_players = {}
    # ordino la tabella per punti e tempo
    for sorted_p in sorted(players, key=lambda player: [players[player]['points'], players[player]['time']], reverse=True):
        sorted_players[sorted_p] = players[sorted_p]
    posizioni = dict(enumerate(OrderedDict(sorted_players).items()))
    classifica = [{player[0]: player[1]} for player in sorted_players.items()]
    # qui cerco di controllare se due giocatori hanno lo stesso punteggio
    for posizione in range(len(classifica)):
        if posizione < len(classifica) - 1:
            supposto_primo = list(classifica[posizione].values())[0]
            supposto_secondo = list(classifica[posizione + 1].values())[0]
            print(supposto_primo)
        if supposto_primo['points'] == supposto_secondo['points']:
            if supposto_primo['time'] > supposto_secondo['time']:
                classifica.pop(posizione + 1)
                classifica.insert(posizione, supposto_secondo)
                continue
    print(classifica)
    return players


M, N, S = map(int, fin.readline().strip().split())
tasks = []
submissions = []

for _ in range(N):
    tid, flag, points = fin.readline().strip().split()
    tasks.append((flag, int(points)))

for _ in range(S):
    player, task, submitted, timestamp = fin.readline().strip().split()
    submissions.append((int(player), int(task), submitted, int(timestamp)))

print(calcola_classifica(M, N, S, tasks, submissions), file=fout)
