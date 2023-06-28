def bank():
    account = 0
    check = 0
    history = []
    data = menu()
    while data != 0:
        if data == 1:
            cash_in = int(input('Введите сумму для пополнения, кратную 50: '))
            while not (cash_in % 50 == 0 and cash_in > 0):
                cash_in = int(input('Введите сумму для пополнения, кратную 50: '))
            account += cash_in
            history.append(cash_in)
            check += 1
        if data == 2:
            cash_out = int(input('Введите сумму для снятия, кратную 50: '))
            while not (cash_out % 50 == 0 and cash_out >= 0):
                cash_out = int(input('Введите сумму для снятия, кратную 50: '))
                if percent_out(account, cash_out) < 0:
                    print('Недостаточно средств на счёте.')
            account = percent_out(account, cash_out)
            history.append(cash_out*-1)
            check += 1
        if check % 3 == 0:
            account += int(account/100*3)
            history.append(int(account/100*3))
            print('На ваш счёт начислено 3%, кэшбек')
        if account > 5000000:
            account -= int(account/100*10)
            history.append(int(account/100*10)*-1)
            print('С вашего счёта списали 10%, налог на роскошь')
        print(account)
        print(history)
        data = menu()


def menu():
    print('Выберите действие: \n1) Пополнить \n2) Снять \n0) Выйти')
    data = input()
    return int(data)


def percent_out(account, cash_out):
    percent = int(cash_out/100*1.5)
    if percent <= 30:
        account -= 30
    elif percent >= 600:
        account -= 600
    else:
        account -= percent
    account -= cash_out
    return int(account)


bank()