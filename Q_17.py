import  math
list1 = []
for i in range(1,5,1):
    a = int(input("Enter the number "))
    list1.append(a)
print("Get the list",list1)

print("Get the biggest number from the list ", max(list1))
print("Get the smallest number from the list ", min(list1))