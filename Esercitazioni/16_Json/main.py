import json

#Il file json è un file di testo , non è compilato ma è serializzato
#ATTENZIONE : Non usare caratteri speciali nelle chiavi di un file JSON

#Spesso i siti internet forniscono Endpoint che tramite JSON forniscono servizi
#Dai metereologi alle risposte di chatGPT

path = "./CorsoPythonRepository\Esercitazioni\\16_Json\\test.json"  #Prendiamo l'abitudine di mettere i file nella stessa directory



#LETTURA di un file Json

with open (path, "r") as file:
#Deserializza il file json (leva virgole e parentesi)
    obj = json.load(file)


print(f"obj è di tipo : {type(obj)}")

#Ora posso accedere ai dati di obj come se fosse un dizionario
print(f"Nome : {obj["nome"]}\nCognome : {obj["cognome"]}\nEtà : {obj["eta"]}")

#I json possono anche assumere strutture dati pi complesse, dizionari di dizionari .... ecc
print(f"Indirizzo : {obj["indirizzo"]["via"]} {obj["indirizzo"]["citta"]}")
#Posso usare anche le liste, per accedervi però dovrò usare gli indici
print(f"Numero di telefono : {obj["num_tel"][0]["num"]}")

#Aggiungo un numero di telefono ad obj
obj["num_tel"].append({"tipo":"cellulare", "numero": "12345678" })


#Se provo a leggere un file vuoto load darà errore bloccante , vuole almeno le quadre, posso usare 
# if os.path.getsize(file_path) > 0:
#    print("Il file NON è vuoto.")
#Per controllare 
#oppure:
with open (path, "r") as file:
    try:
#Deserializza il file json (leva virgole e parentesi)
        obj = json.load(file)
    except Exception as e:
        print(e)


#Leggo da una lista di oggetti Json
path_2 = "./CorsoPythonRepository\Esercitazioni\\16_Json\\test2.json"
with open(path_2, "r") as file:
    obj_2 = json.load(file)
for elemento in obj_2 :
    print(elemento)







#SCRITTURA di un file Json
with open(path , "w") as file :
    #Il metodo dump permette di scrivere sul Json,
    #Il primo parametro è l'oggetto  che verrà scritto
    #Il secondo parametro è il file in cui si scrive
    # il terzo parametro (opzionale) fornisce indicazioni sull'identazione del file
    json.dump(obj , file , indent = 4)

#Se provo a usare remove su un elemento che non esiste ottengo un Value error che va gestito (Try except)
try:
    obj["lingue_parlate"].remove("polacco")
except ValueError as e :
    print(e)

#Non ho messo la scrittura del file dentro il blocco try perchè è sempre meglio mettere dentro il blocco try solo le singole 
#righe che possono generare errore in modo da gestirle puntualmente
with open(path , "w") as file :
        json.dump(obj , file , indent = 4)

#Modifico un campo
obj["nome"] = "nome2"
with open(path , "w") as file:
     json.dump(obj,file,indent = 4 )






