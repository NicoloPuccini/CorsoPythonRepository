# COMPREHENSIONS

#Utile per scrivere codice pi compatto , non tutti lo sanno fare e quindi è buona
#norma mettersi daccordo con il team se usarle o meno
#Si può usare su liste , dizionari e set

#Si usano per creare o filtrare gli elementi nei contenuitori

#List Comprehension
#[espressione for elemento in collezione if condizione]

#Esempio: Crea una lista di quadrati
numeri = [1,2,3,4,5,6,7]
quadrati = [e**2 for e in numeri]  #** è la potenza
print(quadrati)

#Filtrare una lista di numeri pari
pari= [p for p in range(10) if p % 2 ==0]


#Trasformare le stringhe in una lista
nomi = ["nome1" , "nome2" , "nome3"]
maiusolizzati = [n.capitalize() for n in nomi]
print(maiusolizzati)

#con any
#Any ritorna true se la condizione è rispettata da almeno un elemento del contenitore 
almeno_un_pari = any(n % 2 == 0 for n in numeri )


#Creare, trasformare, inizializzare dizionari
lunghezze= {n: len(n) for n in nomi}
print(lunghezze)    #Output : {'nome1': 5, 'nome2': 5, 'nome3': 5}

#Con i set
caratteri = {c for c in "frutta"}
print(caratteri)  #Output : {'f', 't', 'a', 'u', 'r'}
#Ricorda che i set non ammettono duplicati e non hanno ordine 
#(Gli elementi all'interno non hanno ordine e possono cambiare posizione)


#Condizioni nella comprehension :
numeri = [1,2,3,4,5]
parita = ["pari" if n % 2 == 0 else "dispari" for n in numeri]
print (parita)  #Output : ['dispari', 'pari', 'dispari', 'pari', 'dispari']


#Non sempre ti serve l'elemento mentre cicli in questi casi per CONVENZIONE 
#si usa _ questo serve ad indicare che non usiamo l'elemento dell'iterabile che 
#stiamo ciclando
squadre = [[] for _ in range(5)]
#Questa comprehension crea una lista con dentro 5 liste