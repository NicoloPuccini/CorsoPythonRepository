from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#Importo le tabelle 
from models import Base
#Import
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship

import datetime

#Creo l'engine
engine = create_engine("sqlite:///app.db", echo=False) #Dice se stamparti sul terminale i log delle operazioni che vengono fatte

#Creiamo una nuova Session
SessionLocal = sessionmaker(
    bind = engine
)
#Crea tutte le tabelle se non esistono
Base.metadata.create_all(bind=engine)
#bind è l'engine della connessione
#autoflush è per fare il flush automatico delle modifiche cioè per scrivere in memoria
#autocommit fa il commit automatico delle modifiche 
