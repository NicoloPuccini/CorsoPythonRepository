import random

class Personaggio :
    def __init__(self,nome):
        self.nome = nome
        self.salute_max =100
        self.salute = 100
        self.attacco_min = 10
        self.attacco_max = 20
        self.storico_danni_subiti = []
        self.inventario = []

    def attacca(self,bersaglio):
        danno = random.randint(self.attacco_min,self.attacco_max)
        #Critico : se esce un 20 raddoppi il danno
        if random.randint(1,21)==20 :
            danno *=2
            print("Hai Crittato !")
        print(f"{self.nome} attacca {bersaglio.nome} per {danno} punti!\n")
        bersaglio.subisci_danno(danno)


    def subisci_danno(self, danno):
        self.salute -= danno
        if self.salute < 0:
            self.salute = 0
        self.storico_danni_subiti.append(danno)
        print(f"Salute di {self.nome} : {self.salute}\n")

    def sconfitto(self):
        return self.salute <= 0

    def recupero_hp (self, hp_recuperati):
        self.salute += hp_recuperati
        hp_curati = hp_recuperati
        if self.salute > self.salute_max:
            hp_curati = hp_recuperati - (self.salute - self.salute_max)
            self.salute = self.salute_max
        print(f"Hai recuperato : {hp_curati} hp")

    def regen_post_duello(self):
        cura = round(self.salute*30/100)
        self.recupero_hp(cura)

    #Permette al personaggio di usare oggetti di classe Item presenti nell'inventario
    def usa_oggetto(self,oggetto, bersaglio=None ):    #Aggiungiamo un campo bersaglio e gli diamo valore di default nullo
                                                            #L'inizializzazione del bersaglio in questo modo è opzionale
        if oggetto in self.inventario:
            print(f"{self.nome} usa un {oggetto.nome}")
            try:
                risultato = oggetto.usa(self if bersaglio == None else bersaglio)
                self.inventario.remove(oggetto)
                return risultato
            except NotImplementedError as e :
                print(f"Errore : {e}")
            print("Oggetto non presente nell'inventario")
    

    def saccheggia_nemico(self, nemico):
        #Sconfitto un nemico ti appropri del suo inventario
        #Unisco l'inventario del nemico sconfitto all'inventario del giocatore
        self.inventario=[*self.inventario,*nemico.inventario]
        print(f"{self.nome} ha ottenuto {nemico.inventario}")
        print(self.inventario)
        #recupero salute del 30% quando si vince un duello
        #giocatore.regen_post_duello()


class Mago (Personaggio):   #Eredita da personaggio
    def __init__(self,nome):
        super().__init__(nome)
        self.nome = "🔥 "+ nome
        self.salute_max = 50
        self.salute = 50
    
    def attacca(self,bersaglio):
        danno = random.randint(15,30)
         #Critico : se esce un 20 raddoppi il danno
        if random.randint(1,21)==20 :
            danno *=2
            print("Hai Crittato !")
        print(f"{self.nome} lancia una palla di fuoco su {bersaglio.nome} per {danno} !")
        bersaglio.subisci_danno(danno)

    def regen_post_duello(self):
        cura = round(self.salute*20/100)
        self.recupero_hp(cura)

class Guerriero (Personaggio) :
    def __init__(self, nome):
        super().__init__(nome)
        self.nome = "⚔ "+ nome

    def attacca(self, bersaglio) :
        danno = random.randint(self.attacco_min + 15, self.attacco_max +20)
         #Critico : se esce un 20 raddoppi il danno
        if random.randint(1,21)==20 :
            danno *=2
            print("Hai Crittato !")
        print(f"{self.nome} colpisce {bersaglio.nome} con la spada per {danno} !")
        bersaglio.subisci_danno(danno)

class Ladro (Personaggio) :
    #SUPER
    #Super permette si recuperare tutto il codice già esistente del metodo
    #dalla classe padre per poi aggiungere un qualcosa,
    #in questo caso modifichiamo dei campi del costruttore
    def __init__(self, nome):
        super().__init__(nome)
        self.nome = "🔪 "+ nome
        self.salute_max = 50
        self.salute = 50
        self.attacco_min = 0

    def attacca(self,bersaglio):
        danno = random.randint(0,self.attacco_max+40)
        #Critico : se esce un 20 raddoppi il danno
        if random.randint(1,21)==20 :
            danno *=2
            print("Hai Crittato !")
        print(f"{self.nome} pugnala {bersaglio.nome} per {danno} !")
        bersaglio.subisci_danno(danno)

    def regen_post_duello(self):
        cura = random.randint(10,40)
        self.recupero_hp(cura)

class Item :
    #Costruttore:
    def __init__(self,nome,effetto,valore):
        self.nome = nome
        self.effetto = effetto
        self.valore = valore
        self.usato = False

    def usa(self, bersaglio):
            raise NotImplementedError("Questo metodo deve subire un override , questa classe è abstract")
        #Si usa not implemented error quando un oggetto non ha un effetto
        #definito , nel nostro caso object è una classe abstract


class PozioneGuarigione (Item):
    def __init__(self):
        super().__init__("Pozione curativa","cura",30)
        

    def usa(self, bersaglio):
        bersaglio.recupero_hp(self.valore)
        self.usato = True

class Bomba (Item):
    def __init__(self):
        super().__init__("Bomba", "esplode", 200)

    def usa (self, bersaglio):
        print(f"La bomba esplode infliggendo a {bersaglio.nome} {self.valore} danni")
        bersaglio.subisci_danno(self.valore)

class PozioneAttacco (Item):
    def __init__(self):
        super().__init__("Pozione della furia", "boost", 40)

    def usa (self,bersaglio):
        print(f"{bersaglio.nome} è piu potente")
        bersaglio.attacco_max += self.valore




# Funzione senza parametri: stampa un messaggio di benvenuto
def mostra_benvenuto():
    print("Benvenuto nel gioco di combattimento!")  # Non prende input, non restituisce nulla. Serve solo a stampare testo

def avversario_sconfitto(nemico,nemici):
    if nemico.sconfitto() :
        print("Hai vinto il duello!")
        #elimino il nemico dalla lista di nemici
        nemici.remove(nemico)
        #Controllo se si è vinto il torneo
        if len (nemici)==0 :
            return 2
        return True
    else:
        return False


# loop principale di gioco
def gioca_torneo():
    # stampo il messaggio di benvenuto
    mostra_benvenuto()

    # Creiamo i personaggi
    nomi_nemici = ["nemico1", "nemico2", "nemico3"]
    tupla_classi =(Ladro,Mago,Guerriero)
    nemici = []
    for nome in nomi_nemici:
            #Sorteggio la classe del nemico
            classe_sorteggiata = random.choice(tupla_classi)
            #Creo l'istanza del nemico
            nemico = classe_sorteggiata(nome)
            #Assegno al nemico oggetti(solo bombe)
            nemico.inventario.append(Bomba())
            nemico.inventario.append(PozioneGuarigione())
            nemici.append(nemico)

    print(f"nemici :  {nemici}")
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

    giocatore = classe_giocatore("Personaggio Principale")

    #Questo ciclo genera un nuovo nemico e fa ripartire il duello fino a che 
    #il personaggio non muore 
    win_torney = False
    while not giocatore.sconfitto() :

        #Pesco il nemico a caso dalla lista nemici
        nemico = random.choice(nemici)

        # definiamo un contatore per i turni
        turno = 1

       

        # Ciclo finché qualcuno perde (quando la salute è zero)
        while True:
            print(f"Turno {turno}:")
            print(f"Danni ricevuti dal giocatore : {giocatore.storico_danni_subiti}")

            #Il giocatore usa il primo oggetto che ha in inventario
            if not len(giocatore.inventario) == 0 :
                oggetto = giocatore.inventario[0]
                if isinstance(oggetto,Bomba):
                    giocatore.usa_oggetto(oggetto, bersaglio=nemico)
                    #controlliamo se il nemico è morto , puo succedere con la bomba
                    risultato = avversario_sconfitto(nemico,nemici)
                    if risultato == 2:
                        win_torney = True
                    if risultato:
                        giocatore.saccheggia_nemico(nemico)
                        break  # esci dal ciclo nel caso di vittoria
                else:
                    giocatore.usa_oggetto(oggetto)

            # Attacco del giocatore
            giocatore.attacca(nemico)

            # controlla se il nemico è sconfitto
            risultato = avversario_sconfitto(nemico,nemici)
            if risultato == 2:
                win_torney = True
            if risultato:
                giocatore.saccheggia_nemico(nemico)
                break  # esci dal ciclo nel caso di vittoria


            # Attacco del nemico
            nemico.attacca(giocatore)

            # controlla se il giocatore è sconfitto
            if giocatore.sconfitto() :
                print("Sei stato sconfitto!")
                break # esci dal ciclo nel caso di sconfitta

            # incremento il contatore dei turni
            turno += 1

        #controllo se il personaggio ha vinto il torneo e nel caso rompo il while esterno
        if win_torney == True:
            print("Hai vinto il torneo")
            break



# punto di ingresso
def main():
    gioca_torneo()

# Esegui il gioco
if __name__ == "__main__":
    main()