# TIPI DI DATI COMPLESSI

# int interi
num = 3

# float
altezza = 1.70 #dichiara e inizializza un float

# chr si usano gli apici singoli 
char ='c'

# str si usano gli apici doppi
str_1 = "ciao"

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
[int for _ in range(6)] #array di 6 int
[[] for _ in range(6)] #array di 6 array

print(numeri)
numeri.append(60)
print(numeri)

for numero in numeri:
    print(numero)

# Liste
# Una lista a differenza degli array può accogliere come elementi tipi diversi di dati
numeri_lista = [10,"20",30,40,50] #dichiarazione e inizializzazione di una lista
numeri_lista.append(60)
print(numeri_lista)

#Dizionario

voti = {"matematica":28,   #definisce elementi complessi sottoforma di chiave valore
        "informatica":30
        }
voti["Fisica"]=26          #Aggiungo una nuova coppia chiave valore
print(voti)
print (f"il voto di matematica è : {voti["matematica"]}") #faccio riferimento al valore della chiave matematica

# Usa snake_case per i nomi delle variabili