
string=input("enter string: ")
string = string.split()
print("",len(string),"= Words")
a=0
for i in string:
    if len(i) > a:
        a = len(i)
        word = i    
print("the longest word is: ",word)