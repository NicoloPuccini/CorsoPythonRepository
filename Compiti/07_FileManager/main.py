import os
import datetime
import shutil

sorgente = input("Cartella da salvare : ")
destinazione =input("Cartella destinazione : ")

if not os.path.isdir(sorgente):   #Controlla se la sorgente esiste
    print("la sorgente non esiste")
else:
    timestamp = datetime.datetime.now().strftime("%Y-%M-%d-%H-%M-%S")
    backup_folder = os.path.join(destinazione, f"Backup_{timestamp}") #Creo un nome unico con timestamp per la cartella di backub 
                                                                      #e la metto in destinazione
    
    files_info_list = []
    os.makedirs(backup_folder,exist_ok=True)   #Creo la cartella in destinazione
    for filename in os.listdir(sorgente):
        source_file = os.path.join(sorgente, filename)
        if os.path.isfile(source_file):
            file_nome = os.path.splitext(filename)[0]
            file_extensione = os.path.splitext(filename)[1]
            file_dimensioni = os.path.getsize(source_file)
            file_data_creazione = datetime.datetime.fromtimestamp(os.path.getctime(source_file))
            file_abs_path = os.path.abspath(source_file)
            files_info_list.append((file_nome,file_extensione,file_dimensioni,file_data_creazione,file_abs_path))



            shutil.copy(source_file,backup_folder)
    print(f"Backup completo in : {backup_folder}")


    with open(os.path.join(backup_folder,"BackupReport.txt"),"w") as file :  #crea un file vuoto  test.txt per "w" scriverci dentro 
        pass                                                             #Il file viene chiuso automaticamente al termine del blocco with

        file.write("REPORT Backup:\n")
        for file_info in files_info_list:
            file.writelines(f"\nNome file : {file_info[0]}\nEstensione :"
                            f" {file_info[1]}\nDimensioni : {file_info[2]}\n"
                            f"Data di creazione : {file_info[3]}\nPath assoluto :"
                            f"{file_info[4]}\n")
            file.write("-"*80)


    ##Ma non tiene conto delle cartelle e della copia del loro contenuto 
    #Per quello dobbiamo usare funzioni ricorsive o shutil.copytree
    
