#Creiamo un dizionario con due liste 

chiavi =["nome","cognome","eta"]
valori = ["giacomo", "cicogna",25]
persona = dict(zip(chiavi,valori))   # zip crea una lista di tuple che poi viene convertita a dizionario 
                                     #mediante la funzione dict()
print(persona)


#Raggruppa gli elementi in base alla prima lettera 
nomi = ["Anna", "Alberto","Marco","Luigi"]
gruppi = {}
for nome in nomi:
    #prendo la prima lettera
    first_let = nome[0].upper()
    #Aggiungo il nome al dizionario sotto la chiave della prima lettera
    if first_let not in gruppi :
        gruppi [first_let]=[]
    gruppi[first_let].append(nome)
    
print(gruppi["A"])
print(gruppi["A"][0])#output "Anna"


#Rubrica Telefonica
