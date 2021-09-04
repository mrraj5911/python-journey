def ff(fu):
    def inner(name):
        print('2nd decor')
        fu(name)
    return inner

def f(fu):
    def inner(name):
        print('ist decor')
        fu(name)
    return inner
@f
@ff
def fun(name):
    print('hello')
fun('raj')