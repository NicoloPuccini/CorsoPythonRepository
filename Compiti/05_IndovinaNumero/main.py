# INDOVINA NUMERO

import random

MAX_TENTATIVI = 3
level = 0
penalita = 2
points = 10
n_tentativi = 1
rand_num_cap = 11
won = False

while True :
    level = input("\nDigita : \n0 - per easy mode\n1 - per medium mode\n2 - per hard mode")
    if level.isdigit() :
        if int(level) == 0 :
            #Setto l'easy mode
            MAX_TENTATIVI = 3
            penalita = 2
            rand_num_cap = 11
            break
        
        if int(level) == 1 :
            MAX_TENTATIVI = 5
            penalita = 3
            rand_num_cap = 21
            break
        
        if int(level) == 2 :
            MAX_TENTATIVI = 7
            penalita = 4
            rand_num_cap = 51
            break
        
n_generated = random.randint(1,rand_num_cap)

lista_tentativi = []

while not won :
    while True:
        if len(lista_tentativi) > 0 :
            print(f"Precedenti tentativi : ")
            for tent in lista_tentativi:
                print(tent)

        tentativo = input(f"\nProva ad indovinare\nInserisci un numero tra 1 e {rand_num_cap-1} :")
       
        if tentativo.isnumeric() and int(tentativo) < rand_num_cap and int(tentativo) > 0:
            tentativo = int(tentativo)
            break

    lista_tentativi.append(tentativo)

    if n_tentativi >= MAX_TENTATIVI:
        points -= penalita
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
    points -= penalita

print(f"Punteggio : {points}\nTentativi effettuati : {n_tentativi}")