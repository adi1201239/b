a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
c = int(input("Enter the third number"))

if (a>b) & (a>c):
    print("A is biggest number")

elif (b>a) & (b>c):
    print("B is the biggest number")

else:
    print("C is the biggest number")