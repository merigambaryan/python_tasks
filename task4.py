a = [9, 9, 9, 10]
m = sorted(a)[len(a) // 2]
print(sorted(a)[len(a) // 2])
print(sum(abs(i - m) for i in a))