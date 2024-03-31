#Pass_by_value
def update(x):
    print(id(x))
    x = 8
    print(id(x))
    print('x',x)
a = 10
print(id(a))
update(a)
print('a',a)

#Pass_by_reference
def update(x):
    print(id(x))
    x[1] = 25
    print(id(x))
    print('x',x)
a = [10,20,30]
print(id(a))
update(a)
print('a',a)