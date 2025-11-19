# Задание 1
my_list = [1,2,3,4,5]
shift = 2
copied_list = my_list[-shift:] + my_list[0:-shift]
print("Изначальный список", my_list)
print("измененный список", copied_list)

# Задание 2
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
new_matrix = []
shift2 = 1
for i in range(len(matrix)):
    copied_matrix = matrix[i][-shift2:] + matrix[i][0:-shift2]
    new_matrix.append(copied_matrix)
print("Изначальная матрица ",matrix)
print("Измененная матрица ",new_matrix)
