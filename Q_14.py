#a)...
listA=[]
listB=[]
for i in range(0,5,1):
	a=int(input("Enter Employee Id "))
	listA.append(a)
print ("Employee Id are",listA)

for j in range(0,5,1):
	b=str(input("Enter Employee Name "))
	listB.append(b)
print ("Employee Name are",listB)

#b)...
k=int(input("enter an index and index should be positive "))
if(k<5):
	print (listB[k])
else:
	print("invalid index")
#c)..
k=[]
k=listB[3:5]
print ("After slicing",k)

#e)..
l=[]
n=int(input("Specify the number of times "))
l=listB*n
print ("Repeatation of elements of listB ",l)

#f)...
k=[]
k=listA+listB
print ("Concatenation of two list is ",k)