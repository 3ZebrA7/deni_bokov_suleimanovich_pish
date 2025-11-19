# Задание 3
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

set1 = set(list1)
set2 = set(list2)

intersection_set = set1 & set2
result = (sorted(intersection_set))
print("Списки чисел ",list1,list2)
print("Пересечение ", result)

# Задание 4
n = 5
def func_square(x):
    return x**2
squares_dict = {}

for i in range(1,n+1):
    squares_dict[i] = func_square(i)
print("Число n ",n)
print("Словарь с квадратами ",squares_dict)