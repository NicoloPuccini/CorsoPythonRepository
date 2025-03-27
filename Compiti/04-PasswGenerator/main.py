# Generatore Password

import random
""""
ascii_code = 65
caracter = chr(ascii_code)
print(caracter) 
"""
#posso usare una tupla come 
ascii_num_range = (48,57)

#sorteggio il numero di caratteri della psw
dim_psw = random.randint(4,8)

#Genero le liste di caratteri  
ascii_special_c_list = [35,36,37,38,63,64]

n_psw=[]

#genero un carattere speciale casale
special_sorted = random.choice(ascii_special_c_list)
n_psw.append(special_sorted)
#genero un numero
number_sorted = random.randint(48,57)
n_psw.append(number_sorted)
#genero una maiuscola
case_sorted = random.randint(65,90)
n_psw.append(case_sorted)

for i in range(dim_psw-3):
    #genero minuscole
    small_letter_sorted = random.randint(97,122)
    n_psw.append(small_letter_sorted)

#converto da ascii in char
char_psw=[]
for i in range(len(n_psw)):
    character = chr(n_psw[i])
    char_psw.append(character)

#faccio uno shafle per gradire
random.shuffle(char_psw)

print("\n")
print(char_psw)


