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



# V(3.0)
partecipanti= ["Tizio","Caio","Giulio","Cesare","Bruto","Cassio","Tullio","Cicerone","Giovanni"]
n_squadre = int(input("inserisci il numero di squadre"))
n_partecipanti= len(partecipanti)
squadre = [[] for _ in range(n_squadre)] #array di liste
yn = True
while yn == True :
    curr_sqad = 0


    while True :
        input_partecipanti = input("Inserisci un nuovo partecipante alle selezioni,"
        " digita exit per iniziare il sorteggio ")
        if input_partecipanti == "exit":
            break
        partecipanti.append(input_partecipanti)

    while partecipanti :
        sorted = random.choice(partecipanti)
        partecipanti.remove(sorted)
        squadre[curr_sqad].append(sorted)
        curr_sqad += 1
        if curr_sqad == n_squadre:
            curr_sqad = 0

    #stampa le squadre
    for i in range(n_squadre):
        for j in range(len(squadre[i])):
            if j==0 :
                print("\nCapitano : ", end="")   # Print che non va accapo , resta inline
            print ((squadre[i])[j])

    #Stampa le squadre su file 

    with open("Squad_saving.txt","w") as file:
        pass
        for i in range(n_squadre):
            for j in range(len(squadre[i])):
                if j==0 :
                    file.write("\nCapitano : ", end="")   # Print che non va accapo , resta inline
            file.write(f"{(squadre[i])[j]}")
        
    # Chiedo se si wuole ripetere il sorteggio
    yn = True
    while True:
       
        redraw = input("Reapeat the draw ? [Y/N]")
        if redraw.lower() == 'y':
            yn = True
            break
        elif redraw.lower() == 'n':
            yn = False
            break
        else:
            pass
        
