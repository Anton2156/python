import random

from string import ascii_lowercase, ascii_letters, digits, punctuation
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def main():
    choice = input(
        "1. Сгенерировать простой пароль\n"
        "2. Сгенерировать средний пароль\n"
        "3. Сгенерировать сложный пароль\n"
        "4. Закончть"
    )
    if choice == "1":
        password = gen_password("12")
    elif choice == "2":
        password = gen_password(ascii_letters + digits)
    elif choice == "3":
        password = gen_strong_pw()
    else:
        password = "End"
        print("Buy")
    if password != "End":
        print("Pass=",password)
        check_pass(password)


def gen_password(chars, length=3):
    password = ""
    for i in range(length):
        password += random.choice(chars)
    return password

def gen_strong_pw():
    length = random.randint(8, 16)
    password = gen_password(digits + ascii_letters + punctuation, length)

    counter_d = counter_u = counter_l = counter_s = 0
    for char in password:
        if char.isdigit():
            counter_d += 1
        elif char.isupper():
            counter_u += 1
        elif char.islower():
            counter_l += 1
        elif not char.isspace():
            counter_s += 1

    if counter_d and counter_u and counter_l and counter_s:
        return password
    return gen_strong_pw()

def save_pass(password):
    file_path = BASE_DIR / "users2.txt"
    with open(file_path,"a") as f:
        f.write(f"{password}\n")
    return main()

def check_pass(password):
    print("---------------------------------------")
    file_path = BASE_DIR / "users2.txt"
    with open(file_path, "r") as f:
        read = f.read()
        read = read.split("\n")
        a = 0
        for i in read:
            if i == password:
                a = 1
    if a == 1:
        print(f"The password is repeated:{password}\nTry again")
        return main()
    else:
        return save_pass(password)
    # end = input("Continue:?(y/n)")
    print("---------------------------------------")












if __name__ == "__main__":
    main()