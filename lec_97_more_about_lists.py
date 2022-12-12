# generate lists with range functions
# something more about pop method
#index method
#pass list to a function



num=list(range(1,11))
# print(num)
# pop_item=num.pop()
# print(pop_item)
# print(num.index(3))
# print(num.index(5,1,6))

def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative
print(negative_list(num))


