list1=range(1,101)
for i in list1:
    if(i%2==0):
        print("The even numbers:",i)

for i in list1:
    if(i%2==0):
      #break the loop if the value is 50
        if(i==50):
            print("The even numbers:", i)
            break
for j in list1:
    if (j % 2 == 0):
        if (j==10):
            print("The even numbers 10 :",j)
            continue
        if(j==20):
            print("The even numbers 20 :",j)
            continue
        if (j==30):
            print("The even numbers 30: ",j)
            continue
        if(j==40):
            print("The even numbers 40: ",j)
            continue
        if (j ==50):
            print("The even numbers 50: ",j)
            continue
        if (j ==90):
            print("The even numbers 90: ",j)
            break

number = 1
while number <= 100:
    if(number % 2 != 0):
        print("The odd number")
        print("{0}".format(number))
    number = number + 1
for j in list1:
    if (j % 2 == 0):
        if (j==60):
            print("The numbers 60 :",j)
            continue
        if(j==70):
            print("The numbers 70 :",j)
            continue
        if (j==80):
            print("The numbers 80: ",j)
            continue
        if(j==90):
            print("The numbers 90: ",j)
            continue
        else:
            pass