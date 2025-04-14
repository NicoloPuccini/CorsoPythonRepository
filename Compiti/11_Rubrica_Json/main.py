#Rubrica telefonica (V1.0)
from datetime import datetime,timedelta
import os
import shutil
import ast

#OPERAZIONI INIZIALI
path_contacts = "./CorsoPythonRepository\Compiti\\11_Rubrica_Json\contatti"

#Creo la cartella contatti se non esiste già:
os.makedirs(path_contacts , exist_ok = True)

#MENU PRINCIPALE
in_menu = 0
while  in_menu != 5 :

    while True :
        try:
            in_menu = input("\nMENU : \n1-Aggiungi un contatto\n2-Modifica un contatto\n3-Elimina \
un contatto\n4-Visualizza i contatti attivi\n5-Exit\n")
            if not in_menu.isdigit():
                raise ValueError("in menu must be digit (1,2,3,4,5)")
            in_menu = int(in_menu)
            if in_menu == 1:
                # Aggiungi un contatto 
                break
            if in_menu == 2:
                # Modifica un contatto
                break
            if in_menu == 3:
                #Elimina un contatto
                break
            if in_menu == 4:
                #Visualizza i contatti attivi
                break
            if in_menu == 5:
                #Exit
                break
            raise ValueError("in menu must be digit (1,2,3,4,5)")
        except ValueError as e :
            print("*"*40 + "\nError : ")
            print(e)
            print("*"*40)


    #Catturiamo le varie scelte dei menu :

    #AGGIUNTA DI UN CONTATTO
    if in_menu == 1 :
        print("-"*80)
        print("\nAggiungi Contatto\n")

        #Inserimento degli input
        while True :
            try :
                in_nome = input("Digita il nome : ")
                if len(in_nome) < 3 :
                    raise ValueError("Error : Nome e Cognome devono avere almeno tre lettere")
                in_nome = in_nome.strip().capitalize()

                break

            except ValueError as e:
                print("*"*40)
                print (e)
                print("*"*40)

        while True :
            try:
                in_cognome = input("Digita il cognome : ")
                if len(in_cognome) < 3 :
                    raise ValueError("Error : Nome e Cognome devono avere almeno tre lettere")
                in_cognome = in_cognome.strip().capitalize()

                break

            except ValueError as e:
                print("*"*40)
                print (e)
                print("*"*40)

        #Inserimento dei numeri di telefono :
        lista_numeri_telefono = []
        in_tel = True
        while in_tel :
            print("Aggiungi un numero di telefono oppure continua premendo invio")

            in_tipo = input("Digita il tipo : ")
            if in_tipo == "" :
                in_tel = False
                break

            while True :
                try:

                    in_numero_telefono = input("Digita il numero : ")
                    if in_numero_telefono == "":
                        in_tel = False
                        break
                    if not (in_numero_telefono.isdigit() and len(in_numero_telefono) == 10 )  :
                        raise ValueError("Il numero di telefono deve essere un numero di 10 cifre")
                except ValueError as e :
                    print("*"*40)
                    print (e)
                    print("*"*40)

            if in_tel :
                in_telefono = {"tipo" : in_tipo , "numero" : in_numero_telefono }
                lista_numeri_telefono.append(in_telefono)
        
        #Inserimento attivo
        while True :
            try:
                is_attivo = input("E' attivo ? [Y/N] ")
                if is_attivo.strip().lower() == "y":
                    attivo = True
                    break
                if is_attivo.strip().lower() == "n":
                    attivo = False
                    break
                raise ValueError("Digit only Y or N ")
            except ValueError as e :
                print("*"*40)
                print (e)
                print("*"*40)
                
        #Inserimento attività

        





