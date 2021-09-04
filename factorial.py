def fun(a):
    result=1
    while a>=1:
        result*=a
        a-=1
    return result
a=int(input('enter the number: '))
print(fun(a))