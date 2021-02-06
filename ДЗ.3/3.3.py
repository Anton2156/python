import random
limit = int(input("Enter the limit of the <<Magic number>>: "))
random_number = random.randint(0,limit)
i = 0
new_rec = limit
while True:
    i += 1
    num = int(input("Let's try= "))
    if num != random_number:
        if num > random_number:
            print("Try a smaller number,Let's again!")
        else:
            print("Try a bigger number,Let's again")
    elif num == random_number:
        print("\nYou win!")
        print("You spent",i,"attempts")
        if i < new_rec:
            print("Hooray, you set a new record",i,"!!!!")
            new_rec = i
        else:
            print("Your record -",new_rec,"")
        i = 0
        all_end = str(input("Continue? (y/n):"))
        print("\n")
        if all_end == "y":
            random_number = random.randint(0,10)
            continue
        else:
            print("Bye!")
            break