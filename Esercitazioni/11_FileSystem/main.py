#Metodi files & directories
import os




#Creare un file
path_1 = "./test.txt"
with open(path_1,"w") as file :  #crea un file vuoto  test.txt per "w" scriverci dentro 
    pass                       #Il file viene chiuso automaticamente al termine del blocco with

    file.write("ciao")         #Scrivo una stringa nel file




#aggiungere testo al file 
with open(path_1,"a") as file :      # "a" serve per aggiungere (add)
    file.write("\ncome va ?")
    file.write("\nsto bene")       #aggiungo stringhe al file

lines = ["line1","line2","line3"]
with open(path_1,"w") as file :       #usare di nuovo "w" al posto di "a" porta a sovrascrivere il file
    for line in lines :
        file.write(line +"\n")
# Oppure sintassi piu breve 
    file.writelines(f"{line}\n" for line in lines)    #Srivi ogni stringa della lista su una nuova riga
                                                      #A differenxa di write(), writelines() vuole 
                                                      #Come parametro una lista di stringhe iterabile 


with open(path_1,"w") as file :      # "a" serve per aggiungere (add)
    pass
    #file.write(f"{line}\n" for line in lines)  
    file.writelines(f"{line}\n" for line in lines)


#leggere da file 
with open(path_1,"r") as file :
    for line in file :
        print(line.strip())

with open(path_1,"r") as file :
    content=file.read()              #read legge tutto il file e lo carica in una 
                                     #sola stringa
print(content)

#copiare un file
import shutil
path2 = "test2.txt"
shutil.copy(path_1,path2)              #Copia il file test.txt in file2.txt

os.rename(path2,"test3.txt")         #Rinomina il file in test3.txt
os.remove("test3.txt")               #Elimina il file

import datetime
timestamp = datetime.datetime.now().strftime("%Y-%M-%d-%H-%M-%S")  #Crea un file con un timestamp
path4 = f"test_{timestamp}.txt"
with open(path4,"w") as file : 
    file.write("ciao")

#Verificare se un file esiste 
if os.path.exists(path_1):
    print("file exist !")

#Ottenere informazioni da un file 
if os.path.exists(path_1):
    print(os.path.getsize(path_1))    #Ottieni la dimensione del file in byte
    print(datetime.datetime.fromtimestamp(os.path.getctime(path_1))) #Ottieni data di creazione 
    print(datetime.datetime.fromtimestamp(os.path.getmtime(path_1))) #Ottieni data di ultima modifica
    print(datetime.datetime.fromtimestamp(os.path.getatime(path_1))) #Ottieni data di ultimo accesso 


#Estrarre il nome del file senza il path
file_name = os.path.basename(path_1)

#Estrarre il nome file senza estensione
file_name_no_ext = os.path.splitext(file_name)[0]  #Nome file senza estensione
file_name_no_ext = os.path.splitext(file_name)[1]  #Estensione senza nome del file


print(file_name)

#Estrarre il path completo 
dir_path="test"
path_n = os.path.join(dir_path, "test.txt")     #Vuole come parametro il path della cartella dir_path
                                                #e il nome file test.txt

#Estrarre il path relativo
relative_path = os.path.relpath(path_1,dir_path)






#DIRECTORIES

dir_path = "test"
os.makedirs(dir_path, exist_ok=True)     #Crea una directory test se non esiste già 

#os.rmdir(dir_path)       #Elimina una cartella solamente se è vuota (Se no non compila)

shutil.rmtree(dir_path)  #Elimina la directory e tutto il contenuto

#Verificare se una directory esiste

if os.path.isdir(dir_path) :
    print("Directory exist !!")
else :
    os.makedirs(dir_path)
    print("Directory created")



#Ottenere informazioni su una directory :

if os.path.isdir(dir_path):
    print(datetime.datetime.fromtimestamp(os.path.getctime(dir_path)))  #Data di creazione della cartella 
    print(os.path.getsize(dir_path))   #Dimensioni dellla directory
    print(os.listdir(dir_path))        #Contenuto della directory (ti stampa la lista)
    print(os.path.abspath(dir_path))   #Path assoluto dellla directory

