#!/usr/bin/python
import re
import string
from collections import Counter

freq = {
    'a': 0.082, 'b': 0.015, 'c': 0.028, 'd': 0.043, 'e': 0.127, 'f': 0.022, 'g': 0.020,
    'h': 0.061, 'i': 0.070, 'j': 0.002, 'k': 0.008, 'l': 0.040, 'm': 0.024, 'n': 0.067,
    'o': 0.075, 'p': 0.019, 'q': 0.001, 'r': 0.060, 's': 0.063, 't': 0.091, 'u': 0.028,
    'v': 0.010, 'w': 0.023, 'x': 0.001, 'y': 0.020, 'z': 0.001
}

text="""XSIQNFKAHPPCTINAWLPSTOCCSOICSHYENFHWPOKESQEFOCIEEHVWGHVNMYWOERZNMLRZNBXUERIOARGRSXYZTOKEHMCHUSZUHPBSYSRNSCSTNFSOVPEWGKRSMYJCEQVIRDEFQWEIEFRHVZZTALWGHDVRWPHSQPPTLPWOICPAVOGCQSFFGSEFYSJFIWMLGVVCECXOJOJAAZVYBTXRILXWZDFRXLRQRWESECHWAWRNLTWHBFPIXHEGNBFRKLRWPQFHICIBGOEDWJWHRARTMNACEYFFPPKWFZRTMZRSAQFMTLWGVBXTLPGWIWCAROTSAOCLEHXVRVZSXZVMBTKHIOVOSHZNKZJHUSTAVEEWFIEKRZABOIKTLPGOEHRIXDIZSDIOZTHSFOEEBNIZYSETKWMACGVIRESHUSVTLYSZBUZCEWEBQZZNKFMGGWTSMEYOGWFNSQPOGSDEHTIJNZJAVOMBVOZNXSIQNFKAXSIFRWJTLPQCQSINMKMBTCWCICXOVBEOVXWOARKHIUYFVRZCEWAWFRFMXSEHPCETETRGRZVMIYXGBTKHICSANBTARZRWPOCTVLHWGWFNXSIPLNRNXTRSBBVTLPFCYCXNIDIXHFZSTCYRRBTEEYHHUSKHSFKVGCWTLPKZBGJAXZVGBTKHINEHNZRNGZYFGQLLXFVSOIKAFZZSNZCTLPPCPOCJYCMRVQRLIWEPBFRTMZRCSHYEWLVRVBZARNYGGCDSQLHSOMJAVOMBVOEMYYMQVDRLPLACASEOXLFZRDIOZTWWBBFFXSIQBRVIWELOGWKGEGIRNIXHXPVGNBUSSYWHUSJAQPMBUSIIXLRQRFZGLEWOFKVLPTXOYGFDINPOESUTLLXFNDVCSFPROSIEGZQDRBJEHELFBIXHQLVFVOXESYPMVTKHIHSANBNHSHEGEOGEHLKFRSUTSXEFEMYEVCEDVGKAROIJRBZFWSIRVRKHINSRRRVCPLVSQHYAXELSEOGIWEWHVZCHEOXCRWKHICTOLOCAVRITVBVTSELSFSEAXPSFUOMELTWTBCKCYESTSVZSGSSWPSZFWSIRVREOXLKFRSKOQLVFLVZMLPLOQHFGMGIVRFRDSHVMGVRTWFMHRRYEVDSQVOCSXLXIFGFTLLXGUSTOYWHANFIYWZQSBBVEPDIOARYEWEMZYVRDXZIWGVVRTLCOYOIGIQMBRHFTLPWSAOKESCLOISYIWQSCGQLTSQJVVGTHSTGSNGNEPWXVRGVPYYMGUAVNXDASESEOXLJTRQKEHMCKUSKHICSFACKTLPACZOEIRBYSFHZORHEGOSKRSELSQHYEGZHSNZJOGLYGRRVLILRCECWAVMSFROKOFPVSZSDBICIRNGFNIZJHUSWIVDXZNKDAOPVGGCJEXFTHUSTOROMHVCEOJCIQVDIOGTXMJVVNHPEZVBXWMELTBFVIKYIFFOJWIWPOFHYEGCMARCWMMDJSNGRNGP"""

"""
XSIQNFKA
HPPCTINA
WLPSTOCC
SOICSHYE
NFHWPOKE
"""

"""
def occurrence(letter, text):
    return text.count(letter)/len(text)

def ic(text):
    return sum([(occurrence(letter, text)*(occurrence(letter, text)-1))/(len(text)*(len(text)-1)) for letter in ascii_lowercase])


def try_ic(text):
    max_ic = -100
    ic_m = 0
    for m in range(1, 700):
        column = {}
        splitted = split_text(text, m)
        for i in range(m):
            column[i] = ''.join([sp[i] if len(sp) == m else "" for sp in splitted])
            print(i, m, column)
        ic_local = sum([ic(c) for c in column.values()])/len(column)
        if ic_local > max_ic:
            max_ic = ic_local
            ic_m = m
    print(max_ic)
    return ic_m
"""

def split_text(text, chunk_l):
    return list((text[0 + i:chunk_l + i] for i in range(0, len(text), chunk_l)))


def find_repetitions_distance(text):
    for i in range(3, len(text)):
        splitted = split_text(text, i)
        doubles = [k for k, v in Counter(splitted).items() if v > 1]
        if len(doubles) > 0:
            print(f"len: {i}, doubles: {doubles}")
            doubles_distance = []
            for double in doubles:
                matches = [m for m in re.finditer(double, text)]
                doubles_distance.append(matches[1].start() - (matches[0].end()-1)-1)
            print(doubles_distance)


def r_rotate_text(text, rotation):
    text_rotated: str = text
    for i in range(rotation):
        text_rotated = text_rotated[-1] + text_rotated[:-1]
    return text_rotated

def occurrency(text, letter):
    return sum([1 for i in range(1, len(text)) if text[i] == letter])/len(text)

def split_columns(text, column_width):
    splitted = split_text(text, column_width)
    columns = {}
    for i in range(column_width):
        columns[i] = ''.join([sp[i] if len(sp) == column_width else "" for sp in splitted])
    return columns

def occurrency_per_letter_column(column):
    letters = {}
    for char in column:
        if char in letters:
            continue
        letters[char] = round(occurrency(column, char), 3)
    return letters

if __name__ == '__main__':
    # find_repetitions_distance(text)
    key_len = 8  # in questo caso il doppione più lungo è di 8 caratteri (lunghezza minima), mentre le distanze tra i doppioni più piccoli hanno come fattori divisori di 8
    columns = split_columns(text, key_len)
    print("occurrency delle colonne: ")
    occs = []
    for col in columns.values():
        occ = occurrency_per_letter_column(col)
        occs.append({k: occ[k] for k in sorted(occ, key=occ.get, reverse=True)})
    [print(occ) for occ in occs]
    print("occurrency inglese: ")
    print({k: freq[k] for k in sorted(freq, key=freq.get, reverse=True)})
    # da qui, si va a mano :)
    """
    possibilità:
    1) X->E, I->E, S->E, L->E
    2) X->T, I->T, S->T, L->T
    3) X->A, I->A, S->A, L->A
    """