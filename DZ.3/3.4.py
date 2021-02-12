while True:
    n = int(input("Enter the number of digits: "))
    print("Enter '+' if you want to add \nEnter '-' if you want to subtraction \nEnter '*' if you want to multiplication \nEnter '/' if you want to division")
    actoin = str(input("Enter the actoin: "))
    i = 0
    sum_,sub_,mul_,dev_ = 0,0,1,1
    a = 1
    b = 1
    if actoin == "+":
        while i < n:
            amount = int(input("Enter the number: "))
            sum_ = sum_ + amount
            i += 1
        print(sum_)
    elif actoin == "-":
        while i < n:
            amount = int(input("Enter the number: "))
            if i == 0:
                sub_ = amount - sub_
            else:
                sub_ = sub_ - amount
            i += 1
        print(sub_)
    elif actoin == "*":
        while i < n:
            amount = int(input("Enter the number: "))
            mul_ = mul_ * amount
            i += 1
        print(mul_)
    elif actoin == "/":
        while i < n:
            amount = int(input("Enter the number: "))
            if i == 0:
                dev_ = amount / dev_
            else:
                dev_ = dev_ / amount
            i += 1
        print(dev_)
    all_end = str(input("Continue? (y/n):"))
    if all_end == "y":
        pass
    else:
        print("Bye!")
        break














