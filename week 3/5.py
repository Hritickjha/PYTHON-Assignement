bad_pass = ['password','letmein','sesame','hello','justinbiber']
while(True):
    passwd = str (input("enter your pass: "))
    num = len(passwd)
    if passwd in bad_pass:
        print("password to common! \ntry again ")
        continue
    else:
        if num > 8 and num <= 12:
            print("password verified")
            break
        else:
            print("password must be between 8 and 12 characters! \nTry again!")
            continue    