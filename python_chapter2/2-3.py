odd = [1,2,3,4,5]
print(type(odd))
e = [1,2,'qwe','ertdfg']
print(e[2])
print(e[2]+e[3])

q = [1,2,3,['a','b','c']]
print(q[3])
print(q[0::2])
print(len(e+q))
q.insert(1,8)
print(q)
q.remove(8)
q.reverse()
print(q)
print(q.pop())
print(q)
print(q.count(1))
q.append([9,0])
print(q)
q.extend([7,8,9])
del q[3]
print(q)
print(q[1:2])
print(q)
