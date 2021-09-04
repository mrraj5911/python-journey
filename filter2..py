from functools import *
a=eval(input('enter the list: '))
b=reduce(lambda x,y:x+y,a)
print(b)