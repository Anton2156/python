a = int(input("Enter the 1 side="))
b = int(input("Enter the 2 side="))
c = int(input("Enter the 3 side="))

if a + b < c or a + c < b or c + b < a:
    print("Не існує")
else:
    print("Існує")
