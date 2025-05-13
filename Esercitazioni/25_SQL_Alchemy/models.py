#Import
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Table
from sqlalchemy.orm import declarative_base, relationship
import datetime

#Le tabelle possono essere di due tipi :
#-Anagrafiche (Contengono i dati)
#-Azione (Prendono i record da altre tabelle e fungono da collegamento per mettere in relazione piu tabelle)

#ES:
# Prodotto, Cliente sono Anagrafiche
# Ordine è una tabella Azione
#Devo fare un altra table per per collegare le ordine e prodotto essendo una relazione molti a molti
#Di solito si chiamano con i nomi delle tabelle che collega:
Base = declarative_base()

ordine_prodotto = Table(
    "ordine_prodotto", Base.metadata, 
    Column("ordine_id",Integer, ForeignKey("ordini.id"),primary_key=True),
    Column("prodotto_id",Integer,ForeignKey("prodotti.id"),primary_key=True),
    Column("quantita",Integer,default=1)
)

class Cliente(Base):
    __tablename__= "clienti" #Indica il nome della tabella nel database
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)   #Nullable specifica se sono accettati valori vuoti , False rende il campo mandatory
    email = Column(String, unique=True, nullable=False) #Unique fa si che non possano esistere duplicati su questa tabella 
    #Creo una relazione con la tabella Ordine
    ordini = relationship("Ordine", back_populates="cliente")   #Relazione uno a molti con ordini 

#Creo la tabella prodotto:
class Prodotto(Base):
    __tablename__="prodotti"
    id = Column(Integer,primary_key=True)
    nome = Column(String, nullable=False)
    prezzo = Column(Float, nullable= False)

class Ordine(Base):
    __tablename__="ordini"
    id = Column(Integer,primary_key=True)
    cliente_id = Column(Integer, ForeignKey("clienti.id"),nullable=False)
    data_creaz = Column(DateTime, default= datetime.datetime.now)
    cliente = relationship("Cliente", back_populates="ordini")  #Relazione molti a uno con Cliente
    #back_populates serve per definire la relazione da ordine a cliente
    prodotti = relationship("Prodotto", secondary= ordine_prodotto, backref="ordini" )

