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

        new_quantity = input("In che quantità ? ")
        inventory[new_article] = new_quantity

    
    if command == "quantity" or command == "Quantity" :
        #Aggiorno la quantità di un articolo
        new_article = input("Quale articolo vuoi modificare ? ")
        if new_article in inventory.keys() :
            new_quantity = input("In che quantità ? ")
            inventory[new_article] = new_quantity
        else:
            print("Articolo non presente nell'inventario")
            continue

    if command == "print" or command == "Print" :
        #Stampo il dizionario
        print(inventory)
    
    if command == "exit" or command == "Exit" :
        break

