import random
from inventario.inventario import Inventario

class Personaggio :
    def __init__(self,nome):
        self.nome = nome
        self.salute_max =100
        self.salute = 100
        self.attacco_min = 10
        self.attacco_max = 20
        self.storico_danni_subiti = []
        self.inventario = Inventario(self)

    def attacca(self,bersaglio):
        danno = random.randint(self.attacco_min,self.attacco_max)
        #Critico : se esce un 20 raddoppi il danno
        if random.randint(1,21)==20 :
            danno *=2
            print(f"{self.nome} ha crittato !")
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
        if oggetto in self.inventario.lista_inventario:
            print(f"{self.nome} usa un {oggetto.nome}")
            try:
                risultato = oggetto.usa(self if bersaglio == None else bersaglio)
                self.inventario.rimuovi(oggetto)
                return risultato
            except NotImplementedError as e :
                print(f"Errore : {e}")
            print("Oggetto non presente nell'inventario")


    def saccheggia_nemico(self, nemico):
        #Sconfitto un nemico ti appropri del suo inventario
        #Unisco l'inventario del nemico sconfitto all'inventario del giocatore
        print(f"{self.nome} ha ottenuto : ")
        for i in nemico.inventario.get_nomi_oggetti():
            print(i)
        nemico.inventario.riversa_in(self)
        print(self.inventario.mostra())
        #Elimino l'inventario di nemico
        nemico.inventario.svuota()
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