def dec(fu):
    def inner(name):
        print('outer')
        fu(name)
    return inner
def f(fu):
    def inner(name):
        print('inner decor')
        fu(name)
    return inner
@f
@dec
def fun(name):
    print('how are you')
fun('raj')