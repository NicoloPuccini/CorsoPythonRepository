while True :
    print("\n")
    num_1 = input("inserisci il primo numero\n")
    num_2 = input("inserisci il secondo numero\n")
    operation = input("che operazione vuoi fare ? digita: + - * / \n")
    if operation =='+':
        ans = num_1 + num_2
        print(ans)
    elif operation == '-':
        ans = num_1 - num_2
        print(ans)
    elif operation == '*':
        ans = num_1 * num_2
        print(ans)
    elif operation =='/':
        ans = num_1 / num_2
        if num_2 == 0:
            print("Its not possible divide by 0")
        else:
            print(ans)
    else:
        print("input are not valid\n")

    end_calc = input("end program ? [Y/N]\n")
    if end_calc.lower=='y'or end_calc.upper=='Y'or end_calc=='y':
        break