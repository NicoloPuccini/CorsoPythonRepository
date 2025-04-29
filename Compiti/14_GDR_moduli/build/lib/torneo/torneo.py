import random
from item.item import PozioneAttacco,PozioneGuarigione,Bomba
from personaggio.personaggio import Mago,Guerriero,Ladro,Personaggio
from torneo.duello import Duello

class Torneo :
    def __init__(self):
        self.turno = 1
        self.giocatore = None
        self.nemici = None
        self.win_tourney = False

    def mostra_benvenuto(self):
        # Funzione senza parametri: stampa un messaggio di benvenuto
        print("Benvenuto nel gioco di combattimento!")  # Non prende input, non restituisce nulla. Serve solo a stampare testo

    def setup(self):
        # Creiamo i personaggi
        nomi_nemici = ["nemico1", "nemico2", "nemico3"]
        tupla_classi =(Ladro,Mago,Guerriero)
        self.nemici  = []
        for nome in nomi_nemici:
                #Sorteggio la classe del nemico
                classe_sorteggiata = random.choice(tupla_classi)
                #Creo l'istanza del nemico
                nemico = classe_sorteggiata(nome)
                #Assegno al nemico oggetti(solo bombe)
                nemico.inventario.aggiungi(Bomba())
                nemico.inventario.aggiungi(PozioneGuarigione())
                self.nemici .append(nemico)

        print(f"nemici :  {self.nemici }")
        while True :
            n_classe_giorcatore = input("\nSeleziona la classe del tuo personaggio :" 
            "\n-1 Guerriero\n-2 Ladro\n-3 Mago\n").strip()
            if n_classe_giorcatore =="1":
                    classe_giocatore = Guerriero
                    break
            if n_classe_giorcatore =="2":
                classe_giocatore = Ladro
                break
            if n_classe_giorcatore == "3" :
                classe_giocatore = Mago
                break

        self.giocatore = classe_giocatore("Personaggio Principale")


    # loop principale di gioco
    def gioca_torneo(self):
        # stampo il messaggio di benvenuto
        self.mostra_benvenuto()
        self.setup()

        #Questo ciclo genera un nuovo nemico e fa ripartire il duello fino a che
        #il personaggio non muore
        self.win_torney = False
        while not self.giocatore.sconfitto() :
            #Pesco il nemico a caso dalla lista nemici
            nemico = random.choice(self.nemici)
            print(f"{nemico.nome} si erge minaccioso pronto ad affrontarti ")
            duello = Duello(self,nemico)
            # Ciclo finché qualcuno perde (quando la salute è zero)
            while True:
                #Creo un oggetto duello
                risultato = duello.gioca_turno(self)
                if risultato :
                    break
                else :
                    continue

            #controllo se il personaggio ha vinto il torneo e nel caso rompo il while esterno
            if self.win_tourney == True:
                print("Hai vinto il torneo")
                break