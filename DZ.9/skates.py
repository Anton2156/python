
def main():
    available_sizes = input("Введіть доступні розмірі в наявності через пробел:").split()
    print(available_sizes)
    foot_sizes = input("Розмір ног відвідувачів:").split()
    # print(foot_sizes)
    skates(available_sizes, foot_sizes)


def skates(available_sizes, foot_sizes):
    a = 0
    for i in available_sizes:
        for j in foot_sizes:
            print(i,j)
            if j <= i:
                a += 1
                break
    print(a)












main()