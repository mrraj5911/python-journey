def mul(a,b):
    sum=a+b
    sub=a-b
    mult=a*b
    div=a/b
    return sum,sub,mult,div
a=int(input('enter the number: '))
b=int(input('enter the another number: '))
c=mul(a,b)
for i in c:
    print(i)