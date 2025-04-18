#FUNZIONI

#In python il tipo del ritorno della funzione non va specificato e può essere di qualsiasi tipo

def stampa():
    print("hai chiamato la funzione stampa")

def stampa_messaggio (messaggio) :
    print(messaggio)

def somma (a,b ):
    return a + b

def somma(a,b) :
    print(a+b)

#Gestisce da solo i tipi degli output e degli argomenti passati alla funzione

#Una funzione deve necessariamente avere un nome descrittivo e esebuire un unico task
#Le funzioni devono avere non piu di 20 righe


#Per chiamare una funzione basta : 
i=23
j=-2
somma(i,j)


#Una funzione può restituire piu valori :
def divisione (dividendo,divisore):
    quoziente = dividendo//divisore
    resto =  dividendo% divisore
    return quoziente, resto         #Restituisce una tupla con i valori

                                    #Return fa uscire immediatamente dallo scope
q,r = divisione(10,3)
print(f"Quoziente:{q}\nResto:{r}")                                    #della funzione

#DocString
def funzione () :
    """ Se nella prima linea della funzione metti un commento con tre apici
        ottieni un docstring , è buona norma scrivere una breve documentazione di cosa fa
        la funzione. La documentazione verrà poi mostrata con l'hoover sulla funzione
    """

#ARGOMENTI PRESI COME REFERENCE

#Gli argomenti passati a una funzione sono presi per riferimento se sono oggetti mutabili
#(Ovveto : liste , dizionari , oggetti di una classe (almeno di default) )
def aggiungi (i_list) :
    i_list.append("ciao")

lista = []
aggiungi(lista)     #Sto a tutti gli effetti modificando il contenuto della variabile lista
print (f"\n Ho aggiunto un elemento alla lista :{lista}")

#Se l'argomento passato è un oggetto immutabile (int , float , string , tuple)
def incrementa (i) :
    i = i + 1

numero = 1
incrementa(numero)  #numero non è stato preso per riferimento perchè è un int 
                    #(quindi incrementa sta lavorando solo con una copia del valore di numero )
print (f"\nla variabile numero non è stata modificata : numero = {numero}")




#FUNZIONI E VARIABILI GLOBALI 

#E' buona norma non usare variabili globali nelle funzioni senza passarle come argomento
#Una funzione può accedere a ogni variabile globale
num_3 = 2
def print_num_3 ():
    print(f"num_3 = {num_3}")

#chiamo la funzione:
print_num_3()

#Tuttavia non posso modificare le variabili globali all'interno di una funzione 
#a meno che non le passo come argomenti o uso global
def print_num_3 ():
    num_3 = 35
print(f" non ha modificato il valore di num_3 = {num_3}")

#Per modificare una variabile globale senza passarla come argomento:
x = 5
def azzera_x ():
    global x
    x = 0
azzera_x()
print(f"Ho modificato il valore della variabile globale x = {x}")