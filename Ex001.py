def text_per_str(_str):
    data = sorted(_str.split())
    longest = len(max(data, key=len))
    for i in range(len(data)):
        print(f'{i+1}) {data[i]:>{longest}}')


text_per_str(input('Введите текст: '))