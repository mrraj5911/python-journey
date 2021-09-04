def fun(a,b):
    sum=a+b
    sub=a-b
    return sum,sub
a=int(input('enter the number: '))
b=int(input('enter the another number: '))
print("the sum and the subtract  of {} and {} is {} ".format(a,b,fun(a,b)))