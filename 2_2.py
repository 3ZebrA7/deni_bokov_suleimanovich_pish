# Задание 3
def sum_equal_product(n):
    cifro = [int(a) for a in str(abs(n))]
    b = sum(cifro)
    c = 1
    for a in cifro:
        c *= a
    return b == c

n = int(input("Введите значение n (для задания 3): "))
print(sum_equal_product(n))

# Задание 4
def sum_of_cifro(x):
    return sum(int(d) for d in str(abs(x)))

x = int(input("Введите значение d (для задания 4): "))
print(sum_of_cifro(x))