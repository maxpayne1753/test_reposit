s1 = set([1,2,3])
print(s1)
l1 = list(s1)
print(l1)

print(l1[0])
t1 = tuple(s1)
print(t1)
s1.clear()

print(s1)

s1 = set([1,2,3,4,5,6])


s2 = set([4,5,6,7,8,9])
print(s1&s2)

print(s1|s2)
print(s1-s2)
print(s2-s1)
s1.add(9)
print(s1)
