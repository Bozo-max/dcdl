import pandas as pd
from unidecode import unidecode
from copy import deepcopy



df = pd.read_csv('Lexique383.tsv', sep='\t')
dico = df[['ortho', 'lemme', 'genre', 'nombre','cgram','nblettres']]
dico = dico[dico['nblettres']<=10]
dico = dico['lemme'].drop_duplicates().dropna()
dico = dico.map(unidecode).drop_duplicates()


def main():
    chars = []
    while len(chars)!=10:
        chars = input('Veuillez entrer 10 lettres à la suite : ')
    chars = list(chars.lower())
    print('==========')
    print('Tirage : ', end='')
    print('|'.join(chars).upper())
    print('==========')
    matches = solve(chars)
    print('Resultats : ', end='')
    print(find_best(matches))
    print()
    return


def find_best(t):
    best_len, best = 0, []
    for e in t:
        if len(e)>best_len:
            best_len, best = len(e), [e]
        elif len(e) == best_len:
            best.append(e)
    return (best, best_len)

def solve(chars, dico = dico):
    regex = '^(['+''.join(chars)+']*)$'
    dico = dico.str.extractall(regex)
    dico = dico.squeeze()
    res = dico.where(dico.map(lambda e : checkword(e, deepcopy(chars))))
    return list(res.dropna())

# /!\ chars should be a deep_copy
def checkword(word, chars):
    for letter in word:
        if letter in chars:
            chars.remove(letter)
        else:
            return False
    return True

if __name__ =="__main__":
    main()
