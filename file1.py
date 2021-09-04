def fun():
    yield 'a'
    yield 'b'
    yield 'c'
g=fun()
for i in g:
    print(i)