list1 = []
for i in range(0,5,1):
    a = str(input("Enter the name in list "))
    list1.append(a)
print("Name in list ",list1)

j = str(input("Enter the name to search "))
if j in list1:
    print("The given name is present in list")
else:
    print("The given name is not present in list")

l=len(list1)

for i in range(l+1):
    if (list1[i]==j):
         print ("element found  ")
         break
else:
    print ("element not  found")

list2 = list1[::-1]
print("list is reverse order ",list2)
