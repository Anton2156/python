s1 = "Some string"
s2 = "Some edited string"
print("Завдання 1")
print(f"==={s1}===")
string = input("Enter string:")
upper,lower = 0,0
for i in string:
    if i.islower() == True:
        lower += 1
    elif i.isupper() == True:
        upper += 1        
if lower == upper:
    print(string.swapcase())
elif lower > upper:
    print(string.lower())
elif upper > lower:
    print(string.upper())
print(f"==={s2}===")

print("\nЗавдання 2")
print(f"==={s1}===")
string = input("Enter string:")
if string[0].istitle() == True:
    print("done." + string)
else:
    print(string.replace(string[:5],"draft."))
print(f"==={s2}===")

print("\nЗавдання 3")
print(f"==={s1}===")
string = input("Enter string:")
if len(string) == 20:
    print(string)
elif len(string) < 20:
    print(string.ljust(20,"@"))
elif len(string) > 20:
    print(string[:20])
print(f"==={s2}===")

