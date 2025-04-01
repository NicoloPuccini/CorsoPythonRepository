#STRINGHE

nome =  "Giovanni "
len(nome)  #Restituisce la lunghezza della stringa

nome.isspace()  #Restituisce true se contiene uno o piu spazi vuoti
                #NON rileva la stringa vuota

nome.lower()   #Output : giovanni
nome.upper()   #Output : GIOVANNI

nome.strip()   #Leva gli spazi vuoti a fine o inizio stringa 
               #(In altri linguaggi viene chiamato trim)

nomi = "Giovanni, Stefano,Oronzo"
nomi3 = nomi.split(",")  #Ritorna una lista i cui elementi sono i pezzi della 
                         #stringa intervallati dalle ","

nome.replace("io","x") #sostituisce pezzi di stringa con altri 
print(nome.replace("io","x"))

nome[0:3] #Taglia la stringa ritornando solo l'intervallo specificato (Slicing)

nome in nomi #Ritorna true se trova la porzione di stringa nell'altra stringa 

nome.find("vanni") #Trova la prima occorrenza di una substring e ne ritorna 
                   #l'indice del primo carattere(dall'inizio alla fine)

nome.rfind("o")    #Trova l'ultima occorrenza della substring nella stringa
                   #dalla fine all'inizio

nome.startswith("G")  #Ritorna true se la stringa inizia con la substring

nome.endswith("i")    #Ritorna true se la stringa finisce con la substring

nome_2 = "Silvio"
print("{} e {}".format(nome , nome_2 )) #Inserisce il valore dellla variabile 
                                        #nella stringa

#Conversioni implicite
eta = 21               #Ora è un int
eta_2 = eta + 1.5      #Ora è un float

type(eta)              #Ritorna il tipo di dato 

#Conversione esplicita
int(eta_2)             #Ritorna la parte intera del float


#Parsing di stringhe
eta_string = "uno"
eta_string = "12"
try:
    eta_int = int(eta_string)
    print("conversione riuscita")
except ValueError :
    print("Conversione fallita : La stringa non è un numero valido")
    import sys
    print(f"Tipo di errore:{sys.exc_info()[0]}")



