import json

# # json.dumps(dict) для записи
# # json.load(file) для чтения

# a = [
#     {"short": "dict", "long": "dictionary"},
#     {"short": "dict", "long": "dictionary"},
#     {"short": "dict", "long": "dictionary"},
#     {"short": "dict", "long": "dictionary"},
# ]


# # запись
# with open("test.json", "a") as f:
#     data = json.dumps(a, indent=4)
#     f.write(data)


# # чтение
# with open("test.json") as f:
#     data = json.load(f)
#     print(data, type(data))
name = "Anton"
player_data = {
    "name":name
}
    # print("Твоє ім'я:",name,"")
    # print(f"Кількість ігр:{number_of_games}")
    # print("Твій рекорд :",new_rec,"")
    # print("Твої всі спроби :",attempts,"")
    # print("Твоє середню сначення спроб за гру :",avg_attempts,"")
with open("Stats_player.json", "a") as f:
    data = json.dumps(player_data, indent=4)
    f.write(data)