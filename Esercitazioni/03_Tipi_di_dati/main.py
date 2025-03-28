# TIPI DI DATI 

# int interi
num = 3

# float
altezza = 1.70 #dichiara e inizializza un float

# chr si usano gli apici singoli 
char ='c'

# str si usano gli apici doppi
str_1 = "ciao"

#alcuni metodi di string
import string
speciali = string.punctuation #ritorna una stringa con tutti i caratteri speciali
alfabeto_maiuscolo = string.ascii_uppercase #Ritorna la stringa con tutto l'alfabeto maiuscolo
alfabeto_minuscolo = string.ascii_lowercase #ritorna la stringa con tutto l'alfabeto minuscolo
numeri = string.digits  #Ritorna la stringa con tutti i numeri 
# Booleano 
maggiorenne = True

# Variabili di tipo Data 
from datetime import datetime
data_nascita = datetime(2000,12,30)

print(data_nascita)

# TIPI DI DATI COMPLESSI (o strutture di dati)

# Array
import array
numeri = array.array('i',[10,20,30,40,50]) #Dichiarazione e inizializzazione di array interi 
                                            # 'i' identifica un array di interi

#inizializzare array di altri oggetti vuoti 
[int for _ in range(6)] #array di 6 int
[[] for _ in range(6)] #array di 6 array

print(numeri)
numeri.append(60)
print(numeri)

for numero in numeri:
    print(numero)









# Liste (E' un array dinamico)

# (E' una Pila quindi con elementi non accessibile direttamente )
# Una lista a differenza degli array può accogliere come elementi tipi diversi di dati
# Ammette elementi duplicati
numeri_lista = [10,"20",30,40,50] #dichiarazione e inizializzazione di una lista
numeri_lista.append(60)
print(numeri_lista)

frutta=["mela","pera","banana","ananas","mela"]
frutta[2] # Posso accedere direttamente agli elementi della lista
frutta[-1]   #Accedo all'Ultimo elemento della lista 
frutta[-2]   #Accedo al penultimo elemento
frutta[::]   #Accedo a tunti gli elementi
frutta[::2]  #Accedo a tutti gli elementi dispari 
frutta[1:3]  #Accedo dal secondo fino al terzo elemento

print(dir(frutta)) #Stampa tutti i metodi del contenuto in questo caso la lista 
print(help(frutta)) #Stampa tutta la documentazione dell'oggetto 
print(help(frutta.append)) #Stampa la documentazione del metodo apend

len(frutta)       #Ritorna il numero di elementi della lista

"mela" in frutta  #Controlla se mela è presente in frutta e ritorna true o false, è CaseSensitive 
"Mela" in frutta  #ritornerà false perchè non c'è "Mela" nella lista ma "mela"

frutta.append("kiwi")  #Aggiunge un elemento alla lista in ultima posizione
frutta.extend(["mango","papaya"]) #Aggiunge alla lista gli elementi della lista argomento
frutta.remove("mela")   #Rimuove un elemento dalla lista ma non suoi duplicati, elimina solo la prima 
                        #che trova in lista

frutta.pop()            #ritorna l'ultimo elemento della lista e lo rimuove dalla lista

frutta= list(set(frutta))  #Rimuove gli elementi duplicati (perchè casta a set e poi di nuovo a list) e set non ammette duplicati

posizione = 2
frutta.insert(posizione,"pera")  #Inserisce l'elemento nella pposizione 
                                #specificata sovrascrivendo quello già presente

frutta.sort()  #Ordina gli elementi in ordine crescente 
frutta.reverse() #Inverte l'ordine degli elementi
frutta.sort(reverse=True) #Ordina gli elementi in ordine decrescente

frutta.index("mela")      #Sputa l'indice (la posizione) del primo elemento che trova che sia "mela"
                             #da errore se melone non è presente in lista

#if( frutta.index("melone")):        #E quindi questo NON FUNZIONA
print("FFFFUUUUUNGEEEEE") 

frutta.clear()      #cancella tutti gli elementi dalla lista

frutta.count("mela")  #Conta il numero di occorrenze di mela presenti nella lista 

frutta.copy()         #crea una copia di frutta ma legato agli stressi spazi di memoria 
                      #Quindi modificare uno modifica anche l'altro (E' un riferimento)



#Dizionario

voti = {"matematica":28,   #definisce elementi complessi sottoforma di chiave valore
        "informatica":30
        }
voti["Fisica"]=26          #Aggiungo una nuova coppia chiave valore
print(voti)
print (f"il voto di matematica è : {voti["matematica"]}") #faccio riferimento al valore della chiave matematica

# Usa snake_case per i nomi delle variabili





# Set 

# (Insiemi non ordinati di elementi non modificabili , gli elementi devono 
# essere dello stesso tipo, non ammette elementi duplicati)
insieme = {}




# Tuple

bi_tupla = (1,2)

range(*bi_tupla)     #  * Permette di spacchettare la tupla per poterla usare 
                     # come argomento di un metodo


any(bi_tupla)        #La funzione any richiede come argomento un iterabile , 
                     #puo essere una tupla, una lista, una collezione o un 
                     # qualsiaso oggetto iterabile 
                     
                     # any ritorna true se trova almeno un true fra gli elementi 
                     # iterabili o altrimenti false.
                     #termina appena incontra un true per efficienza.