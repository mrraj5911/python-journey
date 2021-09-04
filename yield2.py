def fun(num):
    print('start coundown')
    while num>0:
        yield num
        num-=1
a=fun(10)
for i in a:
    print(i)