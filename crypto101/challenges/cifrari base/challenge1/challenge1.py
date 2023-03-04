#!/usr/bin/python

from string import ascii_lowercase

freq = {
    'a': 0.082, 'b': 0.015, 'c': 0.028, 'd': 0.043, 'e': 0.127, 'f': 0.022, 'g': 0.020, 
    'h': 0.061, 'i': 0.070, 'j': 0.002, 'k': 0.008, 'l': 0.040, 'm': 0.024, 'n': 0.067, 
    'o': 0.075, 'p': 0.019, 'q': 0.001, 'r': 0.060, 's': 0.063, 't': 0.091, 'u': 0.028, 
    'v': 0.010, 'w': 0.023, 'x': 0.001, 'y': 0.020, 'z': 0.001
}

cipher = "SHGDDGLZAJLWWFOSKLZWKWNWFLZESFFWVEAKKAGFAFLZWSHGDDGKHSUWHJGYJSESFVLZWLZAJVAFLWFVWVLGDSFVGFLZWEGGFLZWUJSXLOSKDSMFUZWVXJGELZWCWFFWVQKHSUWUWFLWJXDGJAVSTMLLZWDMFSJDSFVAFYOSKSTGJLWVSXLWJSFGPQYWFLSFCWPHDGVWVLOGVSQKDSLWJUJAHHDAFYLZWKWJNAUWEGVMDWMHGFOZAUZLZWUGEESFVEGVMDWZSVVWHWFVWV"

def shifted(char, shift):
    return ascii_lowercase[(ascii_lowercase.index(char) + shift) % 26]

def occurrence(letter, text):
    return text.count(letter)/len(text)

def greatest_index(text):
    max_mg = 0
    max_mg_m = ""
    for g in range(26):
        Mg = 0
        for i in range(26):
            Mg += (freq[ascii_lowercase[i]] * occurrence(shifted(ascii_lowercase[i], g), text))/len(text)
        if Mg > max_mg:
            max_mg = Mg
            max_mg_m = ascii_lowercase[g]
    return max_mg_m

if __name__ == '__main__':
    print(greatest_index(cipher.lower()))
    shift = ascii_lowercase.index(greatest_index(cipher.lower()))
    for letter in cipher.lower():
        print(shifted(letter, 26-shift), end="")
