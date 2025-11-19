# Задание 4
array =  [1,-2,3,4,-1,2,1,-5,4]
k = 3
max_sum = 0
best_block = []

for i in range(0,len(array), 1):
    block = array[i:i+k]

    if len(block) == k:
        nice_sum = 0

        for j in range(k):
            nice_sum += block[j]

        if nice_sum > max_sum:
            max_sum = nice_sum
            best_block = block[:]

print("Подмассив с максимальной суммой элементов ",best_block)
print("Сумма его элементов ",max_sum)
