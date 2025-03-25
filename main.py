

# commento a riga singola


"""
Commento a riga multipla
"""

# il metodo print stampa a schermo una stringa
print("Hello world")

# il metodo input recepisce un linea di testo da tastiera e la restituisce come
# stringa
nome = input("inserisci il tuo nome ")
print("Ciao" , nome)

# Concatenazione stringhe e variabili con il segno +
print("Ciao" + nome + "!")

# alternativamente si può usare l'interpolazione di stringa , metodo piu
# efficente che permette di concatenare agevolmente stringhe e variabili
print(f"Ciao {nome} !")

# Dichiaro una variabile intera eta_int
eta_int = 47 # desume che è un int perchè sono numeri e mancan gli apici
print(eta_int) # riesce a stamparla anche se non è una string perchè c'è un overload di print

eta_str = str(eta_int) #conversione da intero a stringa

# Faccio un import , ricorda che andrebbero sempre all'inizio del file
import msvcrt
tasto = msvcrt.getch() #Legge il tasto premuto

# Se il tasto premuto è enter
if tasto == b'\r': # '\r' rappresenta in ASCII il tasto enter
    # b indica che è un byte
    print("Hai premuto il tasto enter")
if tasto.lower() == b's': #Confronto il tasto convertito in minuscolo con 's'
    # lower. converte il valore di tasto in minuscolo
    print("Hai premuto 's' ")

    exit()