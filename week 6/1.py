def convertToBinary(num):
    bit = []
    while num != 0:
        remd = num % 2
        bit.append(remd)
        num = num // 2
    bit.reverse()
    return bit

if __name__ == "__main__":
    value = 17
    print(f"The binary of {value} is {convertToBinary(value)}")