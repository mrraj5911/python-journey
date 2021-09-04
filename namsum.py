def fun(name,*a):
    result=0
    for i in a:
        result+=i
    print("the sum by",name,":",result)
a=eval(input('enter the number: '))
name=input('enter the name: ')
fun(name,*a)