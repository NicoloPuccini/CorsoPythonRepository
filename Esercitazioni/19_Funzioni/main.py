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


#Una funzione può restituire pi valori :
def divisione (dividendo,divisore):
    quoziente = dividendo//divisore
    resto =  dividendo% divisore
    return quoziente, resto         #Restituisce una tupla con i valori
                                    
                                    #Return fa uscire immediatamente dallo scope
q,r = divisione(10,3)
print(f"Quoziente:{q}\nResto:{r}")                                    #della funzione
