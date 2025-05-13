

class InterfacciaUtente : #E' un nome un po lungo , posso usare as quando lo importo 
                          #per dargli un alias e usare quello per richiamarlo
    @staticmethod
    def chiedi_input(messaggio, opzioni=None):
        """Chiede un input stringa che deve coincidere con una delle opzioni,
        ritorna la stringa input dell'utente se coincide con una delle opzioni
        """
        while True:
            risposta = input(messaggio).strip()
            if opzioni:
                if risposta.lower() in [o.lower() for o in opzioni]:
                    return risposta
                else:
                    print(f"Input non valido! Scelte valide : {", ".join(opzioni)}")
            else:
                return risposta

    #Nella documentazione metti sempre un esempio d'uso per le tue funzioni , 
    #Nei DocString è obbligatorio.

    """Esempio d'uso :

    from utils.interfaccia import InterfacciaUtente as IU
    #Scegli una classe manualmente:
    classe = IU.chiedi_input("Scegli il tuo personaggio (Mago,Ladro,Guerriero): "),
    opzioni=["mago","guerriero","ladro"]
    )
    print(f"Hai scelto:{classe}")
    """

    @staticmethod
    def chiedi_numero(messaggio , minimo=None, massimo=None):
        while True:
            try:
                numero= int(input(messaggio))
                if minimo is not None and numero < minimo:
                    print(f"Devi inserire un numero maggiore o uguale a {minimo}.")
                    continue
                if massimo is not None and numero>= massimo :
                    print(f"Devi inserire un numero minore o uguale a {massimo}")
                    continue
                return numero
            except ValueError:
                print("Input non valido devi inserire un numero intero")


    @staticmethod
    def conferma(messaggio):
        while True:
            risposta = input(messaggio+ "(y/n):").strip().lower()
            if risposta == "y":
                return True
            elif risposta == "n":
                return False
            else:
                print("Input errato , rispondi con y or n")

