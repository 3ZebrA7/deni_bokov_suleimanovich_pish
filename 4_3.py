# Задание 5
string1 = "listen"
string2 = "silent"

def count_frequency(required_string):
    chastota = {}
    for char in required_string:
        chastota[char] = chastota.get(char, 0) + 1
    return chastota

if len(string1) != len(string2):
    is_anagram = False
else:
    chast1 = count_frequency(string1)
    chast2 =  count_frequency(string2)
    if chast1 == chast2:
        is_anagram = True
print("Слова ",string1,string2)
print("Это анаграмма? -", is_anagram)