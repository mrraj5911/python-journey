def fu(f):
    def inner(a,b):
        if b==0:
            print('how can we divide with zero')
            return
        else:
            return f(a,b)
    return inner
@fu
def fun(a,b):
    return a/b
a=int(input('enter the number: '))
b=int(input('enter the second number: '))
print(fun(a,b))