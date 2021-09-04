def fun():
    yield 'c'
    yield 'd'
    yield 'f'
g=fun()
print(next(g))
print(next(g))
print(next(g))