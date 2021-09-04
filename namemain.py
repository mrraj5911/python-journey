def f():
    if __name__=='__main__':
        print('this is goood')
        print("the value of name is",__name__)
    else:
        print("the code is indirect")
        print("name is",__name__)
f()