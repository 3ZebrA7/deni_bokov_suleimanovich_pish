# Задание 1
def f(x):
    if x < -2:
        return 4
    elif -2 <= x < 2:
        return x**2
    else:  # x >= 2
        return x**2 + 4*x + 5

# Ввод значения x от пользователя (целое число)
x = int(input("Введите значение x (для задания 1): "))

# Вычисление и вывод результата
print("f(x) =", f(x))

# Задание 2
def nod(a, b):
    while b != 0:
        a, b = b, a % b
    return a
a = int(input("Введите значение a (для задания 2): "))
b = int(input("Введите значение b (для задания 2): "))

print("Общий делитель nod=", nod(a, b))