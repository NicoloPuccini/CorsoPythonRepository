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
set_1 = {"sedano", "carote", "patate" ,"cavolo", "sedano"}
print(set_1)              # Non stamperà 2 sedani ma solo uno perchè gli elementi 
                          #di un set non possono avere duplicati

#metodi e operazioni non presenti in set:
#Non si può accedere direttamente ad un valore specifico del set
#set_1.insert(0,"mais")   
#set_1.sort()
#set_1.reverse()

#metodi di set:
"sedano" in set_1      # true se sedano è contenuto in set_1

#Sia discard che remove levano uno specifico elemento dal set , 
# la differenza fra i due è che remove genera un errore se l'elemento non è presente nel set 
set_1.remove("mais")
set_1.discard("mais")

set_1.add("lattuga") #Aggiunge un elemento al set
set_1.update(["uova","formaggio"]) #Amplia gli elementi del set con un iterabile (una lista,un set)

set_1.pop() #Estrae un elemento a caso dal set e lo rimuove 
set_1.clear() #Cancella tutto il set











# Tuple
#Una tupla non può essere modificata in alcun modo dopo la creazione , sono const 
#Sono piu veloci e meno dispendiose delle liste.
#ammettono duplicati
#E' ordinata (mantiene l'ordinamento)


bi_tupla = (1,2,9,10)
tupla_2 = ("cane", "gatto", "balena")

tupla_2[0] #Posso leggere direttamente agli elementi (leggendoli)

#tupla_2[1] ="gallina"              #ma non posso modificarli QUESTO DA ERRORE !
#tupla_2.insert(0,"scoiattolo")                         #Anche questo da ERRORE!

tupla_2.count("cane")   #Restituisce le occorrenze di cane nella tupla  
                        #(cioè quanti cane sono nella tupla)

tupla_2.index("cane")   #Ritorna l'indice (posizione) della prima occorrenza di cane 
                        #che trova nella tupla 

range(*bi_tupla)     #  * Permette di spacchettare la tupla per poterla usare 
                     # come argomento di un metodo


any(bi_tupla)        #La funzione any richiede come argomento un iterabile , 
                     #puo essere una tupla, una lista, una collezione o un 
                     # qualsiaso oggetto iterabile 
                     
                     # any ritorna true se trova almeno un true fra gli elementi 
                     # iterabili o altrimenti false.
                     #termina appena incontra un true per efficienza.



# Dizionario
#I dizionari sono ottimizzati per trovare un argomento al suo interno (find)
# Memorizza i dati in coppie chiave valore 
# Il dizionario è una memoria non ordinata , modificabile e indicizzata.
#Le chiavi sono univoche
#il tipo dei valori può essere diverso , le chiavi devono avere tutte lo stesso tipo 

diz_1 = {"mela":2, "banana":3, "ciliegia":5}

diz_1["mela"] = 4  #Modifica il valore associato alla chiave 

diz_1["fragola"] = 6 #Aggiunge una nuova coppia chiave valore 

diz_1.pop("banana")  #Rimozione di una coppia chiave valore e ritorna il valore 

diz_1["fragola"] = diz_1.pop("mela") #Sostituisce la chiave mela con la chiave fragola 

diz_1.keys()    #Ritorna la lista delle chiavi
diz_1.values()  #Ritorna la lista di tutti i valori
diz_1.items()   #Ritorna una lista di tuple con le coppie chiave valore 

diz_1.clear()   #cancella il dizionario

