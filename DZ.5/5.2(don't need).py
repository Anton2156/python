import math

def main():
    number1 = int(input("Перше число: "))
    number2 = int(input("Друге число: "))
    action = input("Введіть дію: ")
    if action == "+":
        answer = get_sum(number1,number2)
    elif action == "-":
        answer = get_sud(number1,number2)
    elif action == "*":
        answer = get_mul(number1,number2)
    elif action == "/":
        answer = get_div(number1,number2)
    print(f'Верно, {answer}!')

def get_sum(a,b):
    answer = input(f'Сколько будет {a} + {b}: ')
    if answer != str(a + b):
        print('Неверно! Попробуйте еще раз.')
        return get_sum(a,b)
    return answer

def get_sud(a,b):
    answer = input(f'Сколько будет {a} - {b}: ')
    if answer != str(a - b):
        print('Неверно! Попробуйте еще раз.')
        return get_sub(a,b)
    return answer

def get_mul(a,b):
    answer = input(f'Сколько будет {a} * {b}: ')
    if answer != str(a * b):
        print('Неверно! Попробуйте еще раз.')
        return get_mul(a,b)
    return answer

def get_div(a,b):
    answer = input(f'Сколько будет {a} / {b}: ')
    if answer != str(a / b):
        print('Неверно! Попробуйте еще раз.')
        return get_div(a,b)
    return answer



main()

