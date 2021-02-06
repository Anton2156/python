try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
except ValueError:
    try:
        print("not a number")
        a = int(input("Enter the first number again: "))
        b = int(input("Enter the second number again : "))
    except ValueError:
        print("Error")
        
finally:
     print("Enter '+' if you want to add \nEnter '-' if you want to subtraction \nEnter '*' if you want to multiplication \nEnter '/' if you want to division")
     operator = str(input("\nEnter the actoin: "))
     
         
try:
    if operator == "+":
        print(a+b)
    elif operator == "-":
        print(a-b)
    elif operator == "*":
        print(a*b)
    elif operator == "/":
        print(a/b)
    else:
        print("Wrong action or Not a number  ")
except ZeroDivisionError:
    print("Error - division by zero")
except ValueError:
    print("Error - Not a number")
except NameError:
    print("Error - Not a number")
