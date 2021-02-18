import random
import string
def main():
    len_pass = length_pass()
    choice_pass = input(
        "Enter the 'E'for Easy pass\
        \nEnter the 'A'for Average pass\
        \nEnter the 'H'for Hard pass\
        \nEnter The 'U' for User pass\
        \n\nChoise pass:")
    if choice_pass == "E":
        your_pass = easy_pass(len_pass)
    elif choice_pass == "A":
        your_pass = average_pass(len_pass)
    elif choice_pass == "H":
        your_pass = hard_pass(len_pass)
    elif choice_pass == "U":
        your_pass = user_pass(len_pass)
    else:
        print("Wrong value - try again")
        main()
    print(f"\nYour pass:{your_pass}")

def easy_pass(len_pass):
    i = 0
    your_pass = ""
    while i < len_pass:
        letter_for_pass = random.choice(string.ascii_lowercase)
        your_pass = your_pass + letter_for_pass
        i += 1
    return your_pass

def average_pass(len_pass):
    your_pass = ""
    i = 0
    while i < len_pass:
        letter_for_pass = random.choice(string.ascii_letters + string.digits)
        your_pass = your_pass + letter_for_pass
        i += 1
    return your_pass

def hard_pass(len_pass):
    i = 0
    your_pass = ""
    while i < len_pass:
        letter_for_pass = random.choice(string.ascii_letters + string.punctuation + string.digits)
        your_pass = your_pass + letter_for_pass
        i += 1
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
    if (lower and upper and digit and symbol) == 0 :
        print(your_pass)
        return hard_pass(len_pass)
    return your_pass

def user_pass(len_pass):
    password_characters = input("\nEnter the password characters:")
    i = 0
    your_pass = ""
    while i < len_pass:
        letter_for_pass = random.choice(password_characters)
        if letter_for_pass != " ":
            your_pass = your_pass + letter_for_pass
            i += 1
        else:
            continue
    return your_pass

def length_pass():

    print("\n")
    len_pass = int(input("Enter the length of the password:"))
    if len_pass < 4:
        print("The password is strong")
        end = input("You want to continue?(Y/N)")
        if end == "Y":
            return len_pass
        elif end == "N":
            return length_pass()
        else:
            print("Error:Try again")
            return length_pass()
    else:
        return len_pass

if __name__ == '__main__':
    main()
