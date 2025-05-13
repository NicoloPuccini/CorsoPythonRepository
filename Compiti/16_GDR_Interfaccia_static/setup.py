from setuptools import setup, find_packages #Importa le funzioni necessarie
#setuptools è il gestore di paccheti di python
#setup è il modulo che gestisce le funzionalità di importazione
setup (
    name = "gioco_torneo", #nome del pacchetto (Usa nomi brevi)
    version = "0.1.0",   #Indica la versione del progetto , per ora iniziale
    description = "Gioco di combattimento a turni",
    author = "Il tuo nome",
    packages = find_packages(),     #Cerca tutte le cartelle con __init__.py
    install_requires = [],  #Dipendenze esterne (vuoto ,usiamo solo Python base)
    python_requires=">=3.8",    #Versione minima consigliata di Python
    classifiers=["Programming Language :: Python :: 3", "Operating System :: OS Indipendent"],
)