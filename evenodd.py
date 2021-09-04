def fun(a):
    if a%2==0:
        print("{} number is even".format(a))
    else:
        print("{} is odd number".format(a))
a=int(input('enter the number '))
fun(a)