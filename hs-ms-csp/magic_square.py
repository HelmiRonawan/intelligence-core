import numpy as np

def magic_square(matrix_ms):
    i_size = len(matrix_ms[0])
    sum_list = []

    for col in range(i_size):
        sum_list.append(sum(row[col] for row in matrix_ms))
        sum_list.extend([sum(lines) for lines in matrix_ms])

        dl_result = 0
        for i in range(0, i_size):
            dl_result += matrix_ms[i][i]
        sum_list.append(dl_result)
        dr_result = 0
        for i in range(i_size - 1, -1, -1):
            dr_result += matrix_ms[i][i]
        sum_list.append(dr_result)
        if len(set(sum_list)) > 1:
            return False
        return True
    
data = []
n = 9

for i in range(0, n):
    ele = int(input("Enter nilai square: "))
    data.append(ele)
print(data)

data = np.reshape(data, (3, 3))

print(data)
print("\n Nilai Magic Square yang dimasukkan adalah", magic_square(data))
