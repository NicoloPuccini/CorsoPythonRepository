#Le variabili che passo come parametro sono prese per riferimento o sono copie del valore ?
def incrementa (i) :
    i = i + 1

numero = 1
incrementa(numero)
print (f"\nla variabile numero è stata incrementata ? (se si dovrebbe essere 2) :{numero}")


#Dentro una funzione posso accedere a variabili globali ?
testo = "ciao"

def modifica_testo():
    return testo + "belli"
#Chiamo modifica_testo
print(f"Print testo modificato (Se una funzione può accedere a variabili globali dovrebbe dare : ciao belli) : {modifica_testo()}")


#Ma vale solo per le funzioni o tutti gli scope :
if True :
    variabile_locale_if = "Io sono una variabile locale"
print("Posso accedere ad una variabile creata localmente in un altro scope ? " + variabile_locale_if)