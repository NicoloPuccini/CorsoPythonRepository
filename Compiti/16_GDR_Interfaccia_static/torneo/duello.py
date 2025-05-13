from item.item import Bomba
from util.util import InterfacciaUtente as IU
#from inventario.inventario import Inventario

class Duello :
    def __init__(self,torneo,nemico):
        self.giocatore = torneo.giocatore
        self.nemico = nemico

    def avversario_sconfitto(self,nemico,torneo):
        if nemico.sconfitto() :
            print("Hai vinto il duello!")
            #elimino il nemico dalla lista di nemici
            torneo.nemici.remove(nemico)
            #Controllo se si è vinto il torneo
            if len(torneo.nemici)==0 :
                torneo.win_tourney = True
                return True
            return True
        else:
            return False


    def gioca_turno(self,torneo):
        print(f"Turno {torneo.turno}:")
        print(f"Danni ricevuti dal giocatore : {torneo.giocatore.storico_danni_subiti}")
        torneo.turno += 1

        azione_input = IU.chiedi_input("Scegli un azione :\n-1 Attacca\n-2 Usa oggetto",opzioni=["1","2"])
        if azione_input == "2":

            #Il giocatore usa il primo oggetto che ha in inventario
            if not self.giocatore.inventario.size() == 0 :
                oggetto = torneo.giocatore.inventario.prendi_item()
                if isinstance(oggetto,Bomba):
                    self.giocatore.usa_oggetto(oggetto, bersaglio=self.nemico)
                    #controlliamo se il nemico è morto , puo succedere con la bomba
                    risultato = self.avversario_sconfitto(self.nemico,torneo)
                    if risultato:
                        self.giocatore.saccheggia_nemico(self.nemico)
                        return True  # esci dal ciclo nel caso di vittoria
                else:
                    self.giocatore.usa_oggetto(oggetto)

        if azione_input == "1":
            # Attacco del giocatore
            self.giocatore.attacca(self.nemico)

        # controlla se il nemico è sconfitto
        risultato = self.avversario_sconfitto(self.nemico,torneo)
        if risultato:
            self.giocatore.saccheggia_nemico(self.nemico)
            return True  # esci dal ciclo nel caso di vittoria


        # Attacco del nemico
        self.nemico.attacca(self.giocatore)

        # controlla se il giocatore è sconfitto
        if self.giocatore.sconfitto() :
            print("Sei stato sconfitto!")
            return True # esci dal ciclo nel caso di sconfitta
        # incremento il contatore dei turni
        return False
