import os
import datetime
import shutil


# FILE MANAGER V(3.0)
#Ordina i file in cartelle in base all'estensione

sorgente = input("Cartella di origine :")

if not os.path.isdir(sorgente):   #Controlla se la sorgente esiste
    print("la sorgente non esiste")
else:
    #faccio una lista nei file nella directory sorgente(Ignoro le directory)
    file_list = []
    ext_list =[]
    for elem in  os.listdir(sorgente):
        elem_path = os.path.join(sorgente, elem)
        if os.path.isfile(elem_path):
            file_list.append(elem)
            ext_list.append(os.path.splitext(elem)[1].replace(".",""))
            print(ext_list)


    for ext in ext_list :
        print(ext)
        path_new_dir = os.path.join(sorgente,ext)
        os.makedirs(path_new_dir, exist_ok=True)
    
    for file in file_list :
        
        destination_dir = os.path.splitext(file)[1].replace(".","")
        destination_dir_path = os.path.join(sorgente,destination_dir)
        file_path = os.path.join(sorgente,file) 
        shutil.move(file_path, destination_dir_path)
        #shutil.move(file_path, "test/chiocciola.txt")      
    

   