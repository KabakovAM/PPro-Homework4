def change_s(*, ars, bars, car, lip, s):
    list_s = locals()
    new_dic = {}
    for key, value in list_s.items():
            new_dic[value] = key
    print(list_s)
    print(new_dic)


change_s(ars = 12, bars = 3, car = 14, lip = 115, s = 6)