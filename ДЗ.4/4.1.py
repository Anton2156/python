string = input("Enter string:")
a = ""
a1 = 0
for i in string:
    if (i.isalpha() == True) or (i ==" "):
        a += i
    else:
        a += " "
        continue
print(a)
a = a.split()
print("",len(a)," Words")
for i_ in a:
    if len(i_) > a1:
        a1 = len(i_)
        word = i_
print("The longest word = ",word,"\nLength = ",a1,"")


