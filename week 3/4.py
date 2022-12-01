bad_pass = ['pasword','letmein','sesame','hello','justinbiber']
passwd = str(input("enter your pass:"))
num = len(passwd)
if num > 8 and num <= 12:
    print("password verified")
else:
    print("password must be between 8 and 12 characters")
if passwd in bad_pass:
    print("password to common!")
        