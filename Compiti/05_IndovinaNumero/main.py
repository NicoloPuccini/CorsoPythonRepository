# INDOVINA NUMERO

import random

MAX_TENTATIVI = 3
points = 10
n_tentativi = 1
n_generated = random.randint(1,101)
won = False

while not won :
    while True:
        tentativo = input("\nProva ad indovinare\nInserisci un numero tra 1 e 100 :")
       
        if tentativo.isnumeric() and int(tentativo) < 101 and int(tentativo) > 0:
            tentativo = int(tentativo)
            break

    if n_tentativi >= MAX_TENTATIVI:
        points-=2
        print(f"Peccato era il : {n_generated}")
        print("GameOver")
        break

    n_tentativi += 1

    if n_generated == tentativo :
        print("Hai vinto")
        won = True
        continue
    

    if n_generated < tentativo :
        print("Sei andato alto")
    if n_generated > tentativo :
        print("Sei andato basso")
    points-=2

print(f"Punteggio : {points}\nTentativi effettuati : {n_tentativi}")