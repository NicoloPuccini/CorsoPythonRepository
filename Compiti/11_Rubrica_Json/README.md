# Rubrica JSON

I contatti sono salvati in file json separati e conservati in una cartella contatti , ogni file si chiamerà nome_cognome
conterrà le seguenti informazioni :

```json
{
    "nome" : "nome",
    "cognome" : "cognome",
    "telefono" :
    [
        {
            "tipo" : "cellulare",
            "numero": "12345678"
        }
    ],

    "attivo" : true,
    "attività" : ["programmazione", "customer care"],
    "data_di_creazione" : "2025-01-01"
}

```

Devi poter :
- Aggiungere un contatto 
- Modificare un contatto
- Eliminare un contatto 
- Visualizzare i contatti attivi 

Inoltre :
- Gestisci gli errori comuni con try except 
- Scrivi un README completo


