#In questo caso lo scatenarsi dall'eccezione fa uscire dal ciclo while 
try:
    while True :
        num =int(input("insert n"))
        num =int(input("insert s"))
except ValueError as e :
        print(e)
print("Sono libero !!!!!")



print("*"*80)

#In questo caso invece il ciclo while rimane intatto e l'esecuzione ripende alla
#fine del blocco TRY dentro il ciclo whil
"""
while True :
    try:
        num =int(input("insert n"))
        num =int(input("insert s"))
    except ValueError as e :
        print(e)
"""