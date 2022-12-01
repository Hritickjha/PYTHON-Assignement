def factorCalc(num):
    list = [i for i in range(1, num+1) if num % i == 0 ]
    return list

if __name__ == "__main__":
    value = 20
    print(f"The factor of {value} is {factorCalc(value)}")