year = int(input("Enter the year: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Високосний рік- 366 днів")
    
else:
    print("Не високосний рік - 365 днів")