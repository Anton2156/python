# def main():
#     sort_ascending()

def sort_ascending(my_list):
    #my_list = [23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3]
    edit_list = my_list[:]
    a = []
    i = 0
    for ls in my_list:
        i += 1
        if ls == -1:
            a.append(my_list.index(-1,i-1))
            edit_list.remove(-1)
    edit_list.sort()
    for j in a:
        edit_list.insert(j,-1)
    print(my_list)
    print(edit_list)
    return edit_list


t_1 = [-1, 150, 190, 170, -1, -1, 160, 180]
assert sort_ascending(t_1) == [-1, 150, 160, 170, -1, -1, 180, 190]

t_2 = [-1, -1, -1, -1, -1]
assert sort_ascending(t_2) == [-1, -1, -1, -1, -1]

t_3 = [4, 2, 9, 11, 2, 16]
assert sort_ascending(t_3) == [2, 2, 4, 9, 11, 16]

t_4 = [23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3]
assert sort_ascending(t_4) == [1, 3, -1, 23, 43, -1, -1, 54, -1, -1, -1, 77]

t_5 = [-1]
assert sort_ascending(t_5) == [-1]

print("All tests passed successfully!")

# main()

