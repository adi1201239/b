tuple1= input("Enter the values of tuple1:  ")
i=int(len(tuple1))
for i in tuple1:
    print ("tuple val", i)
s=tuple1[2:7]
# Slicing
print ("Slicing : ",s)
# Repeatition
rep=tuple1*5
print ("Repeatation : ",rep)

tuple2=input("Enter the values of tuple2:  ")

# Conacatination
tuple3=tuple1+tuple2
print ("Concatanated tup :  ",tuple3)
