num = int(input("enters the number of the table you require:"))
if num > 0:
    for i in range (0,13):
        mult = i * num
        print(i,"*", num,"=",mult)
else:
    num1 = -num
    for i in range (13,-1,-1):
        mult = i * num1
        print(i,"*",num1,"=",mult)
        