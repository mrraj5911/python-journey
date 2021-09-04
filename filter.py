def fun(a):
    if a%2==0:
        return True
    else:
        return False
b=[12,43,65,67,45,4,24]
c=list(filter(fun,b))
print(c)