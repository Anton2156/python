list_ = [6, 3, -1, 4, -1, 2, -1, 1]
print(list_)
a = 0
edit_list = []
for i in list_:
    if i == -1:
        index_ = list_.index(i) + a
        list_.remove(i)
        a =+ 1
        edit_list.append(index_)
list_ = sorted(list_)
for i in edit_list:
    list_.insert(i,-1)
print(list_)
