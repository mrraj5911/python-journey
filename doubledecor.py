def f(fu):
    def inner(name):
        if name=='raj':
            print('hellow, raj')
        else:
            fu(name)
    return inner
@f
def fun(name):
    print('how are you')
fun('raj')
fun("anuj")