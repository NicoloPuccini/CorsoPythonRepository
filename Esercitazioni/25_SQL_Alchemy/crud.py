from sqlalchemy import select, insert, update, delete
from models import Cliente, Prodotto, Ordine, ordine_prodotto
from db import SessionLocal

#Cominciamo con la funzione per inserire una riga nel DB
def crea_cliente(nome:str, email: str)->Cliente:    #Stiamo imponendo i tipi di input e output della funzione
    #istanzio la sessione
    db = SessionLocal()
    cliente = Cliente(nome=nome,email=email)
    db.add(cliente)
    db.commit() #Salva le modifiche nel database
    db.refresh(cliente) #aggiorna l'oggetto cliente con i dati del database
    #chiudo la sessione
    db.close()
    return cliente
#Da notare che le istanze della classe Cliente sono le righe della tabella Cliente

def lista_prodotti() ->list[Prodotto]:  #Indica che deve ritornare una lista con elementi di tipo Prodotto
    db = SessionLocal()
    prodotti = db.query(Prodotto).all() #Fa (SELECT * FROM Prodotti)
    db.close()
    return prodotti

def lista_clienti() ->list[dict]:  #Indica che deve ritornare una lista con elementi di tipo Dizionario che conterrà i dati del cliente
    db = SessionLocal()
    all_clienti = select(Cliente)
    #creo una lista di dizionari con i dati dei clienti
    clienti = db.execute(all_clienti).scalars().all()   #scalars() serve per recuperare solo gli oggetti, altrimenti recupererebbe una lista di tuple
    result = []
    for c in clienti:
        result.append({"id":c.id,"nome":c.nome, "email":c.email})
    db.close()
    return result

def crea_ordine(cliente_id: int)->Ordine:
    db = SessionLocal()
    ordine = Ordine(cliente_id = cliente_id)
    db.add(ordine)
    db.commit()
    db.refresh(ordine)
    db.close()
    return ordine

def elimina_cliente (cliente_id: int)->None:
    db = SessionLocal()
    #Eliminiamo tutti gli ordini associati al cliente
    c = db.get(Cliente, cliente_id)
    if c:
        db.execute(
            db.delete(Ordine).where(Ordine.cliente_id == cliente_id)
        )
        db.delete(c)
        db.commit()
    db.close()
    raise ValueError("Cliente non trovato")

def aggiungi_prodotto_a_ordine(ordine_id:int, prodotto_id: int, qty:int = 1)->None:
    pass


