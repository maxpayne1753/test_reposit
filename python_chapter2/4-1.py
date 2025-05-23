

def add(a,b):
    return a+b

print(add(1,5))

def say():
    return 'HI'

a=say()
print(a)


def sub(a,b):
    return a-b
result = sub(a=7,b=3)
print(result)


def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result

print(add_many(1,2,3,4,5,6,7))


def say_myself(name,old,man=True):
    print("my name is %s . " % name)
    print("my old is %d ." % old)
    if man:
        print("im the guy")
    else:
        print("i am girl")
say_myself("Kimbyungchang",35)

say_myself("seominseo",35,False)



