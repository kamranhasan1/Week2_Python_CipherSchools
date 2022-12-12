#scope
x=5#gloabal variable
def func():
    global x
    x=6#local variable
    return x
print(func())
print(x)