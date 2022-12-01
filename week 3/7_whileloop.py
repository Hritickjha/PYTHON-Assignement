count = -1
userinput = int(input ("enter the number of the table you require: "))
num = -(userinput) 
while(count < 12):
    num = num + userinput
    count = count + 1
    print(count,"*",userinput,"=",num)
