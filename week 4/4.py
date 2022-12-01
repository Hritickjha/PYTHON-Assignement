def change():
    string = str(input("enter your string:"))
    if len(string) > 1:
        list = [i for i in string] 
        list [-1:] = []
        string_without_last_element = "".join (list)
        return string_without_last_element
    else:
        return string
print(change())  