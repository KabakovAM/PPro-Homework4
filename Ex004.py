def bubble_sort(num_list):
    for i in range(len(num_list) - 1):
        for j in range(len(num_list) - 1 - i):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    print(num_list)


bubble_sort([7, 4, 6, 9, 1, 3, 2, 5, 8])