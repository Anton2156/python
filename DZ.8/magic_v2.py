import random
import json
from pathlib import Path
STATS_PLAYERS = Path(__file__).resolve().parent

def main():
    number_of_games = 0
    attempts = 0
    magic(number_of_games,attempts)

def magic(number_of_games,attempts):
    name = input("Введи своє ім'я:")
    print("Вгадай число від 0 до 5")
    limit = 5
    random_number = random.randint(0,limit)
    i = 0
    new_rec = limit
    while True:
        try:
            num = int(input("Введи число= "))
            i += 1
        except ValueError:
            print("Це повинно бути число")
            continue
        if num != random_number:
            if num > random_number:
                print("Спробуй менше число,давай знову!")
            else:
                print("Спробуй більше число,давай знову!")
        elif num == random_number:
            print("\nТи виграв!")
            print("Кількість спроб -",i)
            if i < new_rec:
                print("Ура,ти поставив новий рекорд",i,"!!!!")
                new_rec = i
            else:
                print("Твій рекорд -",new_rec,"")
            all_end = str(input("Продовжити? (y/n):"))
            number_of_games += 1
            attempts += i
            i = 0
            print("\n")
            if all_end == "y":
                random_number = random.randint(0,10)
                continue
            else:
                avg_attempts = attempts/number_of_games
                player_data(name,number_of_games,new_rec,avg_attempts,attempts)
                break

def player_data(name,number_of_games,new_rec,avg_attempts,attempts):
    stats_players = STATS_PLAYERS / "stats_players.json"
    player_data = {
        "name":name,
        "games":number_of_games,
        "record":new_rec,
        "attemps":attempts,
        "avg_attempts":avg_attempts,
        }
    print("Твоє ім'я:",name,"")
    print(f"Кількість ігр:{number_of_games}")
    print("Твій рекорд :",new_rec,"")
    print("Твої всі спроби :",attempts,"")
    print("Твоє середню сначення спроб за гру :",avg_attempts,"")
    with open(stats_players, "a") as f:
        data = json.dumps(player_data, indent=4)
        f.write(data)
main()