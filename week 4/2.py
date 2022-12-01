def name(username):
    count = 0
    for i in username:
        if i.isupper() == True:
            count = count + 1
    print(count)
name("hritick")
            