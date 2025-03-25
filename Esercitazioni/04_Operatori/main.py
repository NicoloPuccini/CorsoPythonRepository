# OPERATORI
# OPERATORI ARITMETICI

a = 10
b = 20
c = a + b

#modulo (resto della divisione)
resto = 10 % 3
print(resto)

#OPERATORI DI CONFRONTO

numero_e = 10
numero_f = 20
confronto = numero_e == numero_f # CONFRONTO darà false perchè sono numeri diversi
confronto = numero_e != numero_f # DIVERSO in questo caso confronto darà true

# OPERATORI LOGICI

#(and , or not )
con_1 = True
con_2 = False
ris_and = con_1 and con_2
ris_or = con_1 or con_2
ris_not = not con_1

#OPERATORI DI ASSEGNAZIONE

num = 10

num += 5
#Equivale a :
num = num + 5
# vale anche per le altre operazioni

#non ci sono gli operatori incremento e decremento ++ --
#ma puoi simularlo così:
num += 1

#concatenazione + lo si può evitare, è piu comodo usare l'interpolazione
#esempio interpolazione
string_1 = f"io sono{num}"
print(string_1)

