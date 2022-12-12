#practice for loop
# ask user a numberlike 1256
# calculate sum of digits ---> 1 + 2 + 5 + 6
# logic
# num="1256", length=4
# int(num[0])---> 1
# int(num[1])---> 4
# int(num[2])---> 5
# int(num[3])---> 6


total=0
num=input("enter a number : ")
for i in range(0,len(num)):
    total+=int(num[i])
    print(total)
    
