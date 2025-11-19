# Задание 1
sentence = "apple banana apple orange banana kiwi"
words = sentence.split()
unique_words = set(words)
result = sorted(list(unique_words))
print("Строка ",sentence)
print("Повторяющие слова ",result)
# Задание 2
string = "abracadabra"
chastota ={}
for char in string:
    if char in chastota:
        chastota[char] += 1
    else:
        chastota[char] = 1
print("Строка ", string)
print("Частота символов ",chastota)