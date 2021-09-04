def ff(fu):
    def inner():
        x=fu()
        return 2*x
    return inner

def f(fu):
    def inner():
        x=fu()
        return x*x
    return inner
@f
@ff
def fun():
    return 20
print(fun())