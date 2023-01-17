
n = 5
m = 4

# sozdanie jrugovogo massiva
massiv = [i for i in range(1, n+1)]
iter = 0
elem=0
Flag= True
s=''
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
print(s)


'''
 0 1 2 3 
 1 2 3 4  n
 m - dlina obxoda 
'''