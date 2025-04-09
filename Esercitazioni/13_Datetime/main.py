#DATE

from datetime import datetime,timedelta

#Creare una data specifica 
birth_date= datetime(1990,1,1)
print(f"Sei nato il {birth_date.strftime('%d%M%Y')}")   #Stampa la data di nascita formattata


#Ottieni la data di oggi 
today = datetime.today()
print(f"Oggi è : {today.strftime("%d%M%Y %H:%M:%S")}")

#Calcoli con le date

age_days = (today - birth_date).days
print(f"Hai la bellezza di {age_days} giorni")

#Giorni mancanti ad una data 
next_year = datetime(today.year +1,1,1)
missing_days_to_new_year = (next_year - today).days

# Sommare settimane , sommare mesi
next_week = today + timedelta(weeks = 1 ) #aggiungo una settimana
print(f"Mancano{next_week - today}")

next_month = today + timedelta(days = 60) #aggiungo 2 mesi alla data

#Conversione stringa data 
date = datetime.strptime("2024-12-31","%Y-%m-%d")  #strptime converte una stringa in una data

#Conversione data in stringa 
date_string = date.strftime("%d/%m/%Y") 

type(date_string)   #Ritorna il tipo della variabile 



#FORMATTAZIONE

#Conversione stringa data 
date = datetime.strptime("2024-12-31","%Y-%m-%d")   # %d giorni in numero , %m sono i mesi in numero
date = birth_date.strftime('%A%B%Y')   # %A indica il giorno in forma estesa 
                                                    # %B indica il mese in forma estesa
print(date)

#estraggo il giorno della settimana da una data 
week_day = birth_date.weekday()

#estraggo il giorno dell'anno
day_year = birth_date.timetuple().tm_yday  # tm_yday indica il campo anno della struct_time
print(day_year)