#Permette di passare uno o piu argomenti quando si lancia il comando per eseguire il programma (ES  pip instal sqlalchemy)
# python app.py add_cliente "Andrea" andrea@filippelli.com
import argparse
from crud import (crea_cliente, elimina_cliente,crea_ordine,lista_clienti,lista_prodotti)

#Lo scopo del metodo di lavoro argparse è quello di creare dei comandi che contengono gli argomenti da passare ai parametri delle funzioni
def main ():
    parser = argparse.ArgumentParser(description="App Crud SQLAlchemy") #Crea il parser ciè l'oggetto che gestisce gli argomenti dati da linea di comando
    sub = parser.add_subparsers(dest="cmd",required=True)#Crea i sottocomandi sub cioè i comandi che partono da app.py

    #add_cliente -> python app.py add_Cliente "Cliente 1" cliente@dominio.com
    p= sub.add_parser("add_cliente", help="Crea un nuovo cliente") #crea il parser per il comando add_cliente
    p.add_argument("nome", help="Nome del cliente")#Aggiunge l'argomento nome
    p.add_argument("email", help= "Email del cliente")#Aggiunge l'argomento email
    args = parser.parse_args()

    if args.cmd == "add_cliente":
        cliente = crea_cliente(args.nome, args.email)
        print(f"Nuovo cliente :{cliente.id} - {cliente.nome} - {cliente.email}")

if __name__=="__main__":
    main()