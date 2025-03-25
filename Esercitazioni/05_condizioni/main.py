# CONDIZIONI


# non c'è lo switch solo if else ed elif (che è if else)
num=5
if num < 10 :
    print(num)
else:
    print(num-2)

#elif

if num == 5:
    print(1)
elif num==3 :
    print(2)
else :
    print(3)

#Match case (Non si usa quasi mai) ed è simile allo switch
y = 5
match y :
    case 5:
        print(5)
    case 10:
        print(10)
    case _:     #Questo è il caso di Default in cui non si verificano tutti gli altri
        print("ne 5 ne 10")

