import random

def main():
    lucky_ticket = str(random.randint(1,10000000))
    luckyticket(lucky_ticket)


def luckyticket(lucky_ticket):
    print(lucky_ticket)
    num = len(str(lucky_ticket))
    the_first_half = 0
    the_second_half = 0
    if num % 2 == 0:
        for i in lucky_ticket[:int(num/2)]:
            the_first_half += int(i)
        for i in lucky_ticket[int(num/2):]:
            the_second_half += int(i)
    else:
        num = num - 1
        for i in lucky_ticket[:int(num/2)]:
            the_first_half += int(i)
        for i in lucky_ticket[int(num/2) + 1:]:
            the_second_half += int(i)
    if the_first_half == the_second_half:
        print("Твій білет щасливий!!!!")
        return True
    else:
        print("Твій білет не щасливий")
        return False

#Програма робить правильно але тести ні
assert luckyticket(str(1230)) is True
assert luckyticket(str(239017)) is False
assert luckyticket(str(134008)) is True
assert luckyticket(str(15)) is False
assert luckyticket(str(2020)) is True
assert luckyticket(str(199999)) is False
assert luckyticket(str(77)) is True
assert luckyticket(str(479974)) is True

print("All tests passed successfully!")


main()