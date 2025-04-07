#INDOVINA_PAROLA
import ast
import os
import random

file_path = "./Compiti/08_Indovina_Parola/IndovinaParola_SaveFile.txt"
#file_path = "IndovinaParola.txt"
empty_saving_dict = {'punteggio' : 0 , 'numero_partita' : 0 , 'parole':['rana', 'fringuello', 'cane','zuzzurellone','cannuccia']}

#Se non c'è scrivo il file
if not os.path.exists(file_path):
    with open(file_path, "w", encoding="utf-8") as file :
    
        file.write(str(empty_saving_dict))
#Leggo dal file il dizionario
with open(file_path, "r") as file:
    for line in file:
        saved_dict = line
        print(saved_dict)

saved_dict = ast.literal_eval(saved_dict)
print(saved_dict)
#Recupero dati dal dizionario
punteggio = saved_dict["punteggio"]
num_partita = saved_dict["numero_partita"]
#Inizio la partita
stop_plaing = False
while not stop_plaing:
    #Incremento numero partita
    num_partita = num_partita + 1

    #Estraggo una parola dalla lista e mischio le lettere
    rand_word = random.choice(saved_dict["parole"])
    shuffled_word = [*rand_word]
    random.shuffle(shuffled_word)
    shuffled_word = "".join(shuffled_word)

    print(f"\nPartita N : {num_partita}\nPunteggio : {punteggio}\nIndizio : {shuffled_word}")
    choiced_word = input("Prova ad indovinare :  ")
    choiced_word = choiced_word.strip()
    #Confronto
    if(choiced_word == rand_word ):
        print("Hai vinto")
        punteggio = punteggio + len(rand_word)
    else :
        print("Hai perso")
    while True :
        ans = input("Do you wish to play again ? [Y/N]")
        if(ans.upper() == "Y" ):
            stop_plaing = False
            break
        if(ans.upper()=="N"):
            stop_plaing = True
            break
#Aggiorno il dizionario
updated_dict = saved_dict
updated_dict["numero_partita"] = num_partita
updated_dict["punteggio"] = punteggio
#Salvo il dizionario su file 
with open(file_path, "w", encoding="utf-8") as file :
    
    file.write(str(updated_dict))

