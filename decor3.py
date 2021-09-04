def f(fu):
    def inner():
        x=fu()
        return x*x
    return inner
@f
def fun():
    return 20
print(fun())