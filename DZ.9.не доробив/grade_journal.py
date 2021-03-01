def main():
    try:
        a = int(input("\nВведіть кількість студентів: "))
    except ValueError:
        main()
    i = 0
    student = []
    while i < a:
        i += 1
        student.append(
            {
                "name":input(f"Введіть Фамілію - Студент {i}:"),
                "point":input(f"Введіть бали - Студент {i}:")
            }
        )
    # print(sorted(student, key=lambda st: int(st["point"]),reverse=True))
    for i in sorted(student, key=lambda st: int(st["point"]),reverse=True):
        print(i["name"])

if __name__ == "__main__":
    main()