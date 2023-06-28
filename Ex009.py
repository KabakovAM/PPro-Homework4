

def tras_matrix(matrix_a):
    matrix_b = []
    temp = []
    i = 0
    for k in range(len(matrix_a[i])):
        for i in range(len(matrix_a)):
            temp.append(matrix_a[i][k])
        matrix_b.append(temp.copy())
        temp.clear()
    return matrix_b


matrix_a = [[1,2,3,4],[5,6,7,8]]
print(tras_matrix(matrix_a))