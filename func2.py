def fu(funn):
    def inner(name):
        if name=='raj':
            print('welcome',name)
        else:
            funn(name)
    return inner
@fu
def fun(name):
    print('hello,',name,' how are you')
fun('raj')
fun("rohit")