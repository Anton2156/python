while True:
    phone = input('Enter phone number: ')
    i = 0
    count_d = ""
    for char in phone:
        if char.isdigit():
            count_d += char
        else:
            continue
    if (len(count_d) == 10 and count_d[:1] == "0"):
        print("38"+ count_d)
        break
    elif (len(count_d) == 12 and count_d[:3] == "380"):
        print(count_d)
    else:
        print("\nIncorrect number format")
        end = str(input("Enter again? (y/n):"))
        if end == "y":
            pass
        else:
            print("Bye!")
            break
        
