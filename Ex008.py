def change_s():
    ars = 12
    bars = 13
    car = 14
    lip = 5
    s = 6
    list_s = locals()
    new_dic = {}
    for key, value in list_s.items():
        if key[-1] == 's' and key != 's':
            new_dic[key[:-1]] = value
            list_s[key] = None
    print(list_s)
    print(new_dic)


change_s()