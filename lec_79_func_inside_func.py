def greater(a,b):
    if a>b:
        return a
    else:
        return b

def greatest(a,b,c):
    if a>b>c:
        return a
    elif b>c>a:
        return b
    else:
        return c
def new_greatest(a,b,c):
    return greater(greater(a,b),c)
print(new_greatest(10,200,30))
   


