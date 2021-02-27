import re


def main():
    list_in = input("Enter the string")
    list_in = re.sub('[^a-z0-9A-Z]', ' ', list_in).split()
    longest_strings(list_in)
    

def longest_strings(list_in):
    longest_word = list_in[0]
    list_ = []
    for i in list_in:
        if len(i) > len(longest_word):
            longest_word = i
    for i in list_in:
        if len(i) == len(longest_word):
            list_.append(i)
    print(list_)
    return list_


t_1 = ["x"]
assert longest_strings(t_1) == ["x"]

t_2 = ["abc", "eeee", "abcd", "dcd"]
assert longest_strings(t_2) == ["eeee", "abcd"]

t_3 = ["a", "abc", "cbd", "zzzzzz", "a", "abcdef", "asasa", "aaaaaa"]
assert longest_strings(t_3) == ["zzzzzz", "abcdef", "aaaaaa"]

t_4 = ["enyky", "benyky", "yely", "varennyky"]
assert longest_strings(t_4) == ["varennyky"]

t_5 = ["abacaba", "abacab", "abac", "xxxxxx"]
assert longest_strings(t_5) == ["abacaba"]




main()
