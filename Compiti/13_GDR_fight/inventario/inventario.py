
class Inventario :
    def __init__(self, i_proprietario):
        self.lista_inventario = []
        self.proprietario = i_proprietario

    def aggiungi(self,i_item):
        """Aggiungi un item all'inventario"""
        self.lista_inventario.append(i_item)

    def rimuovi(self, i_item):
        """Rimuove item dall'inventario"""
        self.lista_inventario.remove(i_item)
    
    def get_nomi_oggetti(self):
        tupla_nomi = (i.nome for i in self.lista_inventario)
        return tupla_nomi


    def mostra(self):
        if len(self.lista_inventario) != 0:
            print(f"\nInventario di {self.proprietario.nome} : ")
            for i in self.lista_inventario:
                print(f"- {i.nome}")
            print("\n")

    def svuota(self):
        self.lista_inventario.clear()

    def size(self):
        return len(self.lista_inventario)

    def riversa_in(self,i_giocatore):
        i_giocatore.inventario.lista_inventario = [*i_giocatore.inventario.lista_inventario,*self.lista_inventario]

    def prendi_item(self):
        return self.lista_inventario[0]