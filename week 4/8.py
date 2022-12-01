from statistics import mean

def maths():
    list = []
    while(True):
        user_input = str(input("Enter numbers or press enter to end: "))
        list.append(user_input)
        if user_input == "":
            break
        else:
            continue
    list[-1:] = []
    new_list = [int(i) for i in list]

    max_value = max(new_list)
    min_value = min(new_list)
    mean_value = mean(new_list)
    print("The max Value is", max_value)
    print("The min Value is", min_value)
    print("The mean Value is", mean_value)
    return None

maths()