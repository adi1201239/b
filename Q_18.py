list1 = []
list2 = []
list3 = []
list4 = []

for i in range(1,101,1):
    s = 0
    s = s+i
    list1.append(s)
print("List of number from 1 to 100 using for loop",list1)

for i in range(1,101,1):
    s = 101
    s = s-i
    list2.append(s)
print("List of number from 100 to 1 using for loop",list2)

a = 0
while a <= 99:
    a+=1
    list3.append(a)
print("List of number from 1 to 100 using while loop",list3)

n=101
while(n>1):
    n-=1
    list4.append(n)
print("List of number from 1 to 100 using while loop",list4)
