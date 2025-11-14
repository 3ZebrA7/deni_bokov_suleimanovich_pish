# Задание 3
a = int(input("Введите a (для задания 3): "))
b = int(input("Введите b (для задания 3): "))

if a > b:
    print("Ошибка: a должно быть меньше или равно b")
else:
    s = 0
    for x in range(a, b + 1):
        s += x * x

    print("Сумма квадратов от", a, "до", b, "=", s)

# Задание 4
n = input("Введите целое число (для задания 4): ")
n = n.replace("-", "") # Убираем минус, если число отрицательное

if len(n) == 1:
    print(True)
else:
    up = True
    for i in range(len(n) - 1):
        if n[i] >= n[i + 1]:
            up = False
            break
    print(up)
