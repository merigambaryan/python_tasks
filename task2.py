

#из файла1
x0, y0 = 1, 1
r = 5
#из файла2
#for i in file2:
x=1
y=6
if (x - x0) ** 2 + (y - y0) ** 2 == r ** 2:
    res = 0
if (x - x0) ** 2 + (y - y0) ** 2 < r ** 2:
    res = 1
if (x - x0) ** 2 + (y - y0) ** 2 >= r ** 2:
    res = 2
print(res)