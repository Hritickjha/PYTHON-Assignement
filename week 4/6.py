def conversion():
    userinput = str(input("enter temp:"))
    if "c" in userinput or "c" in userinput:
        list = [userinput]
        seprated_list[-1:] = []
        joined_list = "".join(seprated_list)
        temp = float(joined_list)
        f = (temp*1.8) + 32
        result = (f"{temp}c is equivalent to {f}F")
        return result
    else:
        result = "something went wrong !"
        return result
    
print(conversion())
               