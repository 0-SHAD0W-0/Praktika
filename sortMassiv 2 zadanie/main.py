a = [1, 4, 6]
b = [11, 33, 22]

x = zip(a,b)
xs = sorted(x, key=lambda tup: tup[1])

a1 = [x[0] for x in xs]
b1 = [x[1] for x in xs]
print(a1, b1)