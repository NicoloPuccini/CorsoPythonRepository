from sqlalchemy import select, insert, update, delete
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
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

def crea_ordine(cliente_id: int)->Ordine:
    db = SessionLocal()
    ordine = Ordine(cliente_id = cliente_id)
    db.add(ordine)
    db.commit()
    db.refresh(ordine)
    db.close()
    return ordine

def lista_prodotti() ->list[Prodotto]:  #Indica che deve ritornare una lista con elementi di tipo Prodotto
    db = SessionLocal()
    prodotti = db.query(Prodotto).all() #Fa (SELECT * FROM Prodotti)
    db.close()
    return prodotti

def lista_clienti() ->list[dict]:  #Indica che deve ritornare una lista con elementi di tipo Dizionario che conterrà i dati del cliente
    db = SessionLocal()
    all_clienti = select(Cliente)
    #creo una lista di dizionari con i dati dei clienti
    clienti = db.execute(all_clienti).scalars().all()   #scalars() serve per recuperare gli oggetti, altrimenti recupererebbe una lista di tuple con le variabili come elementi
    result = []
    for c in clienti:
        result.append({"id":c.id,"nome":c.nome, "email":c.email})
    db.close()
    return result

def lista_ordini() ->list[dict]:
    db = SessionLocal()
    all_ordini = select(Ordine)
    ordini = db.execute(all_ordini).scalars().all() #Il metodo execute permette di scrivere ed eseguire una query
                                                    #Il metodo scalars() è uno spacchettatore , serve a recuperare gli oggetti risultanti da una query 
                                                    #e renderli iterabili
                                                    #Il metodo all() recupera tutti i risultati della Query e li mette in una lista 
    result = []
    #Ora ordini è una lista di istanze di Ordine
    for ordine in ordini:
        result.append({"id": ordine.id,"cliente id": ordine.cliente_id,"data creazione" :ordine.data_creaz })
    db.close()
    return result

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
    else:
        raise ValueError("Cliente non trovato")
    db.close()
    

def elimina_ordine(ordine_id : int)->None:
    db = SessionLocal()
    #Elimino l'ordine in base all'id
    c = db.get(Ordine, ordine_id)   #Il metodo get di SessionLocal si usa per 
                                    #recuperare oggetti dal DB tramite la chiave la chiave primaria
    
    if c:
        db.delete(Ordine).where(Ordine.id == ordine_id)
        db.commit()
    else:
        raise ValueError("Ordine non trovato")
    db.close()

def aggiungi_prodotto_a_ordine(i_ordine_id:int, i_prodotto_id: int, qty:int = 1)->None:
    try:
        db = SessionLocal()
        stmt = insert(ordine_prodotto).values(ordine_id= i_ordine_id, prodotto_id= i_prodotto_id, quantita = qty)
        db.execute(stmt)
        db.commit()
        db.close()
        print("Prodotto aggiunto ad ordine")
    except IntegrityError as e :
        print("""
              Errore : Gli input non rispettano i vincoli del db,
               chiave primaria duplicata o foreign key non trovata
              """)
    except SQLAlchemyError as e :
        print("Errore : generico SQAlchemy")
    except Exception as e :
        print("Error : Errore generico (riprova)")


