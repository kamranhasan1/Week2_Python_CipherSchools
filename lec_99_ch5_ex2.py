# def reverse_list(a):
#      a.reverse()
#      return a
# num=[1,2,3,4]
# print(reverse_list(num))

# def reverse_list(a):
#     return a[::-1]
# num=[1,2,3,4]
# print(reverse_list(num))

def reverse_list(l):
    r_list = []
    for i in range(len(l)):
        popped_item = l.pop()
        r_list.append(popped_item)
    return r_list

numbers= [1,2,3,4,5]
print(reverse_list(numbers))

