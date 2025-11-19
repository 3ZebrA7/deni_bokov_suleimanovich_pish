 #Задание 3
array = [1,2,3,4,5,6,7]
block_size = 3
new_array = []

for i in range(0, len(array), block_size):
  block = array[i:i + block_size]


  if len(block) == block_size:
      block = block[::-1]
  new_array += block

print("Изначальный массив ",array)
print("Измененный массив ",new_array)