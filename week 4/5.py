def c_to_f(temp):
    temp = float(temp)
    f = (temp * 1.8) + 32
    result = (f"{temp}c is equivalent to {f}F")
    return result

def f_to_c(temp):
    temp = float(temp)
    c = (temp-32)/1.8
    result = (f"{temp}F is equivalent to {c}c")
    return result

print(c_to_F(30))
print(f_to_c(86))
   