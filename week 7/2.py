def at_least_one(name1="",name2=""):
    only_one = set(name1) | set(name2)
    return only_one

def on_both(name1="",name2=""):
    both = set(name1) & set(name2)
    return both

def neither_both(name1="",name2=""):
    neither = set(name1) ^ set(name2)
    return neither

if __name__ == "__main__":
    real_name = "sanju"
    nick_name = "sashin"

    print("At least one in two words ",at_least_one(real_name,nick_name))
    print("In both ",on_both(real_name,nick_name))
    print("In either word, but not in both. ",neither_both(real_name,nick_name))