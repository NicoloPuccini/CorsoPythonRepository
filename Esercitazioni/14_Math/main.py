#MATH

import math

#abs _ valore assoluto
num=-10
abs_num = abs(num)  #Output : 10

#Arrotondamenti
num = 10.9
c_num = math.ceil(num) #Per eccesso    Output : 11

f_num = math.floor(num) #Per difetto   Output : 10

#Round
num=10.3456
r_num = round(num)      #arrotonda all'intero piu vicino
r_num = round(num, 2)   #Il secondo parametro indica la cifra decimale a cui si 
                        #approssima 
# min & max
nums = [10,11,24,7,39,47,98,25]
max_n = max(nums)
min_n = min(nums)
print(f"max_n : {max_n}, min_n : {min_n}")

#pow-Potenza
cento = math.pow(10,2)  #Output: 100

#sqrt-Radice quadrata
dieci = math.sqrt(100)  #Output : 10 

#Costante pi greco
math.pi


