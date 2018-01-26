i = ['a', 'b']
l = [1, 2]

print(dict([i, l]))

l1 = [1, 2, 3, 6, 87, 3]
l2 = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff']
d = {}

for i in range(len(l1)):
    d[l1[i]] = l2[i]

print(d)

i = ['a', 'b', 'c']
l = [1, 2, 3]
b = dict(zip(i, l))
print(b)

print(list(zip(i, l)))

l1, l2, l3 = (1, 2, 3), (4, 5, 6), (7, 8, 9)
print(list(zip(l1, l2, l3)))

l1 = [2, 3, 4]
l2 = [4, 5, 6]
for x, y in zip(l1, l2):
    print(x, y, '--', x * y)


d={}
for i in range(len(l1)):
    d.setdefault(l1[i],l2[i])
print(d)