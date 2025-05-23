marks = [90,25,67,45,80]

number = 0
for mark in marks:
    number += 1
    if mark >=60:
        continue
        print("%d student is success" % number)
    else:
        print("%d student is fail" % number)

