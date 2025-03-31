#SET

#UNION si può fare sia con il metodo union sia con |
set_1 = {1,2,3}
set_2 = {3,4,5}

set_unito_1 = set_1 | set_2
set_unito_2 = set_1.union(set_2)

print(f"Unito con | : {set_unito_1}")
print(f"Unito con il metodo union() :{set_unito_2}")

#Si possono anche unire piu set 
set_3 =  {"a","b"}
set_4 = {"banana", "husky"}
set_unito_3 = set_1 | set_2 | set_3 | set_4
set_unito_4 = set_1.union(set_2,set_3,set_4)

print(f"Unito con | multiplo : {set_unito_3}")
print(f"Unito con il metodo union() multiplo :{set_unito_4}")




#INTERSECTION
#Usa il metodo intersection() o l'operatore &
set_intersezione_1 = set_1 & set_2
set_intersezione_2 = set_1.intersection(set_2)
print(f"Intersection con & : {set_intersezione_1}")
print(f"Intersection con il metodo intersection() :{set_intersezione_2}")



#DIFFERENCE
#ottieni un set di elementi che sono nella prima lista ma non nella seconda 
#Si può fare con il metodo difference o con l'operatore -

set_differenza_1 = set_1 - set_2
set_differenza_2 = set_1.difference(set_2)
print(f"Difference con - : {set_differenza_1}")
print(f"Difference con il metodo difference() :{set_differenza_2}")


#UPDATE
#Permette di modificare il set (in-place) aggiungendo altri set (a differenza di union che ne crea uno nuovo)

set_1_copy = set_1.copy()
set_1.update(set_2)
print(set_1)

set_1.difference_update(set_2)   #fa la differenza in-place
print(set_1)

set_1.intersection_update(set_2) #fa l'intersezione in-place
print(set_1)





