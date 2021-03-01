data = [
    (2, "green"),
    (1, "blue"),
    (2, "yellow"),
    (1, "aquamarine"),
    (4, "red"),
    (3, "gold"),
    (5, "black"),
    (2, "brown"),
    (5, "pink"),
    (1, "purple"),
    (4, "white"),
    (1, "gray"),
]

print("1=============================\n")
print(sorted(data, key=lambda d: d[1].lower()))

print("2=============================\n")
print(sorted(data, key=lambda d: (d[0], d[1].lower())))

print("3=============================\n")
print(list(filter(lambda d: len(d[1]) == 4, data))) 
# print([i for i in data if len(i[1]) == 4])

print("4=============================\n")
data = sorted(data, key=lambda d: d[1].lower())
print(data[0][1])
