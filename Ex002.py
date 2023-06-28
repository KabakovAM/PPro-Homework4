def text_to_unicode(_str):
    result_list = []
    for i in _str:
        if ord(i) in result_list:
            continue
        else:
            result_list.append(ord(i))
    result_list.sort(reverse=True)
    print(result_list)

text_to_unicode(input('Введите текст: '))