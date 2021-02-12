
n = input("Enter the number: ")
n = int(n)
if n >= 999:
    print("Error - number less  than 999") 
    
else:
    a1 = n % 10
    a2 = n % 100 // 10
    a3 = n // 100
    print("sum", a1 + a2 + a3)
if a1 < a2 < a3:
    print("Порядок-убывание")
elif a1 > a2 > a3:
    print("Порядок-Возростание")
elif a1 == a2 == a3:
    print("Порядок-Равны")
else:
    print("Порядок-В разброс")





