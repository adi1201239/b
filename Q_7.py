for i in range(0,5,1):
	a=input("enter a no")
	list1.append(a)
print ("Elements of the list",list1)

# slicing operation
a =list1[0:int(len(list1)/2)]
print ("Sliced list is :-",a)

# Repetition with * operator
b = list1*2
print ("Repeatation of elements:-",b)

print ("Second list ")
list2 = []
for j in range(0,5,1):
	b=input("enter a no")
	list2.append(b)
print ("Elements of the list",list2)
print ("Concatenation of the 2 lists",list1+list2)