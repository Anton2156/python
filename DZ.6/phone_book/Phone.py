from pathlib import Path
import re
import string
PHONE_BOOK = Path(__file__).resolve().parent

phone_book = PHONE_BOOK / "phone_book.txt"
edit_phone_book = PHONE_BOOK / "edit_phone_book.txt"

#Дуже криво але якось робить

def main():
    phone = input("Enter the phone:")
    name = input("Enter the name:")
    save_info(phone,name)
    char = char_()
    digits = digits_()
    edit_book(char,digits)

def digits_():
    with open(phone_book,"r") as f:
        a = ""
        read = f.read()
        read = read.split("\n")
        for phone in read:
            digits = re.sub(r'\D',"",phone)
            phone = '+380' + digits[-9:]
            if len(phone) != 13:
                print('Wrong format.')
                continue
            a = a + phone + "\n"
        a = a.split("\n")
        return a

def char_():
    with open(phone_book,"r") as f:
        read = f.read()
        read = read.split("\n")
        a = ""
        for i in read:
            i = re.sub('[^a-zA-Z]', '', i)
            a = a + i + "\n"
        a = a.split("\n")
        return a

def edit_book(char,digits):
    edit_phone_book = PHONE_BOOK / "edit_phone_book.txt"
    with open(edit_phone_book,"w") as f:
        i = 0
        while i < len(char) - 2:
            f.write(f"{digits[i]} - {char[i]}\n")
            i += 1

def save_info(phone,name):
    phone_book = PHONE_BOOK / "phone_book.txt"
    with open(phone_book, "a") as f:
        # f.write(f"{name} {surname} - {age}\n")
        print(f"{phone}  - {name}", file=f)
    a = input("Contunue?y/n")
    if a == "y":
        main()




if __name__ == "__main__":
    main()