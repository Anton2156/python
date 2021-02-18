from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / "users.txt"

with open(file_path, "r") as f:
    read = f.read()
    read = read.split("\n")
    print(read)
    for i in read:
        print(i)
