import sys

# считывание аргументов командной строки
n = int(sys.argv[1])
m = int(sys.argv[2])

# создание кругового массива
massiv = [i for i in range(1, n+1)]

# обнуление переменных
iter = 0
elem=0
Flag= True
s=''

# цикл обхода по круговому массиву
while Flag:
    if iter == 0:
        s += str(massiv[elem])
    if elem > n-2:
        elem = 0
    else:
        elem += 1
    iter += 1
    if iter > m-1:
        iter = 0
        elem -=1
    if iter == 0 and elem == 0:
        Flag = False

# вывод результата
print(s)
