import sys

# открытие файла с массивом nums
file1 = open(sys.argv[1], 'r')

# преобразование значений к целочисленным
nums = [int(i) for i in file1]

# сортировка и выборка среднего элемента массива
m = sorted(nums)[len(nums) // 2]

# подсчет шагов для приведения всех чисел массива к одному значению
print(sum(abs(i - m) for i in nums))

# закрытие файла
file1.close()