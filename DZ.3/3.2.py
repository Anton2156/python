#1-спосіб через віднімання
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
while a > 0 and b > 0:
    if a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    else:
        print("НОД; = ",a,"")
        break
else:
    print("Enter a positive number or not 0")

#2-спосіб через отримання остачі від ділення(Більш універсальний)
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
while a > 0 and b > 0:
    if a > b:
        a = a % b
    else:
        b = b % a 
if b >= 0 and a >= 0:
    print("НОД = ",a + b,"")
else:
    print("Enter a positive number or not 0")






