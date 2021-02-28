import re



# def main():
#     text = "hi world, hi python. i am very cool but but but i am still learning."
#     text = sorted(re.sub('[^a-z0-9A-Z]', ' ',text).split())
#     frequent_word(text)


def frequent_word(text):
    text = sorted(re.sub('[^a-z0-9A-Z]', ' ',text).split())
    max_count_word = ""
    data = {}
    for word in text:
        if word not in data:
            data[word] = text.count(word)
            if max_count_word == "":
                max_count_word = word
            elif len(max_count_word) < text.count(word):
                max_count_word = word
    return max_count_word


t_1 = "hi world, hi python. i am very cool but but but i am still learning."
assert frequent_word(t_1) == "but"

t_1 = "hi world, hi python"
assert frequent_word(t_1) == "hi"

t_1 = "hi world, hi python. i am very cool  but i am still learning."
assert frequent_word(t_1) == "am"

t_1 = "hi hi"
assert frequent_word(t_1) == "hi"

t_1 = "hi world, hi python. i am very cool cool cool but but but i am still learning."
assert frequent_word(t_1) == "but"

print("All tests passed successfully!")

# main()