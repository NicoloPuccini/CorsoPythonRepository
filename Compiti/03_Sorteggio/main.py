import array
import random

n_squadre = 2
partecipanti= ["Tizio","Caio","Giulio","Cesare","Bruto","Cassio","Tullio","Cicerone","Giovanni"]
n_partecipanti= len(partecipanti)
squadra_1=[]
squadra_2=[]
curr_sqad=True
while partecipanti :

    sorted = random.choice(partecipanti)
    partecipanti.remove(sorted)
    if(curr_sqad):
        squadra_1.append(sorted)
    else:
        squadra_2.append(sorted)
    curr_sqad = not curr_sqad

#stampa le squadre
print("\nsquadra_1 :")
while squadra_1 :
    print(squadra_1.pop())
print("\nsquadra_2 :")
while squadra_2 :
    print(squadra_2.pop())

print("-"*50)

n_squadre = int(input("inserisci il numero di squadre"))
partecipanti= ["Tizio","Caio","Giulio","Cesare","Bruto","Cassio","Tullio","Cicerone","Giovanni"]
n_partecipanti= len(partecipanti)
squadre = [[] for _ in range(n_squadre)]
curr_sqad = 0
while partecipanti :

    sorted = random.choice(partecipanti)
    partecipanti.remove(sorted)
    squadre[curr_sqad].append(sorted)
    curr_sqad += 1
    if curr_sqad == n_squadre:
        curr_sqad = 0

#stampa le squadre
for i in range(n_squadre):
    print(squadre[i])

    
