from sys import argv
list = argv[:]
list.sort(key=len)
print(list)
try:
    print(f"The shortest word is: {list[0]}")
except:
    print("word is not passed")