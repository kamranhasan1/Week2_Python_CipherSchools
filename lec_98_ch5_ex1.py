
def square_list(num):
    square=[]
    for i in num:
      square.append(i**2)
    return square
    
n=int(input())
number=list(range(n))
# n=int(input())
print(square_list(number))