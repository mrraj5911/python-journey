def fun(**a):
    print('records')
    for k,v in a.items():
        print(k,"....",v)
name=input('enter the name: ')
marks=input('enter the marks: ')
fun(name=name,marks=marks)
clas=input('enter the class name: ')
age=input('enter the age')
fun(marks=marks,age=age)