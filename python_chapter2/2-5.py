dic = { 'name' : 'byungchang', 'phone' : '010-1234-5678', 'birth' : '1125' }
a = { 1 : 'hi' }
a[2] = 'b'
print(a)
a['name'] = 'byungchang'
a[3] = [1,2,3]
print(a)
del a[1]
print(a)
print(dic.keys())

for k in a.keys():
	print(k)
print(list(a.keys()))
print(a.values())
print(a.items())
a.clear()
print(a)
print(dic.get('name'))
print(dic.get('nokey','none'))
print('name' in dic)
print('no' in dic)
test = {'name' : 'hong', 'birth' : 1125, 'age' : 30 }
print(test)
print(test['name'])
