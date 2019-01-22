count = 0
s = 0
numList = []

for n in range(1,11):
    a = int(input("Enter 10 numbers: "))
    numList.append(a)
    s += n
print("Sum all ten number",s)
print("list of ten number for addition", numList)

avg = int(s / n)
print("Average is ", avg)

print("Numbers less than average are :")

for i in numList:
    if (avg > i):
        print(i)
        count += 1

print("No of numbers less than average : ", count)

count = 0
print("Numbers greater than average are :")

for i in numList:
    if (avg < i):
        print(i)
        count += 1

print("No of numbers less than average : ", count)

count = 0
print("Numbers equal to average are :")

for i in numList:
    if (avg == i):
        print(i)
        count += 1

print("No of numbers equal to average : ", count)
