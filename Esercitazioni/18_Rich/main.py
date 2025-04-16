from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.table import Table
from rich import box
from rich import print

#Spinner
from time import sleep
from rich.progress import Progress, SpinnerColumn,TextColumn

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

menu = """
[1] Visualizza contatti
[2] Aggiungi contatto
[3] Modifica contatto
"""
console.print(Panel(menu, title = "Menu", subtitle="Subtitle",style = "bold blue"))




#TABLE
#Stampa una tabella
table = Table(title="Titolo", box=box.SIMPLE) 
table.add_column("Nome", style="cyan")
table.add_column("Cognome", style="magenta")
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


#Spinner
with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}")) as progress :
    task = progress.add_task("[cyan]Caricamento in corso ...[/cyan]", total = None)
    sleep(2)
    progress.remove_task(task)


#Il sito ufficiale della documentazione di rich è (https://rich.readthedocs.io/en/stable)