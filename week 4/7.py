from statistics import mean

def maths(a,b,c,d,e,f):
    list = [a,b,c,d,e,f]
    max_value = max(list)
    min_value = min(list)
    mean_value = mean(list)
    print("The max Value is", max_value)
    print("The min Value is", min_value)
    print("The mean Value is", mean_value)
    return None

maths(1,2,3,4,5,6)