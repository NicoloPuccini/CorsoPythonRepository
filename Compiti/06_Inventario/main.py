inventory = {}


while True:
    command = input("\nDigita :\n- add per aggiungere un  nuovo articolo\n- "
    +"quantity per aggiornare la quantità di un articolo\n"
    +"- print per stampare l'inventario\n- exit per uscire\n")

    if command == "add" or command == "Add":
        #Aggiungo un nuovo articolo
        new_article = input("Quale articolo vuoi inserire ? ")
        if new_article in inventory.keys() :
            print("Articolo già presente usa quantity")
            continue
        new_price = input("Inserisci prezzo unitario")
        new_quantity = input("In che quantità ? ")
        inventory[new_article] = {"price" : new_price, "quantity" : new_quantity }

    
    if command == "quantity" or command == "Quantity" :
        #Aggiorno la quantità di un articolo
        mod_article = input("Quale articolo vuoi modificare ? ")
        if mod_article in inventory.keys() :
            mod_quantity = input("In che quantità ? ")
            inventory[mod_article] ["quantity"] = mod_quantity
        else:
            print("Articolo non presente nell'inventario")
            continue

    if command == "print" or command == "Print" :
        #Stampo il dizionario
        print(inventory)
    
    if command == "exit" or command == "Exit" :
        break

