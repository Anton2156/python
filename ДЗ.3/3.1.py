print("Enter:   \n    1 - Find even and odd digits of the number.\n    2 - Find the factorial of a number\n    3 - Show a sequence of numbers squared\n    4 - Leave")
while True:
    a = int(input("Choose the actoin: "))
    if a == 1:
        num = int(input("Enter the number: "))
        even,odd,zero = 0,0,0
        num_ = num
        while num > 0:
            a = num % 10
            if a  == 0:
                zero += 1
            elif a % 2 == 0:
                even += 1
            else:
                odd += 1
            num = num // 10
        print("The number ",num_,"has: \n      Even numbers - ",even,"\n      Odd numbers - ",odd,"\n      Zeros - ",zero,"")
    elif a == 2:
        fac = int(input("Enter the number: "))
        n = 1
        i = 0
        while i < fac:
            i += 1
            n = n * i
        print(n)
    elif  a == 3:
        limit = int(input("Enter the limit: "))
        i = 1
        power = int(input("Enter the power: "))
        if limit == 0 or (limit == 0 and power == 0):
            print("Enter not limit 0")
        else:
            while i ** power < limit:
                if power == 0:
                    print("There is no limit")
                    break
                else:
                    print(i ** power)
                    i += 1
    elif a == 4:
        print ("Bye!")
        break
#test
