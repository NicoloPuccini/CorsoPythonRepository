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
