def obfuscation(string):
    name = [i for i in string if i.isalpha()]
    name.reverse()
    encrypt = ''.join(name)
    return encrypt

if __name__ == "__main__":
    name = "test encrypt"
    print(f"'{name}' encryption is '{obfuscation(name)}'")