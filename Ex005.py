def salary(name_list, salary_list, bonus_list):
    salary_dic = {}
    for i in range(len(name_list)):
        salary_dic[name_list[i]] = salary_list[i] / 100 * float(bonus_list[i][0:-1])
    print(salary_dic)

salary(['Вася', 'Миша', 'Саша'], [500, 600, 700], ['15%', '10.25%', '25%'])
