a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
c = int(input("Enter the third number"))
d = int(input("Enter the fourth number"))

if (a>b) & (a>c) & (a>d):
    print(a," is the greatest number")

elif (b>a) & (b>c) & (b>d):
    print(b," is the greatest number")

elif (c>a) & (c>b) & (c>d):
    print(c," is the greatest number")

else:
    print(d, " is the greatest number")