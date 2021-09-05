try:
    x=int(input("enter the ist number: "))
    y=int(input("enter the 2nd number: "))
    print(x/y)
except (ZeroDivisionError,ValueError) as msg:
    print("please provide a valid number")