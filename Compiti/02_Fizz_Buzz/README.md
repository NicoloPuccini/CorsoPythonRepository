# FizzBuzz

## Consegna:

Per ogni nimero da 0 a 100 :
- Se il numero è divisibile per 3 , stampa Fizz
- Se è divisibile per 5 stampa Buzz
- Se è divisibile per entrambi stampa FizzBuzz
- Altrimenti stampa il numero 

<details>
<summary>Codice</summary>

```python 
for i in range(101):
ans = ""
if i%3==0 :
    ans = ans +"Fizz"
if i%5==0 :
    ans = ans + "Buzz"
if ans=="":
    print(i)
else:
    print(ans)
```
</details>


# Versione 2 

Come prima ma il numero su cui fare FizzBuzz viene inserito a tastiera dall'utente

<details>
<summary>Codice</summary>

```python 
num = input("inserisci un numero")
ans = ""
if i%3==0 :
    ans = ans +"Fizz"
if i%5==0 :
    ans = ans + "Buzz"
if ans=="":
    print(i)
else:
    print(ans)
```
</details>

# Versione 3

Aggingiamo un controllo sugli input e rendiamo il programma ripetibile fino a 
che non si sceglie di uscire

<details>
<summary>Codice</summary>

```python 
while True :
    print("\n")
    while True:
        num = input("inserisci un numero")
        if num.isdigit():
            num=int(num)
            break
        else:
            print("Please enter only numbers")

    ans = ""
    if num%3==0 :
        ans = ans +"Fizz"
    if num%5==0 :
        ans = ans + "Buzz"
    if ans=="":
        print(num)
    else:
        print(ans)
    
    endProgram = input("Vuoi continuare [Y/N]")
    if endProgram.lower == 'y' or endProgram=='Y':
        break
```
</details>