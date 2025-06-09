#Permette di passare uno o piu argomenti quando si lancia il comando per eseguire il programma (ES  pip instal sqlalchemy)
# python app.py add_cliente "Andrea" andrea@filippelli.com
import argparse
from crud import (crea_cliente, elimina_cliente, elimina_ordine, crea_ordine,lista_clienti, lista_prodotti, lista_ordini, aggiungi_prodotto_a_ordine)

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

    #Genero il nuovo cmd add_ordine
    add_ordine_subp = sub.add_parser("add_ordine", help="Crea un nuovo ordine")
    add_ordine_subp.add_argument("cliente_id", help="Id del cliente")
    args = parser.parse_args()

    if args.cmd =="add_ordine":
        ordine = crea_ordine(args.cliente_id)
        print(f"Nuovo ordine creato : {ordine.id} - {ordine.cliente_id} - {ordine.data_creaz}")

    #Genero il nuovo cmd show_clienti
    show_clienti_subp = sub.add_parser("show_clienti", help="Mostra tutti i clienti")
    args = parser.parse_args()

    if args.cmd =="show_clienti":
        clienti = lista_clienti()
        print("Lista clienti : ")
        for cliente in clienti :
            print(f"id : {cliente.id}, nome : {cliente.nome}, email : {cliente.email}")

    #Genero il nuovo cmd show_prodotti
    show_prodotti_subp = sub.add_parser("show_prodotti", help="Mostra tutti i prodotti")
    args = parser.parse_args()

    if args.cmd =="show_prodotti":
        prodotti = lista_prodotti()
        print("Lista prodotti : ")
        for prodotto in prodotti :
            print(f"id : {prodotto.id}, nome : {prodotto.nome}, email : {prodotto.prezzo}")

    #Genero il nuovo cmd show_ordini
    show_ordini_subp = sub.add_parser("show_ordini", help="Mostra tutti gli ordini")
    args = parser.parse_args()

    if args.cmd =="show_ordini":
        ordini = lista_ordini()
        #ordini è una lista di dizionari
        print("Lista ordini : ")
        for ordine in ordini :
            print(f"{ordine["id"]} - {ordine["cliente id"]} - {ordine["data creazione"]}")

    #Genero il nuovo add_prodotto_a_ordine
    add_prodotto_ordine_subp = sub.add_parser("add_prodotto_a_ordine", help="Aggiungi un prodotto a ordine")
    add_prodotto_ordine_subp.add_argument("ordine_id", help="Id dell'ordine")#i_ordine_id:int, i_prodotto_id: int, qty:int = 1
    add_prodotto_ordine_subp.add_argument("prodotto_id", help="Id del prodotto")
    add_prodotto_ordine_subp.add_argument("qty", help="Quantità di prodotto")
    args = parser.parse_args()

    if args.cmd =="add_prodotto_a_ordine":
        aggiungi_prodotto_a_ordine(args.ordine_id, args.prodotto_id, args.qty)


if __name__=="__main__":
    main()