def fun():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
f=fun()
for i in f:
    if i>200:
        break
    print(i)