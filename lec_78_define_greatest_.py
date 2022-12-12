def greatest(a,b,c):
    if a>b>c:
        return a
    elif b>c>a:
        return b
    else:
        return c
x=int(input())
y=int(input())
z=int(input())
k=greatest(x,y,z)
print(k,"is greatest")


