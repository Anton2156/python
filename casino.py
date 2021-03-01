import random

def main():
    all_points = 0
    print("Главное меню:\
        \n  1. Magic\
        \n  2. Blackjack (21)\
        \n  3. Посмотреть статистику\
        \n  4. Сбросить игровой прогресс\
        \n  5. Вихід")
    menu = input("\nВиберіть дію:")
    if menu == "1":
        Magic(all_points)
    elif menu == "2":
        pass
    elif menu == "3":
        pass    
    elif menu == "4":
        pass
    elif menu == "5":
        pass
    else:
        print("Повенення до головного меню")
        main()
    # a = Magic(all_points)
    # print(a)

def rules():
    if input("Введіть '/rules' якщо потрібні правила гри або просто нажімть 'Enter' продовжть: ") == "/rules":
        print("""
            =======Magic=======
            Ви попали в гру "Magic" правила:
            1)Ви можете вибрать рівень ігри
                ================================
                Перша рівень це 'Easy'
                На уровні 'Easy' ви не втрачаєте очкі
                    Тут ви повинні вгада число від 1 до 10:
                    У вас є 5 спроб
                    Очкі за cпроби начисляються так:
                        1 - 50
                        2 - 25
                        3 - 10
                        4 - 5
                        5 - 0
        """)

def Magic(all_points):
    rules()
    random_number = random.randint(1, 10) 
    print("Вгадайте Магічне число від 1 до 10")
    counter = 0  
    print("==Ігра починається==\n")
    while True:
        try:
            number = int(input("Ваше число: "))
            counter += 1 
        except ValueError:
            print("Це повинно бути число.")
            continue
        if number > random_number:
            print("Магічне число менше", number)
        elif number < random_number:
            print("Магічне число більше", number)
        else:
            print("\nВітаю! Ви вгадали число",number,"")
            print("Витрачено спроб:", counter)
            random_number = random.randint(1, 10)
            points_1 = 0
            if counter == 1:
                print(f"Вам начисляно 50 очків")
                points_1 = 50
            elif counter == 2:
                print("Вам начисляно 25 очків")
                points_1 = 25
            elif counter == 3:
                print("Вам начисляно 10 очків")
                points_1 = 10
            elif counter == 4:
                print("Вам начисляно 5 очків")
                points_1 = 5
            else:
                print("Вам начисляно 0 очків")

            if all_points == 0:
                all_points = points_1
            else:
                all_points += points_1
            print("Тепер у вас",all_points,"очків")
            break

        if counter == 5:
            print("\nМагічне число було",random_number)
            print("Використано забагато спроб")
            break
    next_action = input("\nСпробувати ще раз?(y/n/menu):")
    if next_action == "Y":
        counter = 0
        Magic(all_points)
    elif next_action == "menu":
        main()
    return all_points



if __name__ == "__main__":
    main()