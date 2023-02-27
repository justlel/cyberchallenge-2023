#!/bin/env python3

from collections import defaultdict
import sys

# Se vuoi leggere/scrivere da file decommenta qua
fin = open("input.txt", "r")  # File di input fornito dalla piattaforma
fout = open("output.txt", "w")  # File di output fornito dalla piattaforma

# Se vuoi leggere/scrivere da linea di comando decommenta qua
#fin = sys.stdin  # File di input fornito dalla piattaforma
#fout = sys.stdout  # File di output fornito dalla piattaforma


def solve(N, S, M, required_skills_list, players):
    skills = {}
    for req_skill in required_skills_list:
        if req_skill in skills:
            skills[req_skill]['quantity'] += 1
        else:
            skills[req_skill] = {}
            skills[req_skill]['skills'] = []
            skills[req_skill]['quantity'] = 1
            skills[req_skill]['filled'] = False
    for id, player in players.items():
        skill = list(player.keys())[0]
        if skill in skills and not skills[skill]['filled']:
            skills[skill]['skills'].append(player[skill])
            if len(skills[skill]['skills']) > skills[skill]['quantity']:
                skills[skill]['skills'].sort(reverse=True)
                skills[skill]['skills'].pop(-1)
                skills[skill]['filled'] = True
        elif skill in skills and skills[skill]['filled']:
            for i, selected in enumerate(skills[skill]['skills']):
                if selected < player[skill]:
                    skills[skill]['skills'].insert(i, player[skill])
                    skills[skill]['skills'].pop(-1)
                    break
    return sum(sum(skill['skills']) for skill in skills.values())


T = int(fin.readline().strip())

for _ in range(T):
    N, M, S = list(map(int, fin.readline().strip().split()))
    required_skills_list = list(map(str, fin.readline().strip().split()))
    players = {}
    for i in range(N):
        id = fin.readline()
        players[id] = defaultdict(int)
        for j in range(S):
            skill, level = fin.readline().strip().split()
            level = int(level)
            players[id][skill] = level

    print(solve(N, S, M, required_skills_list, players), file=fout)
