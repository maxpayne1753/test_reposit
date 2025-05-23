
a = 0
while a<10:
    a+=1
    if a % 2 == 0:
        continue
    print(a)
b = [(1,2), (3,4), (5,6)]
for (first, last) in b:
    print(first + last)
