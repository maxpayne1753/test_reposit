a='i eat %d apples.' % 4
print(a)
num=10
day='three'
b='i ate {num} apples. so i was sick for {day} days.'.format(num=14,day='three')
print(b)

c='%0.6f' % 1.123456789
print(c)
d = "{0:<10}" .format("hi")
print(d)
f = "{0:>10}".format('hi')
print(f)
g = "{0:^10}".format('hi')
print(g)
h = "{0:*^30}".format('hi')
print(h)
