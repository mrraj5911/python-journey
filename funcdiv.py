def f(fu):
    def inner(a,b):
        if b==0:
            print('how can we divide with zero')
            return
        else:
            return fu(a,b)
    return inner
@f
def fun(a,b):
    return a/b
a=int(input('enter the first number: '))
b=int(input('enter the second number: '))
print(fun(a,b))