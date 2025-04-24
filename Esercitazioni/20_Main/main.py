# MAIN

#L'entry point di una porzione di codice è la funzione main in molti linguaggi
#In python non è obbligatorio ma è buona pratica mantenere la convenzione

def main():
    nome=input("Inserisci il tuo nome : ")
    print(f"Ciao {nome}")

#Permette al programma quando chiamato direttamente da terminale usando :
#nome_file.py

if __name__ == "__main__":    #Se il nome fel file è main
    main()                      #Eseguirà per prima il corpo della funzione main

# ? questa istruzione quando e come viene letta ? 

#Python non ha access modifiers