def num_to_unicode(_str: str):
    num_list = list(map(int, _str.split()))
    num_dic = {}
    if num_list[0] > num_list[1]:
        num_list[0], num_list[1] = num_list[1], num_list[0]
    for i in range(num_list[0], num_list[1]+1):
        num_dic[chr(i)] = i
    print(num_dic)


num_to_unicode(input('Введите два числа через пробел: '))
