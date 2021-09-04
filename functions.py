def fun():
    def inner(a,b):
        print('the sum is',a+b)
        print('the average is',(a+b)/2)
    a=int(input('enter the first number: '))
    b=int(input('enter the second number: '))
    inner(a,b)
fun()