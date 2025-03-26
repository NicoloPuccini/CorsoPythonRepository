"""
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
"""

fizz_count = 0
buzz_count = 0
fizzBuzz_count = 0
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
        print(ans+"\n")
        if ans=="Fizz":
            fizz_count+=1
        if ans=="Buzz":
            buzz_count+=1
        if ans=="FizzBuzz":
            fizzBuzz_count+=1
    print(f"Fizz -> {fizz_count}\nBuzz -> {buzz_count}\nFizzBuzz -> {fizzBuzz_count}\n")
    
    endProgram = input("Vuoi continuare [Y/N]")
    if endProgram.lower == 'y' or endProgram=='Y':
        break




