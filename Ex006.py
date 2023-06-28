def sum_between(num_list, index_a, index_b):
    if index_a < index_b:
        start, stop = index_a + 1, index_b
    else:
        start, stop = index_b + 1, index_a
    if start < 0:
        start = 0
    if stop > len(num_list):
        stop = len(num_list)
    result = 0
    for i in range(start, stop):
        result += num_list[i]
    print(result)

sum_between([1, 2, 3, 4, 5, 6, 7, 8, 9], -1, 20)