def fun(*a):
    result=0
    for i in a:
        result+=i
    print("the sum is:",result)
a=eval(input('enter the number: '))
fun(*a)