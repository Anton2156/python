import re

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ERROR_DIR = Path(__file__).resolve().parent



def main():
    user_list = []

    while True:
        phone = get_phone()
        email = get_email()
        password = get_password()

        user_list.append([phone, email, password])
        save_data(phone, email, password)

        print(
            f"\nПоздравляем с успешной регистрацией!"
            f"\nВаш номер телефона: +{phone}"
            f"\nВаш email: {email}"
            f'\nВаш пароль: {"*"*len(password)}'
        )

        if input("Continue? (Y/n)") == "n":
            break


def save_data(phone, email, password):
    with open(BASE_DIR / "users.txt", "a") as f:
        # print(f"{phone} {email} {password}", file=f)
        print(
f"Phone: {phone}\n\
Email: {email}\n\
Password: {password}",file = f
            )

def save_error(Error):
    with open(ERROR_DIR / "Error.txt", "a") as f:
        f.write(F"incorrect input:{Error}\n")
        

def get_phone():
    phone = input("Введите номер телефона: ")
    phone = re.sub(r"\D", "", phone)
    if len(phone) > 8:
        return "380" + phone[-9:]
    else:
        save_error(phone)
        return get_phone()

def get_email():
    email = input("Введите email: ")
    if len(email) < 6 or email.count("@") != 1 or email.startswith("@"):
        print("Неверный формат. Повторите ввод.")
        save_error(email)
        return get_email()
    return email

def get_password():
    password = input("Введите пароль: ")
    if len(password) < 8 or re.findall(r"\s", password):
        save_error(password)
        print("Пароль слишком простой. Придумайте более надежный пароль.")
        return get_password()

    u_counter = l_counter = d_counter = s_counter = 0
    for i in password:
        if i.isupper():
            u_counter += 1
        elif i.islower():
            l_counter += 1
        elif i.isdigit():
            d_counter += 1
        else:
            s_counter += 1

    if min(u_counter, l_counter, d_counter, s_counter) == 0:
        save_error(password)
        print("Пароль слишком простой. Придумайте более надежный пароль.")
        return get_password()

    if input("Повторите пароль: ") != password:
        print("Пароли не совпадают.")
        return get_password()
    return password


if __name__ == "__main__":
    main()