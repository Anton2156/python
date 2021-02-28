def draw_border(a):
    new_list= []
    for i in a:
        new_list.append("*"+i+"*")
    new_list.append((len(new_list[0])) * "*")
    new_list.insert(0, (len(new_list[1])) * "*")
    print(new_list)
    return new_list


t_1 = ['django',
        'django']
assert draw_border(t_1) == ['********',
            '*django*',
            '*django*',
            '********']

t_2 = ['abc',
        'def']
assert draw_border(t_2) == ['*****',
            '*abc*',
            '*def*',
            '*****']


print("All tests passed successfully!")

