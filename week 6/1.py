if __name__ == '__main__':
    password = input('Enter your new password:   ')
    check = input('Re-enter the same password:')

    if password == check:
        print('Password Set')
    else:
        print('Error. Passwords do not match.')