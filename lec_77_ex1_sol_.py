def greater(a,b):
    if a>b:
        return a
    else:
        return b
num1=int(input("Enter first num: "))
num2=int(input("Enter second num:"))
bigger=greater(num1,num2)
print(bigger,"is greater",sep=" ")