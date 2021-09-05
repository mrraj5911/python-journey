try:
    x=int(input("enter the first number: "))
    y=int(input("enter the second number: "))
    print(x/y)
except ZeroDivisionError:
    print("how can we divide by zero")
except ValueError:
    print("plz provide a valid number")