import random

def ia(liste, dico, signe):
    while True:
        move = random.choice(liste)
        print(move)
        if liste.index(move) not in dico:
            signe(liste.index(move))
            break
        else:
            continue

