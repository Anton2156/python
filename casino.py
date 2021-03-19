import random
import json
import time


def main():
    nick_name = input("Введи свій nick-name:")
    menu(nick_name)

def menu(nick_name):
    a = input("")
    player_data = check_nickname(nick_name)
    player_data_for_magic = player_data["Magic"]
    player_data_for_Blackjack = player_data["Blackjack"]
    my_points = player_data["MyPoints"]
    print(f"==========\nУ вас {my_points}₴ гривень \n==========", end=" "); input()

    print("\n=====Casino=====\nГлавное меню:\
        \n  1. Magic\
        \n  2. Blackjack (21)\
        \n  3. Free point\
        \n  4. Переглянути статистику\
        \n  5. Зкінути статистику\
        \n  6. Змінити гравця\
        \n  7. Вихід")
    action = input("\nВиберіть дію:")
    print("\n\n")
    if action == "1":
        Magic(player_data_for_magic, nick_name, my_points)
    elif action == "2":
        Blackjack(player_data_for_Blackjack, nick_name, my_points)
    elif action == "3":
        freePoint(nick_name)
    elif action == "4":
        print("\n=====Casino=====\n\nВаша статистика")
        show_data(nick_name)
        print("Повенення до головного меню\n=====Casino=====")
        menu(nick_name)
    elif action == "5":
        data_reset(nick_name,my_points )
        print("\n=====Casino=====\nВаша статистика успшішно скинута!")
        print("\n\nПовенення до головного меню\n=====Casino=====")
        menu(nick_name)
    elif action == "6":
        main()
    elif action == "7":
        exit
    else:
        print("Повенення до головного меню")
        menu(nick_name)

def check_nickname(nick_name):
    with open("users.json") as f:
        data_name = json.load(f)
    if nick_name in data_name.keys():
        player_data = data_name[nick_name]
    else:
        player_data = save_new_pleyer(nick_name)
    return player_data

def save_data(player_data, nick_name, game, my_points):
    with open("users.json", "r") as f:
        data = json.load(f)
        
    with open("users.json", "w") as f:
        data_game = data[nick_name] 
        data_game["MyPoints"] = my_points 
        data_game[game] = player_data
        data = json.dumps(data, indent=4)
        f.seek(0)
        f.write(data)

def show_data(nick_name):
    with open("users.json", "r") as f:
        data = json.load(f) 
        data = data[nick_name]
        data_magic = data["Magic"]
        data_blackjack = data["Blackjack"]
        print("==Magic==")
        for i in data_magic:
            print(f"{i}\t{data_magic[i]}")
        print("\n==Blackjack==")
        for i in data_blackjack:
            print(f"{i}\t{data_blackjack[i]}")

def save_new_pleyer(nick_name):
    print(f"\n=====Casino=====\nВітаємо з регестрацією {nick_name}\n=====Casino=====\n\n")
    rules()
    player_data={
                "MyPoints":1000,
                "Magic":{"Record": 0,"Games": 0,"Avg_attempts": 0},
                "Blackjack":{"Win": 0,"Lose": 0,"Press stop": 0}
    }
    with open("users.json", "r+", encoding="utf-8") as f:
        data = json.load(f)
        data[nick_name] = player_data
        data = json.dumps(data, indent=4, ensure_ascii=False)
        f.seek(0)
        f.write(data)
    return player_data

def data_reset(nick_name, my_points):
    player_data={
                "MyPoints":my_points,
                "Magic":{"Record": 0,"Games": 0,"Avg_attempts": 0},
                "Blackjack":{"Win": 0,"Lose": 0,"Press stop": 0}
    }
    with open("users.json", "r") as f:
        data = json.load(f)

    with open("users.json", "w") as f:
        data[nick_name] = player_data
        data = json.dumps(data, indent=4)
        f.seek(0)
        f.write(data)

def Magic(player_data_for_magic, nick_name, my_points):
        game = "Magic"
        value, value1, value2, value3, value4, value5 = lvl_magic(my_points)
        random_number = random.randint(1, 52)
        while True:
            print("\n\n=====Casino=====\n\nВгадайте Магічне число від 1 до 52")
            counter = 0  
            print("==Ігра починається==\n")
            while True:
                try:
                    number = int(input("Ваше число: "))
                    counter += 1 
                except ValueError:
                    print("Це повинно бути число.")
                    continue
                if number > random_number: print("Магічне число менше", number)
                elif number < random_number: print("Магічне число більше", number)
                else:
                    print("\nВітаю! Ви вгадали число",number,"")
                    random_number = random.randint(1, 10)
                    points = 0
                    points_1 = point_for_magic(counter, points, value, value1, value2, value3, value4, value5)
                    my_points += points_1
                    print(f"Тепер у вас {my_points}₴ гривень")
                    break
            if not player_data_for_magic["Record"] or player_data_for_magic["Record"] > counter:
                    player_data_for_magic["Record"] = counter
            games = player_data_for_magic["Games"]
            avg = player_data_for_magic["Avg_attempts"]
            player_data_for_magic["Games"] += 1
            player_data_for_magic["Avg_attempts"] = round((games * avg + counter) / (games + 1), 2)

            save_data(player_data_for_magic, nick_name, game, my_points)
            action = input("\nСпробувати ще раз?(y/menu/exit інше:main):") 
            if action == "y":
                counter = 0
                continue
            elif action == "menu":
                menu(nick_name)
            elif action == "exit":
                print("Бувай!")
            else:
                main()

def point_for_magic(counter, points, value, value1, value2, value3, value4, value5):
    if counter == 1:
        print("🎉🎉🎉🎉Ого не може бути!!🎉🎉🎉🎉")
        print(f"Вам начисляно {value5} очків")
        points = value5
    elif counter == 2:
        print(f"Вам начисляно {value4} очків")
        print("А ти щасливчик")
        points = value4
    elif counter == 3:
        print("Повело повезло!")
        print(f"Вам начисляно {value3} очків")
        points = value3
    elif counter == 4:
        print(f"Вам начисляно {value2} очків")
        points = value2
    elif counter == 5:
        print(f"Вам начисляно {value1} очків")
        points = value1
    elif counter == 6:
        print(f"Вам начисляно {value} очків")
        points = value
    elif counter == 7:
        print(f"У вас знято {value1} очків :(")
        points = -value1
    elif counter == 8:
        print("Не ну а че")
        print(f"У вас знято {value2} очків")
        points = -value2
    elif counter == 9:
        print("Ахсахса")
        print(f"У вас знято {value3} очків")
        points = -value3
    else:
        print("Дякую за очки:)")
        print(f"У вас знято {value4 * 2} очків")
        points = -value4 * 2
    return points

def Blackjack(player_data_for_Blackjack, nick_name, my_points):
    cof = lvl_blackjack()
    while True:
        while True:
            try:
                rate = int(input("Зробіть свою ставку:"))
            except ValueError:
                continue  
            if rate > my_points or rate < 0:
                print("Недостатьньо коштів!!")
                continue
            break
        my_rate_points = rate
        game = "Blackjack"
        print(player_data_for_Blackjack)
        deсk_of_cards = desk()
        while True:
            random_first_deck = random.choice(deсk_of_cards)
            random_first_card = random.choice(list(random_first_deck.keys()))
            
            random_second_deck = random.choice(deсk_of_cards)
            random_second_card = random.choice(list(random_second_deck.keys()))
            if random_first_card != random_second_card:
                my_cards = [random_first_card,random_second_card]
                my_blackjack_point = random_first_deck[random_first_card] + random_second_deck[random_second_card]
                del random_first_deck[random_first_card]
                del random_second_deck[random_second_card]
                break
        while True:
            print("\n\n=====Casino=====\nОчкі:", my_blackjack_point)
            print("Ваші карти:", end=" ")
            for card in my_cards:
                print(card,end=" ")
            if my_blackjack_point == 21:
                print("\nВи перемогли! :)\n")
                player_data_for_Blackjack["Win"] += 1
                if cof == 2:my_points += my_rate_points
                else:my_points += round(my_rate_points * cof, 2)
                break
            elif my_blackjack_point > 21:
                if ("♦Туз" in my_cards) or ("♣Туз" in my_cards) or ("♠Туз" in my_cards) or ("♥Туз" in my_cards):
                    input("\nУ вас БІЛЬШЕ ніж 21 очків тому ВСІ Тузи = 1")
                    for i in my_cards:
                        j = my_cards.index(i)
                        if i == "♦Туз":
                            my_cards.remove(i)
                            my_cards.insert(j, "♦Туз(1)")
                            my_blackjack_point -= 10
                        if i == "♣Туз":
                            my_cards.remove(i)
                            my_cards.insert(j, "♦Туз(1)")
                            my_blackjack_point -= 10
                        if i == "♠Туз":
                            my_cards.remove(i)
                            my_cards.insert(j, "♦Туз(1)")
                            my_blackjack_point -= 10
                        if i == "♥Туз":
                            my_cards.remove(i)
                            my_cards.insert(j, "♦Туз(1)")
                            my_blackjack_point -= 10
                    print("\n==============================")
                else:
                    print(f"\nВи програли у вас було {my_blackjack_point} очків :(\n")
                    player_data_for_Blackjack["Lose"] += 1
                    if cof == 2:my_points -= my_rate_points
                    else:my_points -= round(my_rate_points * cof, 2)
                    break
            else:
                action = input("\n\n=====Casino=====\nЯкщо хочеш взяти карту ввeди 'add' або 'stop' або 'exit':")
                if action == "add":
                    random_new_deck = random.choice(deсk_of_cards)
                    random_new_card = random.choice(list(random_new_deck.keys()))
                    my_cards.append(random_new_card)
                    my_blackjack_point += random_new_deck[random_new_card]
                    del random_new_deck[random_new_card]
                    continue
                elif action == "stop":
                    print("\nВи не втратили очкі\n")
                    player_data_for_Blackjack["Press stop"] += 1
                    break
                else:
                    print("Ви вийшли в з гри\n")
                    break
        print(f"Тепер у вас:{my_points}")
        save_data(player_data_for_Blackjack, nick_name, game, my_points)
        action = input("\nСпробувати ще раз?(y/menu/exit інше:main): ") 
        if action == "y":
            continue
        elif action == "menu":
            menu(nick_name)
        elif action == "exit":
            print("Бувай")
            break
        else:main()

def desk():
    desk_of_cards = [
    {
        "♦Два":2,
        "♦Три":3,
        "♦Чотири":4,
        "♦П'ять":5,
        "♦Шість":6,
        "♦Сім":7,
        "♦Вісім":8,
        "♦Девять":9,
        "♦Деcять":10,
        "♦Валет":10,
        "♦Дама":10,
        "♦Король":10,
        "♦Туз":11
    },
    {
        "♥Два":2,
        "♥Три":3,
        "♥Чотири":4,
        "♥П'ять":5,
        "♥Шість":6,
        "♥Сім":7,
        "♥Вісім":8,
        "♥Девять":9,
        "♥Деcять":10,
        "♥Валет":10,
        "♥Дама":10,
        "♥Король":10,
        "♥Туз":11
    },
    {
        "♣Два":2,
        "♣Три":3,
        "♣Чотири":4,
        "♣П'ять":5,
        "♣Шість":6,
        "♣Сім":7,
        "♣Вісім":8,
        "♣Девять":9,
        "♣Деcять":10,
        "♣Валет":10,
        "♣Дама":10,
        "♣Король":10,
        "♣Туз":11
    },
    {
        "♠Два":2,
        "♠Три":3,
        "♠Чотири":4,
        "♠П'ять":5,
        "♠Шість":6,
        "♠Сім":7,
        "♠Вісім":8,
        "♠Девять":9,
        "♠Деcять":10,
        "♠Валет":10,
        "♠Дама":10,
        "♠Король":10,
        "♠Туз":11
    }]
    return desk_of_cards

def lvl_blackjack():
    while True:
        a = input("ПОПЕРЕДЖЕННЯ для гри про режими Avarage і Hard рекомендую познайомитись з правилами")
        lvl = input("Виберіть режим гри\
                    \nВведіть:\
                    \n\tE(Easy)\
                    \n\tA(Avarage)\
                    \n\tH(Hard):")
        if lvl == "E":
            cof = 2
        elif lvl == "A":
            cof = 3
        elif lvl == "H":
            cof = 5
        else:
            print("Можливо у вас не достьньо коштів для цієї гри спробуйте ще раз")
            continue
        break
    return cof

def lvl_magic(my_points):
    a = input("ПОПЕРЕДЖЕННЯ для гри про режими Avarage і Hard рекомендую познайомитись з правилами")
    while True:
        lvl = input("Виберіть режим гри\
                    \nВведіть:\
                    \n\tmenu\
                    \n\tE(Easy-У вас повинно бути на балансі 1000 або більше)\
                    \n\tA(Avarage-У вас повинно бути на балансі 5000 або більше)\
                    \n\tH(Hard-У вас повинно бути на балансі 10000 або більше):")
        if lvl == "E" and my_points >= 1000:
            value = 0
            value1 = 65
            value2 = 125
            value3 = 250
            value4 = 500
            value5 = 5000
            break
        elif lvl == "A" and my_points >= 5000:
            value = 0
            value1 = 312
            value2 = 625
            value3 = 1250
            value4 = 2500
            value5 = 25000
            break
        elif lvl == "H" and my_points >= 10000:
            value = 0
            value1 = 650
            value2 = 1250
            value3 = 2500
            value4 = 5000
            value5 = 50000
            break
        elif lvl == "menu":
            menu(nick_name)
            break
        else:
            print("\n\nНедостатьньо коштів!!!!")
    return value, value1, value2, value3, value4, value5

def freePoint(nick_name):
    with open("users.json", "r+") as f:
        data = json.load(f)
        data_game = data[nick_name]
        my_points = data_game["MyPoints"]
        while True:
            if input("Введи 'exit' для повернення в menu:") != "exit":
                my_points += 5
                print("Тепеп у вас ",my_points," очків")
            else:
                data_game["MyPoints"] = my_points 
                data = json.dumps(data, indent=4)
                f.seek(0)
                f.write(data)
                break
    menu(nick_name)

def rules():
    stop = input()
    print("==Magic==\n\
        =У грі Magic вам потрібно вгадати число(від 1 до 52)=\n\
        =Чим скоріш ви вгадаєте число більш приз ви отримаєте!!!=\n\
            !!При перемозі з ПЕРШОЇ спроби в отримуєте Джекпот!!\n\
        =Але після 6-мої спроби(6 спроба = 0) ви будете втарачати очкі (і чим більш спроб витрачено тим більш очок знімається)=\n\
            !!Але після 10-тої спроби  МІНУС буде максимальний!!\n\
        =Також ви можете вибрати режим гри=\n\
            Easy:\n\
                Очкі будуть роподілені так:\n\
                    Спроба 1 = 5000\n\
                    Спроба 2 = 500\n\
                    Спроба 3 = 250\n\
                    Спроба 4 = 125\n\
                    Спроба 5 = 65\n\
                    Спроба 6 = 0\n\
                    Спроба 7 = -65\n\
                    Спроба 8 = -125\n\
                    Спроба 9 = -250\n\
                    Спроба 10 = -1000\n\
            Avarage:\n\
                    Спроба 1 = 25000\n\
                    Спроба 2 = 2500\n\
                    Спроба 3 = 1250\n\
                    Спроба 4 = 625\n\
                    Спроба 5 = 312\n\
                    Спроба 6 = 0\n\
                    Спроба 7 = -321\n\
                    Спроба 8 = -625\n\
                    Спроба 9 = -1250\n\
                    Спроба 10 = -5000\n\
            Hard:\n\
                    Спроба 1 = 50000\n\
                    Спроба 2 = 5000\n\
                    Спроба 3 = 2500\n\
                    Спроба 4 = 1250\n\
                    Спроба 5 = 650\n\
                    Спроба 6 = 0\n\
                    Спроба 7 = -650\n\
                    Спроба 8 = -1250\n\
                    Спроба 9 = -2500\n\
                    Спроба 10 = -10000\n\
    ")
    stop = input()

    print("==BlackJack==\n\
    =Вам потрібно зробити ставку=\n\
    =У гри BlackJack вам потрібно для перемогі набрати 21 очко=\n\
        Кожна карта має свою кількість очків:\n\
                Від двойкі до десяткі — від 2 до 10 відповідно,\n\
                у туза — 1 або 11 (11 пока сума карт буде менше  21, далі 1),\n\
                у карт з Картиноками (король, дама, валет) — 10.\n\
    =В началі гри ви отримуєте дві карти\n\
        Для перемогі ви можете БРАТЬ карти з колоди до поки ваша сума карт не буде 21\n\
        Якщо буде більше 21 ви програли\n\
        ТАКОЖ ви можете закінчити гру (не набрав більше 20 очок), тоді ваші ставка yвертається гравцю\n\
    =Також ви можете вибрати режим гри=\n\
        Easy:\n\
            Ваша ставка буду змінюватись в 2 раза (залежно від перемогі або поразкі)\n\
        Avarage:\n\
            Ваша ставка буду змінюватись в 3 раза (залежно від перемогі або поразкі)\n\
        Hard:\n\
            Ваша ставка буду змінюватись в 5 раза (залежно від перемогі або поразкі)\n\
    !!ПОПЕРЕДЖЕННЯ!! - при великій ставці і програші ваш баланс буде мінусовий!!\n\
    ")
    stop = input()
    print("==Інше==\n\
    =Також у вас є можливість заробити бесплатно очкі в гра Free point=\n\
        За 1 клік вам дають 5 очків\n\
        ")


if __name__ == "__main__":
    main()