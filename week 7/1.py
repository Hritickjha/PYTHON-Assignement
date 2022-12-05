def split_string(name):
    new = set(i for i in name)
    unique_list = list(new)
    return sorted(unique_list)

if __name__ == "__main__":
    word = "sdfhgsyugukhda"

    print("The unique list is:",split_string(word))