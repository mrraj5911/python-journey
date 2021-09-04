def fact(a):
    if a==0:
        result=1
    else:
        result=a*fact(a-1)
    return result
a=int(input('enter the number: '))
print(fact(a))