import sys

# открытие и считывание первого файла с координатами
# центра окружности и радиуса
file1 = open(sys.argv[1], 'r')
file11 = file1.readlines()
x0, y0 = int(file11[0].split()[0]),  int(file11[0].split()[1])
r = int(file11[1])

# открытие второго файла на чтение с координатами точек
file2 = open(sys.argv[2], 'r')
res = ''

# считывание координат точек из второго файла
# и формирование результата
for i in file2:
    x = int(i.split()[0])
    y = int(i.split()[1])
    if (x - x0) ** 2 + (y - y0) ** 2 == r ** 2:
        res += '0'
    if (x - x0) ** 2 + (y - y0) ** 2 < r ** 2:
        res += '1'
    if (x - x0) ** 2 + (y - y0) ** 2 > r ** 2:
        res += '2'

# вывод результата
print(res)

# закрытие файлов
file1.close()
file2.close()