def primeTest(num):
    for i in range(2,num):
        if num % 2 == 0:
            result = ("is not a prime number.")
            break
    else:
        result = ("is a Prime Number.")
    return result

if __name__ == "__main__":
    value = 19
    print(f"{value} {primeTest(value)}")