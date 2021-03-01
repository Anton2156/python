import random
from pathlib import Path
DATA = Path(__file__).resolve().parent

print("====1====")
x = 2**3

print("====2====")
x = x + 3

print("====3====")
num_list = []
i = 0
while i < x:
    num_list.append(random.randint(1,x))
    i += 1
print(num_list)

print("====4====")
print(list(reversed(num_list)))

print("====5====")
num_list.append(len(num_list),11)
print(num_list)

# data = DATA / "stats_players.json"
# with open(data,"a")as file:
#     f.write
#     (f" Кількість елментів {len(num_list)}\
#     Кількість унікальних елемнтів {set(num_list)}\
#     "    
#     )

