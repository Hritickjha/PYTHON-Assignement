userinput = int(input("Enters the number of the table you require: "))
if userinput > 0:
    count = -1
    num = -(userinput)
    while (count < 12):
        num = num + userinput
        count = count + 1
        print(count, "*", userinput, "=", num)
else:
    count = 0
    num = 12
    userinput1 = -(userinput)
    while(count < 12):
        num = num -1 
        mult = num * userinput1
        count = count + 1
        print(num, "*", userinput1, "=", mult)
