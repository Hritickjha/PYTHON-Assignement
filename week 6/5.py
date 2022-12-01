from string import ascii_lowercase as alpha
from random import choice, randint


def encryption(message):

    rand_num = randint(2,20)

    encrypt_letter = [choice(alpha) for count in range(rand_num)]

    suffix = "".join(encrypt_letter)

    encrypt = ''

    for i in message:
        encrypt += i + suffix

    return encrypt, rand_num

if __name__ == "__main__":
    text = "Send Cheese"

    encryption_text, spacing = encryption(text)

    print(f"'{text}' encryption is '{encryption_text}', spacing is {spacing}")