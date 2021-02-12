while True:  
    try:
        start = input("Enter the start of the numeric series: ")
        if start != "":
            start = int(start)
            end = int(input("Enter the end of the numeric series: "))
        else:
            start = 0
            end = int(input("Enter the end of the numeric series: "))
        range_ = range(start,end + 1)
        sum_ = 0
        mult_odd = 1
        if start < end:
            for i in range_:
                sum_ += i
                if i % 2 == 1:
                    mult_odd  *= i
            print("Sum all = ",sum_,"")
            print("Mult odd = ",mult_odd,"")
        elif start == end:
            print("Sum all = ",0,"")
            print("Sum odd = ",0,"")
        else:
            print("Wrong number order")
    except ValueError:
        print("Enter the number pls")
    all_end = str(input("Continue? (y/n):"))
    if all_end == "y":
        pass
    else:
        print("Bye!")
        break





