string = 'Lorem, Ipsum, is, simply, dummy,\
 text, of, the, printing, industry.'

print("1. Изменить строку таким образом, чтоб вместо ', ' был пробел ' '")
print("Answer = ",string.replace(",",""),"\n")

print("2. Найти индекс самой последней буквы 's' в строке.")
a2 = string.replace(",","")
print("Answer = ",a2.rfind("s"),"\n")

print("3. Найти количество букв 'i' в строке (регистр не имеет значения).")
print("Answer = ",string.count("i") + string.count("I"),"\n")

print("4. Найти и вывести срез строки.")
start = string.find("simply")
end = string.find("text") + len("text")
a4 = string[start:end]
a4 = a4.replace(",","")
print("Answer = ",a4,"")

print("\n5. Продублируйте первую половину строки 3 раза и \
склейте с второй половиной и выведите на экран.")
a5 = string.replace(",","")
half = len(a5) / 2
print("Answer = ",(a5[:int(half)] * 3) + a5[int(half):],"")
