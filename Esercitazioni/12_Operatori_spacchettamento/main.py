#OPERATORI DI SPACCHETTAMENTO

#"*" ed "**"
#Servono a spacchettare o espandere contenitori come liste , tuple e dizionari 
# Ottimo per usare questo tipo di dati complessi come ingresso a funzioni



numeri = [1,2,3]
print(numeri)   #Output : [1, 2, 3]
print(*numeri)  #Output :  1 2 3



numeri = (1,2,3)
print(numeri)      #Output : (1, 2, 3)
print(*numeri)     #Output : 1 2 3



dati = {"nome" : "Gianni", "eta": 30}
print(*dati)             #Stampa la chiave
print(*dati.values())    #Stampa i valori



# **  Va a cercarsi gli argomenti della funzione nel dizionario 
dati = {"nome" : "Gianni", "eta": 30}
def saluta(nome,eta):
    print(f"Ciao{nome},hai,{eta} anni !")

saluta(**dati)


#in assegnaione
a ,*b ,c = [1,2,3,4,5]
print(a) # assume il primi valore (Output:1)
print(b) # * dice a b che è una lista (Output: [2,3,4])
print(c) # (Output : 5)

#Unire liste
lista1 = [1,2,2]
lista2 = [3,4]
unione = [*lista1,*lista2]
print(unione)         #Output: [1,2,2,3,4]



#Unione di dizionari 
#Se ci sono chiavi duplicate l'ultima sovrascrive le altre
d1 = {"a" : 1, "b" : 2}
d2 = {"b" : 3, "c" : 4}
d_unito = {**d1,**d2}
print(d_unito)  # Output: {'a': 1, 'b': 3, 'c': 4}



#Mischiare valori normali e spacchettati
valori = [2,3,4]
nuova = [1,*valori,5]
print(nuova)    #Output : [1, 2, 3, 4, 5]



#Convertire string in lista
print([*"ciao"])    #Converte una sting in una lista in cui ogni char è un elemento della lista
                    #Output : ['c', 'i', 'a', 'o']


#convertire stringhe in tupla
print((*"ciao",))    #Output : ('c', 'i', 'a', 'o')


#convertire range in lista
print([*range(3, 6)])   #Output : [3, 4, 5]
