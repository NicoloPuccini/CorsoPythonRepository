# Random

import random #importo la libreria random

#metodi di Random

rand = random.randint(1,101) #sorteggia un int in un range chiuso da 1 a 100

random.choice(["ciao","hello"]) #sorteggia un elemento da una lista

lista=[1,2,3,4]
random.shuffle(lista) #rimescola l'ordine degli elementi di una lista

n =5 #numero di escrazioni
random.sample([1,2,3,4,5],n) #sorteggia n elementida una lista

random.seed(42) #permette di usare un seme per  drogare , i risultati saranno in tal caso ripetibili
                #pi estrazioni daranno gli stessi risultati

import time
time.sleep(random.randint(3,8)) #Blocca il processo per il tempo in secondi specificato

random.random() #sorteggia una float tra 0 e 1
random.uniform(1,10) #sorteggia un float nel range specificato