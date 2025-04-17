#Calcolatrice con le funzioni 

def calcolatrice (num1, num2, operazione):
    try:
        if not (type(num1) == int) and (type(num2) == int) :
            raise ValueError("Input errato")

        if operation =='+':
            ans = num_1 + num_2
            return(ans)
        elif operation == '-':
            ans = num_1 - num_2
            return(ans)
        elif operation == '*':
            ans = num_1 * num_2
            return(ans)
        elif operation =='/':
            ans = num_1 / num_2
            if num_2 == 0:
                raise ValueError("Its not possible divide by 0\n")
            else:
                return(ans)
        else:
            raise ValueError("Operation must be + - * / \n")
    except ValueError as e :
        return e




while True :
    print("\n")
    try:
        num_1 = int(input("inserisci il primo numero\n"))
        num_2 = int(input("inserisci il secondo numero\n"))
    except ValueError as e :
        print(e)
        continue

    operation = input("che operazione vuoi fare ? digita: + - * / \n")

    ans = calcolatrice(num_1,num_2,operation)
    if type(ans)== str:
        print(ans)
    else:
        print(f"Il risultato è : {ans}")

    end_calc = input("end program ? [Y/N]\n")
    if end_calc.lower=='y'or end_calc.upper=='Y'or end_calc=='y':
        break