# i cicli sono :
# for
# while
#Non esistono do while , ma si possono simulare

#FOR

for i in range(11): #range genera elementi da 0 a 10
    print(i)

#For each
nomi=["nome_1","nome_2"]
for nome in nomi:
    print(nome)

#Non puoi fare cicli for con passi diversi da +1

#WHILE
j=0
while j <= 10  :
    print(f"Ciao {j}")
    j += 1


j=0
while True:
    if j>10:
        break
    j += 1

#Do While simulato
l=0
while True :
    print("ciao")
    l+=1
    if not (l>10):
        break
# continue fa ripartire il ciclo while da capo
