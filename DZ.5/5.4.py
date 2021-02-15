import re
import string
import random

def main():
    phone_finished = the_phone_number()

    email_finished = the_email()

    pass_finished = the_pass()

    the_checking(phone_finished,email_finished,pass_finished)

def the_phone_number():
    print("==Phone==")
    phone = input('Enter phone number: ')
    your_phone = ""
    count_d = ""
    for char in phone:
        if char.isdigit():
            count_d += char
    if (len(count_d) == 10 and count_d[:1] == "0"):
        your_phone = "38"+ count_d
        return
    elif (len(count_d) == 12 and count_d[:3] == "380"):
        your_phone = count_d
    else:
        print("Wrong number\nTry again")
        the_phone_number()
    return your_phone

def the_email():
    print("==Email==\nSymbol available: '.' or '_' or '-'")
    login = input('Enter login(without a domain):')
    login = login + "@"
    email = input(f"Enter domain:{login}")
    email = login + email
    for i in email:
        if i == " ":
            print("\nWrong format\nTry again\n")
            the_email()
        if i == "@" or i == "_" or i == "-" or i == ".":
            i = " "
        else:
            for j in string.punctuation:
                if i == j:
                    print("\nSymbol not available\nTry again\n")
                    the_email()
    if email[0] == "." or email[0] == "-" or email[0] == "_" or email[0] == "@":
        print("The word doesn't begin with a letter\nTry again\n")
        the_email()

    if len(email) <= 6:
        print("Must be more than 6 characters\nTry again")
        the_email()
    return(email)

def the_pass():
    print("==Pass==")
    your_pass = input("Enter the password:")
    if len(your_pass) < 8:
        print("Must be more than 8 characters\nTry again")
        the_pass()
    lower,upper,digit,symbol = 0,0,0,0
    for j in your_pass:
        if j.islower() == True:
            lower += 1
        elif j.isupper() == True:
            upper += 1
        elif j.isdigit() == True:
            digit += 1
        else:
            symbol += 1
    if (lower and upper and digit and symbol) == 0:
        print("Unreliable password\nTry again")
        return the_pass()
    confirm_pass = input("Confirm password:" )
    if confirm_pass != your_pass:
        print("Password not confirm")
        the_pass()
    return your_pass

def the_checking(phone_finished,email_finished,pass_finished):
    print("==End==")
    count_pass = len(pass_finished)
    count_pass = count_pass * "*"
    print(
        f"Поздравляем с успешной регистрацией!\n\
        Ваш номер телефона: {phone_finished}\n\
        Ваш email: {email_finished}\n\
        Ваш пароль: {count_pass}"
        )










if __name__ == '__main__':
    main()
