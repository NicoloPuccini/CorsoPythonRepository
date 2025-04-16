#Rubrica telefonica (V1.0)
from datetime import datetime,timedelta
import os
import json

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.table import Table
from rich import box
from rich import print
from rich.style import Style



#OPERAZIONI INIZIALI
path_contacts = "./CorsoPythonRepository\Compiti\\11_Rubrica_Json\contatti"

#Definisco gli style che userò nella console
error_style = Style(color="red", bold=True )
submenu_title_style = Style(color = "green" , bold = True , underline = True )
menu_style = Style(color = "blue" , bold = True)

#Creo la cartella contatti se non esiste già:
os.makedirs(path_contacts , exist_ok = True)

#Mi prendo la console che userò per tutti i vari metodi di rich
console = Console()

#MENU PRINCIPALE
in_menu = 0
while  in_menu != 5 :

    while True :
        

        menu = """
1-Aggiungi un contatto\n2-Modifica un contatto\n3-Elimina \
un contatto\n4-Visualizza i contatti attivi\n5-Exit
        """

        console.print(Panel(menu, title = "* Menu *", style = "bold blue"))
        in_menu = Prompt.ask("[yellow]Digita il numero dell'operazione che desideri svolgere: [/yellow]" , choices = ["1", "2","3","4","5"] , default = "2")
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




    #Catturiamo le varie scelte dei menu :



    #AGGIUNTA DI UN CONTATTO
    if in_menu == 1 :
        console.print("\nAGGIUNGI UN CONTATTO", style = submenu_title_style)
        #Inserimento degli input
        while True :
            try :
                in_nome = Prompt.ask("[yellow]Digita il nome [/yellow]")
                if len(in_nome) < 3 :
                    raise ValueError("Error : Nome e Cognome devono avere almeno tre lettere")
                in_nome = in_nome.strip().lower().capitalize()

                break

            except ValueError as e:
                print("\n")
                console.print(Panel(f"{e}",style = error_style , title = " ! Error ! "))
                print("\n")

        while True :
            try:
                in_cognome = Prompt.ask("[yellow]Digita il cognome [/yellow]")
                if len(in_cognome) < 3 :
                    raise ValueError("Error : Nome e Cognome devono avere almeno tre lettere")
                in_cognome = in_cognome.strip().lower().capitalize()

                break

            except ValueError as e:
                print("\n")
                console.print(Panel(f"{e}",style = error_style , title = " ! Error ! "))
                print("\n")

        #Inserimento dei numeri di telefono :
        lista_numeri_telefono = []
        in_tel = True
        while in_tel :
            console.print("[yellow]Aggiungi un numero di telefono oppure continua premendo invio[/yellow]")

            in_tipo = Prompt.ask("[yellow]Digita il tipo [/yellow]")
            if in_tipo == "" :
                in_tel = False
                break

            while True :
                try:

                    in_numero_telefono = Prompt.ask("[yellow]Digita il tipo [/yellow]")
                    if in_numero_telefono == "":
                        in_tel = False
                        break
                    if not (in_numero_telefono.isdigit() and len(in_numero_telefono) == 10 )  :
                        raise ValueError("Il numero di telefono deve essere un numero di 10 cifre")
                    break
                except ValueError as e :
                    print("\n")
                    console.print(Panel(f"{e}",style = error_style , title = " ! Error ! "))
                    print("\n")

            if in_tel :
                in_telefono = {"tipo" : in_tipo , "numero" : in_numero_telefono }
                lista_numeri_telefono.append(in_telefono)
        
        #Inserimento attivo
        is_attivo = Confirm.ask("[yellow]E' attivo ?  [/yellow]")

        #Inserimento attività
        lista_attivita = []
        while True :
            in_attivita = input("Digita un'attività o enter per continuare \n")
            if in_attivita == "" :
                break
            lista_attivita.append(in_attivita)

        #Genero la data di creazione:
        data_creazione = datetime.today()
        data_creazione = data_creazione.strftime("%Y-%m-%d")

        #Metto i dati inseriti dentro la struttura dizionario:
        dizionario = {
            "nome" : in_nome,
            "cognome" : in_cognome,
            "telefono" : lista_numeri_telefono,
            "attivo" : is_attivo,
            "attivita" : lista_attivita,
            "data_di_creazione" : data_creazione
            }
        #genero il path al json
        no_space_nome = in_nome.replace(" ", "_")
        no_space_cognome = in_cognome.replace(" ","_")
        nome_json = f"{no_space_nome}_{no_space_cognome}.json"
        path_to_json = os.path.join(path_contacts , nome_json)

        with open(path_to_json,"w") as file :
            json.dump(dizionario , file , indent = 4)

        print("Utente creato con successo\n")




    #ELIMINA UN CONTATTO
    if in_menu == 3 :
        console.print("\nELIMINA UN CONTATTO", style = submenu_title_style)

        #Chiediamo in input nome e cognome del contatto da eliminare
        while True :
            try:
                in_delete_nome = input("Inserisci il nome del contatto da cancellare : ")
                if len(in_delete_nome) < 3 :
                    raise ValueError("Error : Nome e Cognome devono avere almeno tre lettere")
                in_delete_nome = in_delete_nome.strip().lower().capitalize()

                break
            except ValueError as e:
                print("\n")
                console.print(Panel(f"{e}",style = error_style , title = " ! Error ! "))
                print("\n")

        while True :
            try:
                in_delete_cognome = input("Inserisci il cognome del contatto da cancellare : ")
                if len(in_delete_cognome) < 3 :
                    raise ValueError("Error : Nome e Cognome devono avere almeno tre lettere")
                in_delete_cognome = in_delete_cognome.strip().lower().capitalize()

                break
            except ValueError as e:
                print("\n")
                console.print(Panel(f"{e}",style = error_style , title = " ! Error ! "))
                print("\n")

        #Ricostruisco il path dati nome e cognome
        no_space_nome = in_delete_nome.replace(" ", "_")
        no_space_cognome = in_delete_cognome.replace(" ","_")
        nome_json = f"{no_space_nome}_{no_space_cognome}.json"
        path_to_json = os.path.join(path_contacts , nome_json)

        #Se il  file json esiste lo cancello
        try:
            os.remove(path_to_json)
            print("Utente cancellato con successo\n")
        except FileNotFoundError as e :
            print("\n")
            console.print(Panel(f"{e}",style = error_style , title = " ! Error ! "))
            print("\n")


    #VISUALIZZA I CONTATTI ATTIVI
    if in_menu == 4 :
        console.print("\nVISUALIZZA I CONTATTI ATTIVI", style = submenu_title_style)
        list_in_contacts = os.listdir(path_contacts)
        for file in list_in_contacts :
            if os.path.splitext(file)[1] == ".json" :

                #Ricavo il path al json
                file_path = os.path.join(path_contacts , file)

                #Leggo il contenuto dei file json
                try:
                    with open (file_path , "r") as file:
                        obj = json.load(file)
                except Exception as e :
                    print("\n")
                    console.print(Panel(f"{e}",style = error_style , title = " ! Error ! "))
                    print("\n")

                #Stampo le informazioni contenute nel dizionario ottenuto leggendo il file json
                if obj :
                    if obj["attivo"] :
                        print("-"*80)
                        print(f"Nome : {obj["nome"]}\nCognome : {obj["cognome"]}\n")
                        for data_tel in obj["telefono"] :
                            print(f"\nTipo : {data_tel["tipo"]}\nNumero \
di telefono : {data_tel["numero"]}\n")

                        print("\nAttività : ")
                        for data_attivita in obj["attivita"] :
                            print(data_attivita)

                        print(f"\nData di creazione : {obj["data_di_creazione"]}")




    #MODIFICA UN CONTATTO
    if in_menu == 2 :
        console.print("\nMODIFICA UN CONTATTO", style = submenu_title_style)


        #Chiediamo in input nome e cognome del contatto da eliminare
        while True :
            try:
                to_modify_nome = input("Inserisci il nome del contatto da modificare : ")
                if len(to_modify_nome) < 3 :
                    raise ValueError("Error : Nome e Cognome devono avere almeno tre lettere")
                to_modify_nome = to_modify_nome.strip().lower().capitalize()

                break
            except ValueError as e:
                print("\n")
                console.print(Panel(f"{e}",style = error_style , title = " ! Error ! "))
                print("\n")

        while True :
            try:
                to_modify_cognome = input("Inserisci il cognome del contatto da modificare : ")
                if len(to_modify_cognome) < 3 :
                    raise ValueError("Error : Nome e Cognome devono avere almeno tre lettere")
                to_modify_cognome = to_modify_cognome.strip().lower().capitalize()

                break
            except ValueError as e:
                print("\n")
                console.print(Panel(f"{e}",style = error_style , title = " ! Error ! "))
                print("\n")

        #Ricostruisco il path dati nome e cognome
        no_space_nome = to_modify_nome.replace(" ", "_")
        no_space_cognome = to_modify_cognome.replace(" ","_")
        nome_json = f"{no_space_nome}_{no_space_cognome}.json"
        path_to_json = os.path.join(path_contacts , nome_json)
        
        #Se il  file json esiste lo modifico
        if not os.path.exists(path_to_json) :
            print("File json non trovato")
        else :
            #Se il  file json esiste lo cancello
            try:
                os.remove(path_to_json)
            except FileNotFoundError as e :
                print("\n")
                console.print(Panel(f"{e}",style = error_style , title = " ! Error ! "))
                print("\n")

            #Chiedo in input i nuovi campi da inserire 
            #copia da aggiungi contatto
            while True :
                try :
                    in_nome = input("Digita il nome : ")
                    if len(in_nome) < 3 :
                        raise ValueError("Error : Nome e Cognome devono avere almeno tre lettere")
                    in_nome = in_nome.strip().lower().capitalize()

                    break

                except ValueError as e:
                    print("\n")
                    console.print(Panel(f"{e}",style = error_style , title = " ! Error ! "))
                    print("\n")

            while True :
                try:
                    in_cognome = input("Digita il cognome : ")
                    if len(in_cognome) < 3 :
                        raise ValueError("Error : Nome e Cognome devono avere almeno tre lettere")
                    in_cognome = in_cognome.strip().lower().capitalize()

                    break

                except ValueError as e:
                    print("\n")
                    console.print(Panel(f"{e}",style = error_style , title = " ! Error ! "))
                    print("\n")

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
                        break
                    except ValueError as e :
                        print("\n")
                        console.print(Panel(f"{e}",style = error_style , title = " ! Error ! "))
                        print("\n")

                if in_tel :
                    in_telefono = {"tipo" : in_tipo , "numero" : in_numero_telefono }
                    lista_numeri_telefono.append(in_telefono)
            
            #Inserimento attivo
            is_attivo = Confirm.ask("[yellow]E' attivo ?  [/yellow]")
            
            #Inserimento attività
            lista_attivita = []
            while True :
                in_attivita = input("Digita un'attività o enter per continuare \n")
                if in_attivita == "" :
                    break
                lista_attivita.append(in_attivita)
            
            #Genero la data di creazione:
            data_creazione = datetime.today()
            data_creazione = data_creazione.strftime("%Y-%m-%d")

            #Metto i dati inseriti dentro la struttura dizionario:
            dizionario = {
                "nome" : in_nome,
                "cognome" : in_cognome,
                "telefono" : lista_numeri_telefono,
                "attivo" : is_attivo,
                "attivita" : lista_attivita,
                "data_di_creazione" : data_creazione
                }
            #genero il path al json
            no_space_nome = in_nome.replace(" ", "_")
            no_space_cognome = in_cognome.replace(" ","_")
            nome_json = f"{no_space_nome}_{no_space_cognome}.json"
            path_to_json = os.path.join(path_contacts , nome_json)

            with open(path_to_json,"w") as file :
                json.dump(dizionario , file , indent = 4)

            print("Utente modificato con successo con successo\n")


