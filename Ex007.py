def count_m(company_dic: dict):
    money = 0
    check = True
    for key, value in company_dic.items():
        for i in range(len(value)):
            money += value[i]
        print(key, money)
        if money < 0:
            check = False
    print(check)
    return check

company_dic = {'АО Вася': [-30, 50, 60, -10], 'ООО Миша': [100, 30, 40, -500], 'ПАО Саша': [34, 25, 2]}
count_m(company_dic)
