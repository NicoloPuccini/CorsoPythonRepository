# GESTIONE DELLE ECCEZIONI
#Cattura solo gli errori che sai gestire
#utilizza i costrutti : try, except e finally
# 
# Il blocco try deve contenere il codice che può scatenare un errore
# Il blocco except contiene il codice da eseguire quando si verifica un errore 
#
#Quando la line nel blocco try esegue la linea che scatena l'errore , va ad eseguire il codice nel blocco except
#Infine torna nel punto in cui si era scatenato l'errore e riprende ad eseguire da li 
try :
    x = 10/0  #Ovviamente darà errore

except ZeroDivisionError as e :
    print(f"Errore : {e}")

#vediamo gli errori piu comuni :

#Value error capita quando provo a fare casting a tipi che non possono contenere il valore
try:
    numeri= int("ciao")
except ValueError as e :
    print(f"Errore: {e}")

#Overflow quando supero i limiti di memoria del dato 
try:
    numero = int("100000000000000000000000000000000000000000000000000")
except OverflowError as e :
     print(f"Errore: {e}")

#IndexError Quando provo a accedere con indici che eccedono la lunghezza dell'oggeto
try:
    lista = [1,2,3]
    elemento = lista[3]  #indice non valido
except IndexError as e :
    print(f"Errore : {e}")

#KeyError : chiave non trovata in un dizionario
try:
    dizionario = {"a" : 1, "b" : 2}
    valore = dizionario["c"] #provo a chiamare una chiave inesistente
except KeyError as e :
    print(f"Errore : {e}")


#FileNotFoundError : file non presente
try:
    with open("file_non_esistente", "r") as file:
        contenuto = file.read()
except FileNotFoundError as e:
    print(f"Error : {e}")

#Import error : Modulo non trovato 
try:
    import modulo_inesistente
except ImportError as e :
    print(f"Errore: {e}")


#Type error
try:
    int("345")+"rtyui"
except TypeError as e :
    print(f"Error : {e}")


#Atribute Error :
try:
    x = None
except AttributeError as e :
    print(f"Error : {e}")



#Catturare un errore generico (sconsigliato)
try:
    x = int("rupe")
except Exception as e :   #Cattura qualsiasi tipo di errore , meglio evitare 
    print(f"Error : {e}")


#Posso incatenare e gestire piu tipi di eccezioni :

try:
    x = int("rupe")
except TypeError as e :
    print(f"Error : {e}")
except ValueError as e :
    print(f"Error as : {e}")        #Si bloccherà al primo errore che trova



#FINALLY
try :
    number = int("abc")
except ValueError as e :
    print(f"Error : {e}")
finally :
    print("Il finally viene eseguito comunque che si verifichi o meno l'errore")    #Di solito viene usato per chiudere 
                                                                                    # le comunicazioni con file o db


#TRY EXCEPT ELSE FINALLY
#l'else viene eseguito solo se non si verifica l'errore
#il finally viene eseguito comunque
try:
    f = open("dati.txt","r")
    contenuto = f.read()
except FileNotFoundError as e :
    print(f"Error :{e}")
else :
    print("File letto con successo")
    print(contenuto)
finally:
    print("chiusura del blocco")
    try:
        f.close()
    except NameError:
        print("Il file è già chiuso")


#RAISE lanciare un errore volontariamente e personalizzato
#Viene usato soprattutto per fare Debug
try:
    raise ValueError("Questo è un errore personalizzato") #Viene scatenato per forza
                                                          #usando rise
except ValueError as e :
    print(f"Errore : {e}")

