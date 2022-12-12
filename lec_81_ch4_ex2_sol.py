# def is_palindrome(a):
#     if a[:]==a[::-1]:
#         return True
#     else:
#         return False
# a=input("Enter the string:- ")
# print(is_palindrome(a))

                # #or

# def is_palindrome(a):
#     if a==a[::-1]:
#         return True
#     return False
# a=input("Enter the string:- ")
# print(is_palindrome(a))
           
            #or

def is_palindrome(a):
    return a==a[::-1]
a=input("Enter the string:- ")
print(is_palindrome(a))


