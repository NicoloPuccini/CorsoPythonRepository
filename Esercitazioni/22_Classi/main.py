# CLASSI

#Definizione della classe
class Animale :
    #Definiamo il costruttore della classe
    def __init__(self,nome):    # nome sarà il nome dell'oggetto
        #self è il riferimento all'istanza della classe
        #(self è la versione di python di this)
        self.nome = nome
        self.n_zampe = 4    #Qua definisco gli attributi della classe

    #Definiamo un metodo
    #Bisogna sempre passare compe primo parametro self , anche se non dovrò
    #passarlo come argomento quando chiamo il metodo
    def piscia_su (self, bersaglio):
        print(f"{self.nome} piscia su {bersaglio}")

# OVERRIDE del metodo

    #definisco un metodo
    def verso(self) :
        print("\nVerso animale")

class Cane (Animale) :   #Cane eredita da animale
    #faccio override del metodo verso :    (Non va dichiarato , si fa e basta, e sovrascrive il metodo del padre nella classe figlio)
    def __init__(self, nome):
        super().__init__(nome)

    
    def verso (self) :
        print("\nBau Bau !!")

class Anatra (Animale) :
    def __init__(self,nome):
                            #SUPER
                            #Super permette si recuperare tutto il codice già esistente del metodo
                            #dalla classe padre per poi aggiungere un qualcosa,
                            #in questo caso modifichiamo dei campi del costruttore
        super().__init__(nome)
        self.n_zampe = 2

    #Override
    def verso (self) :
        print("\nQua Qua !!")

class Cananatra (Anatra,Cane) :     #In python una classe può ereditare da piu classi
    #Ma quale dei due versi che eredita userà ? Va gestito facendo override, Python è molto
    #Permissivo ed implementa il metodo con quello della prima classe genitore (Anatra)
    def __init__(self,nome):
        super().__init__(nome)
        self.nome = "Canatra"


def main():
    #Creo un animale Birba
    birba = Animale("Birba")    #Genero un istanza di animale , generare un istanza
                                #significa invocare il costruttore _"_init__
    birba.piscia_su("Leo")  #chiamo il metodo

    gizmo = Cananatra("Gizmo")
    gizmo.verso()

#Entry point
if __name__ == "__main__" :
    main()


