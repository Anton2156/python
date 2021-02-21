from pathlib import Path
import re
import string
PHONE_BOOK = Path(__file__).resolve().parent

phone_book = PHONE_BOOK / "phone_book.txt"
edit_phone_book = PHONE_BOOK / "edit_phone_book.txt"

def main():
    edit()


def edit():
    with open(phone_book,"r") as f:
        fl = open(edit_phone_book,"w").close()
        read = f.read()
        read = read.split("\n")
        for i in read:
            phone = re.sub(r'\D',"",i)
            phone = '+380' + phone[-9:]
            name =  re.sub('[^a-zA-Z]', '', i).capitalize()
            if len(phone) == 13 and (name[0] == "M" or name[-1] == "a"):
                name =  re.sub('[^a-zA-Z]', '', i).capitalize()
                with open(edit_phone_book,"a") as f:
                    f.write(f"{name} - {phone}\n")








if __name__ == "__main__":
    main()