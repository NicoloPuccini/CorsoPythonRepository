import ast
import os
import random

file_path = "./Compiti/09_CalcolatriceRandom/CalcolatriceRandom_SaveFile.txt"
operations = ("+","-","*","/")
empty_saving_dict = {'punteggio' : 0 , 'round' : 1 , "last_round_data" : (0,0,0)}

#Gestione del salvataggio dati mediante dizionario su file
#Se non c'è già scrivo il file
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
round = saved_dict["round"]
last_round_data = saved_dict ["last_round_data"]


#Inizio partita

#Se è presente un file di salvataggio ofre la scelta di utilizzarlo
if not (round == 1 and punteggio == 0 and last_round_data ==(0,0,0)) :
    while True:
        in_str = input("Ci sono dati di salvataggio.\nDesideri continuare la partita interrotta ? [Y/N]")
        if in_str.strip().lower() == "y" :
            break
        if in_str.strip().lower() == "n" :
            round = 0
            punteggio = 0
            last_round_data = (0,0,0)
            break

#inizia partita
while round < 11 :
    #Se non sono ancora stati estratti i numeri del round 
    if last_round_data == (0,0,0) :
        num_1 = random.randint(0,11)
        operation = random.choice(operations)
        num_2 = random.randint(0,11)

        if operation =="-":
            num_2 = random.randint(0,num_1)

        if operation == "/" :
            num_2 = random.randint(1,11)
        last_round_data = (num_1,operation,num_2)
#Se ho già i numeri da un salvataggio precedente
    else:
        num_1 = last_round_data[0]
        num_2 = last_round_data[2]
        operation = last_round_data[1]


#Controlli (dovrebbero innescarsi solo modificando i valori nel file di salvataggio)
    if operation == "+":
        correct_ans = num_1 + num_2
    elif operation == "-" :
        if num_2 <= num_1:
            correct_ans = num_1 - num_2
        else:
            correct_ans = "Error"
    elif operation == "*" :
        correct_ans = num_1 * num_2
    elif operation == "/":
        if num_2 != 0 :
            correct_ans = int(num_1 / num_2)
        else :
            correct_ans = "Error"
    else :
        correct_ans = "Error"
    
    if correct_ans == "Error":
        print("\nCi deve essere stato un errore di calcolo, la partita verrà resettata\n")
        punteggio = 0
        round = 1
        last_round_data = (0,0,0)
        continue
    
    #Aggiorno il dizionario 
    updated_dict = saved_dict
    updated_dict["last_round_data"] = last_round_data
    updated_dict["punteggio"] = punteggio
    updated_dict["round"] = round
    #Salvo il dizionario su file 
    with open(file_path, "w", encoding="utf-8") as file :
        file.write(str(updated_dict))

#Chiedo all'utente di risolvere l'operazione
    while True :
        ans = input(f"\nRound : {round}\nPunteggio : {punteggio} \nQuanto fa : {last_round_data[0]} {last_round_data[1]} {last_round_data[2]}\n")
        if ans.isdigit():
            ans = int(ans)
            break
        print("\nLa risposta deve essere un numero\n")
    
    #Comparo le risposte 
    if correct_ans == ans :
        print("Giusto!\n")
        punteggio += 1
    else:
        print("Sbagliato\n")

    #Incremento il round e pulisco le variabili locali
    round += 1
    last_round_data = (0,0,0)

#Gestisci il fine partita
print(f"\nHai totalizzato {punteggio} punti\n")
#Aggiorno il dizionario 
#Salvo il dizionario su file 
with open(file_path, "w", encoding="utf-8") as file :
    file.write(str(empty_saving_dict))