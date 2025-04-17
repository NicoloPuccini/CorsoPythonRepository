from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.table import Table
from rich import box
from rich import print

#Spinner
from time import sleep
from rich.progress import Progress, SpinnerColumn,TextColumn ,BarColumn, TaskProgressColumn ,TimeRemainingColumn
from rich.table import Column


#Il sito ufficiale della documentazione di rich è (https://rich.readthedocs.io/en/stable)


console = Console()

#Puoi usare l'rgb
console.print("Hello", style="#1f00f2")
console.print("Hello", style="rgb(175,0,255)")

#i o italic per l'italico
console.print("Rubrica Telefonica", style="i red")
console.print("Rubrica Telefonica", style="italic red")
#bold o b per il grassetto
console.print("Rubrica Telefonica", style="bold green")
console.print("[bold magenta]Messaggio magenta [/bold magenta]")
# Se usi print senza l'argomento style usa la vecchia versione di print 

#blink  per il lampeggiante
console.print("Rubrica Telefonica", style="blink yellow")

#s o strike per il cancellato (con la riga sopra)
console.print("Rubrica Telefonica", style="s white")
console.print("Rubrica Telefonica", style="strike white")

#u o underline per il sottolineato
console.print("Rubrica Telefonica", style="u red")
console.print("Rubrica Telefonica", style="underline red")

#Posso colorare anche il background
console.print("Rubrica Telefonica", style="red on yellow")

#r o reverse per invertire il colore del background con quello del testo 
console.print("Rubrica Telefonica", style="r purple on green")
console.print("Rubrica Telefonica", style="reverse green on purple")

#Puoi mettere i tuoi stili dentro variabili :
from rich.style import Style
danger_style = Style(color="red", blink=True, bold=True)
console.print("Danger, Will Robinson!", style=danger_style)





# PANEL
#Stampa un messaggio con un pannello
console.print(Panel("Contenuto del panel", title="Titolo" , border_style = "blue"))

#Stampa la variabile dentro il Panel
menu = """
[1] Visualizza contatti
[2] Aggiungi contatto
[3] Modifica contatto
"""
console.print(Panel(menu, title = "[red]Menu", subtitle="Subtitle",style = "bold blue"))

# expand=False impedisce che il panel si allarghi a tutto il terminale ma si aggiusti sul contenuto 
console.print(Panel("Contenuto del panel", title="[red]Titolo" , border_style = "blue", expand=False))
# oppure si può usare il metodo fit 
print(Panel.fit("Hello, [red]World!"))

#border style e  padding
print(Panel("Hello, [red]World!", border_style= "yellow" ,padding=15 , expand=False , title="[green]Io sto a destra" , title_align= "right")) #il padding è verticale



#TABLE
#Stampa una tabella

#default : box.HEAVY
table = Table(title="Titolo")
table.add_column("Nome", style="cyan")
table.add_column("Cognome", style="magenta")
table.add_row("nome","cognome","1256395")
table.add_row("nome","cognome","1256395")
console.print(table)

#box.SIMPLE
table = Table(title="Titolo", box=box.SIMPLE) 
table.add_column("Nome", style="cyan")
table.add_column("Cognome", style="magenta")
table.add_row("nome","cognome","1256395")
table.add_row("nome","cognome","1256395")
console.print(table)

#box.HEAVY
table = Table(title="Titolo", box=box.HEAVY) 
table.add_column("Nome", style="cyan")
table.add_column("Cognome", style="magenta")
table.add_row("nome","cognome","1256395")
table.add_row("nome","cognome","1256395")
console.print(table)

#pulisce la console 
# console.clear() 

#PROMPT
#Stampa di un prompt 
#Ti permette di chiedere input e ti gestisce anche la parte di controlli
nome = Prompt.ask("[cyan]Nome[/cyan]")

#choices limita l'imput a delle opzioni predeterminate
#Il default è il caso che viene usato se l'utenta preme solo invio
genere = Prompt.ask("[yellow][/yellow]" , choices = ["maschio", "femmina"] , default = "maschio")

#Scelta binaria , ritorna un bool
m18 = Confirm.ask("[red]Sei maggiore di 18 anni ?[/red]")     # Aggiungi import : from rich.prompt import Prompt, Confirm

print(f"Accesso {"consentito" if m18 else "negato"}")






#SPINNERS
#Spinner
from time import sleep
from rich.progress import Progress, SpinnerColumn,TextColumn ,BarColumn, TaskProgressColumn ,TimeRemainingColumn
from rich.table import Column

print("SPINNERS :")
#Un oggetto progres ti permette di visualizzare delle animazioni continue in un lasso di tempo
#SpinnerColumn : ti permette di mettere uno spinner per far vedere che qualcosa sta macinando
#TextColumn : Ti fa aggiungere un testo
#BarColumn : Ti permette di inserire una barra di progressione 

with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}")) as progress :
    task = progress.add_task("[cyan]Caricamento in corso ...[/cyan]", total = None)
    sleep(2)
    progress.remove_task(task)

#Di spinner così con le immaginette ne esistono tanti :
#Stili di spinners che puoi provare : line dots2 bouncingBar monkey earth aesthetic weather
with Progress(SpinnerColumn(spinner_name="line"), TextColumn("[progress.description]{task.description}")) as progress :
    task = progress.add_task("[cyan]Caricamento in corso ...[/cyan]", total = None)
    sleep(2)
    progress.remove_task(task)

with Progress(SpinnerColumn(spinner_name="dots2"), TextColumn("[progress.description]{task.description}")) as progress :
    task = progress.add_task("[cyan]Caricamento in corso ...[/cyan]", total = None)
    sleep(2)
    progress.remove_task(task)
with Progress(SpinnerColumn(spinner_name="monkey"), TextColumn("[progress.description]{task.description}")) as progress :
    task = progress.add_task("[cyan]Caricamento in corso ...[/cyan]", total = None)
    sleep(2)
    progress.remove_task(task)




#Barre di caricamento
with Progress() as progress:
    #il metodo add task aggiunge una barra che si carica in relazione al metodo update
    task1 = progress.add_task("[red]Downloading...", total=1000)
    task2 = progress.add_task("[green]Processing...", total=1000)
    task3 = progress.add_task("[cyan]Cooking...", total=1000)

    while not progress.finished:
        progress.update(task1, advance=4)
        progress.update(task2, advance=5)
        progress.update(task3, advance=10)
        sleep(0.02)

#Columns
text_column = TextColumn("{task.description}", table_column=Column(ratio=1))       #per la colonna di testo
bar_column = BarColumn(bar_width=None, table_column=Column(ratio=2))     #Per la barra di progresso
progress = Progress(text_column, bar_column, expand=False) #Creo l'oggetto Progress(con le colonne come parametri)

with progress:
    for n in progress.track(range(100)):
        progress.print(n)
        sleep(0.1)


#Barra di progresso per quando leggi da json
import json
import rich.progress
"""
with rich.progress.open("data.json", "rb") as file:
    data = json.load(file)
print(data)
"""
print("\n\n")






#TREES
#Richiede di importare:
from rich.tree import Tree

tree = Tree("Creato")
print(tree)

plant_tree = tree.add("Piante", style="bold green")  #Per muovermi sui livelli basta inizializzare variabili 
                                                     #con dentro i sottoalberi 
animal_tree = tree.add("Animali",style="bold red")

plant_tree.add("Conifere")
alghe_tree = plant_tree.add("Alghe")
alghe_tree.add("Combu")
alghe_tree.add("Poseidonia")

#Creo il primo livello di Animal
mamal_tree = animal_tree.add("Mammiferi")
animal_tree.add("Rettili")
animal_tree.add("Pesci")
animal_tree.add("Anfibi")

#Posso anche fare add dietro add  ecc ecc in tal caso creo un percorso 
animal_tree.add("Uccelli").add("Corvidi").add("Corvo", style="black on white")

#terzo livello 
mamal_tree.add("Canidi")
mamal_tree.add("Felini")
mamal_tree.add("Cetacei")
print(tree)

